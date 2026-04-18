from datetime import datetime
import sys
import sqlite3

def connect_db():
    """Connect to local SQLite database"""
    db_path = "local_ridesharing.db"

    try:
        db = sqlite3.connect(db_path)
        db.row_factory = sqlite3.Row
        print(f"Connected to local SQLite database: {db_path}")
        return db
    except sqlite3.Error as err:
        print(f"Error connecting to local database: {err}")
        sys.exit(1)

def get_cursor(db):
    """Create a cursor for SQLite database"""
    return db.cursor()

def display_menu():
    print("\n" + "="*70)
    print("RIDE-SHARING DEMAND PRICING DATABASE - FEATURE MENU")
    print("="*70)
    print("1. Get all passengers of a specific driver")
    print("2. Get all special events in a certain area")
    print("3. Get total earnings of a specific driver")
    print("4. Get pickups on a certain day")
    print("5. Get occurrences count of a specific ride-sharing service")
    print("6. Exit")
    print("="*70)

def feature_1_passengers_by_driver(db):

    print("\n--- Selected 1: Get All Passengers of a Specific Driver ---")

    try:
        driver_id = int(input("Enter Driver ID: "))
        
        cursor = get_cursor(db)
        query = """
        SELECT DISTINCT p.PASS_ID, p.PASS_FNAME, p.PASS_LNAME, p.PASS_PHONE, p.PASS_EMAIL
        FROM Passenger p
        JOIN Ride r ON p.PASS_ID = r.PASS_ID
        WHERE r.DRIV_ID = ?
        ORDER BY p.PASS_LNAME, p.PASS_FNAME
        """
        cursor.execute(query, (driver_id,))
        results = cursor.fetchall()
        cursor.close()
        
        if not results:
            print(f"\nNo passengers found for driver ID {driver_id}.")

        else:
            print(f"\n{'='*70}")
            print(f"PASSENGERS FOR DRIVER ID: {driver_id}")
            print(f"{'='*70}")
            print(f"{'ID':<6} {'First Name':<15} {'Last Name':<15} {'Phone':<15} {'Email':<20}")
            print("-"*70)
            for row in results:
                print(f"{row['PASS_ID']:<6} {row['PASS_FNAME']:<15} {row['PASS_LNAME']:<15} {row['PASS_PHONE']:<15} {row['PASS_EMAIL']:<20}")
            print(f"{'='*70}")
            print(f"Total passengers found: {len(results)}\n")

    except ValueError:
        print("Invalid input. Please enter a numeric driver ID.")

    except Exception as err:
        print(f"Database error: {err}")

def feature_2_events_by_area(db):

    print("\n--- Selected 2: Get All Special Events in a Certain Area ---")

    try:
        area_id = int(input("Enter Area ID: "))
        
        cursor = get_cursor(db)
        query = """
        SELECT e.EVENT_ID, e.EVENT_NAME, e.EVENT_STREET, e.EVENT_ZIP, 
               e.BUILDING_NUM, e.EVENT_START, e.EVENT_END, a.CITY_NAME, a.STATE_NAME
        FROM Special_Event e
        JOIN Area_Loc a ON e.AREA_ID = a.AREA_ID
        WHERE a.AREA_ID = ?
        ORDER BY e.EVENT_START DESC
        """
        cursor.execute(query, (area_id,))
        results = cursor.fetchall()
        cursor.close()
        
        if not results:
            print(f"\nNo events found for area ID {area_id}.")

        else:
            print(f"\n{'='*70}")
            print(f"SPECIAL EVENTS IN AREA ID: {area_id}")
            print(f"{'='*70}")
            for i, row in enumerate(results, 1):
                print(f"\nEvent {i}:")
                print(f"  Event ID: {row['EVENT_ID']}")
                print(f"  Event Name: {row['EVENT_NAME']}")
                print(f"  Location: {row['EVENT_STREET']}, {row['BUILDING_NUM']}, {row['EVENT_ZIP']}")
                print(f"  City, State: {row['CITY_NAME']}, {row['STATE_NAME']}")
                print(f"  Start Date: {row['EVENT_START']}")
                print(f"  End Date: {row['EVENT_END']}")
            print(f"\n{'='*70}")
            print(f"Total events found: {len(results)}\n")

    except ValueError:
        print("Invalid input. Please enter a numeric area ID.")

    except Exception as err:
        print(f"Database error: {err}")

def feature_3_driver_earnings(db):

    print("\n--- Selected 3: Get Total Earnings of a Specific Driver ---")

    try:
        driver_id = int(input("Enter Driver ID: "))
        
        cursor = get_cursor(db)
        query = """
        SELECT d.DRIV_ID, d.DRIV_FNAME, d.DRIV_LNAME, 
               COUNT(r.RIDE_ID) as TOTAL_RIDES,
               SUM(p.PAY_AMOUNT) as TOTAL_EARNINGS
        FROM Driver d
        JOIN Ride r ON d.DRIV_ID = r.DRIV_ID
        JOIN Payment p ON r.RIDE_ID = p.RIDE_ID
        WHERE d.DRIV_ID = ?
        GROUP BY d.DRIV_ID, d.DRIV_FNAME, d.DRIV_LNAME
        """
        cursor.execute(query, (driver_id,))
        results = cursor.fetchall()
        cursor.close()
        
        if not results:
            print(f"\nNo earnings found for driver ID {driver_id}.")

        else:
            row = results[0]
            print(f"\n{'='*70}")
            print(f"EARNINGS SUMMARY FOR DRIVER")
            print(f"{'='*70}")
            print(f"Driver ID: {row['DRIV_ID']}")
            print(f"Driver Name: {row['DRIV_FNAME']} {row['DRIV_LNAME']}")
            print(f"Total Rides: {row['TOTAL_RIDES']}")
            print(f"Total Earnings: ${row['TOTAL_EARNINGS']:.2f}")
            print(f"Average Earnings per Ride: ${row['TOTAL_EARNINGS']/row['TOTAL_RIDES']:.2f}")
            print(f"{'='*70}\n")

    except ValueError:
        print("Invalid input. Please enter a numeric driver ID.")

    except Exception as err:
        print(f"Database error: {err}")

def feature_4_pickups_by_day(db):

    print("\n--- Selected 4: Get Pickups on a Certain Day ---")

    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        # Validate date format
        datetime.strptime(date_str, "%Y-%m-%d")
        
        cursor = get_cursor(db)
        query = """
        SELECT r.RIDE_ID, r.DRIV_ID, r.PASS_ID, r.REQUEST_TIME, 
               r.PICKUP_LOCATION, r.DROPOFF_LOCATION, r.DIST_TRAVELED, 
               r.BASE_FARE, r.TRIP_DURATION,
               d.DRIV_FNAME, d.DRIV_LNAME,
               p.PASS_FNAME, p.PASS_LNAME
        FROM Ride r
        JOIN Driver d ON r.DRIV_ID = d.DRIV_ID
        JOIN Passenger p ON r.PASS_ID = p.PASS_ID
        WHERE DATE(r.REQUEST_TIME) = ?
        ORDER BY r.REQUEST_TIME DESC
        """
        cursor.execute(query, (date_str,))
        results = cursor.fetchall()
        cursor.close()
        
        if not results:
            print(f"\nNo pickups found on {date_str}.")

        else:
            print(f"\n{'='*70}")
            print(f"PICKUPS ON {date_str}")
            print(f"{'='*70}")
            print(f"{'Ride ID':<8} {'Driver':<15} {'Passenger':<15} {'Pickup Location':<20} {'Dropoff':<20} {'Distance':<8} {'Fare':<8}")
            print("-"*100)
            for row in results:
                driver_name = f"{row['DRIV_FNAME']} {row['DRIV_LNAME']}"[:14]
                passenger_name = f"{row['PASS_FNAME']} {row['PASS_LNAME']}"[:14]
                print(f"{row['RIDE_ID']:<8} {driver_name:<15} {passenger_name:<15} {row['PICKUP_LOCATION']:<20} {row['DROPOFF_LOCATION']:<20} {row['DIST_TRAVELED']:<8.2f} ${row['BASE_FARE']:<7.2f}")
            print(f"{'='*70}")
            print(f"Total pickups on {date_str}: {len(results)}\n")

    except ValueError as e:
        print(f"Invalid date format. Please use YYYY-MM-DD format. Error: {e}")

    except Exception as err:
        print(f"Database error: {err}")

def feature_5_service_occurrences(db):

    print("\n--- Selected 5: Get Occurrences Count of a Specific Service ---")

    # First, show available services
    try:
        cursor = get_cursor(db)
        services_query = "SELECT SERV_TYPE_ID, SERV_NAME FROM Service_Type ORDER BY SERV_NAME"
        cursor.execute(services_query)
        services = cursor.fetchall()
        
        if not services:
            print("No services found in the database.")
            cursor.close()
            return
        
        print("\nAvailable Services:")
        for service in services:
            print(f"  ID: {service['SERV_TYPE_ID']} - {service['SERV_NAME']}")
        
        service_id = int(input("\nEnter Service Type ID: "))
        
        cursor2 = get_cursor(db)
        query = """
        SELECT st.SERV_TYPE_ID, st.SERV_NAME, COUNT(rs.RIDE_ID) as OCCURRENCE_COUNT
        FROM Service_Type st
        LEFT JOIN Ride_Service rs ON st.SERV_TYPE_ID = rs.SERV_TYPE_ID
        WHERE st.SERV_TYPE_ID = ?
        GROUP BY st.SERV_TYPE_ID, st.SERV_NAME
        """
        cursor2.execute(query, (service_id,))
        results = cursor2.fetchall()
        cursor2.close()
        
        if not results:
            print(f"\nNo service found with ID {service_id}.")

        else:
            row = results[0]
            print(f"\n{'='*70}")
            print(f"SERVICE OCCURRENCES")
            print(f"{'='*70}")
            print(f"Service Type ID: {row['SERV_TYPE_ID']}")
            print(f"Service Name: {row['SERV_NAME']}")
            print(f"Total Occurrences: {row['OCCURRENCE_COUNT']}")
            print(f"{'='*70}\n")

    except ValueError:
        print("Invalid input. Please enter a numeric service ID.")

    except Exception as err:
        print(f"Database error: {err}")

def main():

    print("\nWelcome to the Ride-Sharing Demand Pricing Database Application!")

    db = connect_db()

    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                feature_1_passengers_by_driver(db)
            elif choice == '2':
                feature_2_events_by_area(db)
            elif choice == '3':
                feature_3_driver_earnings(db)
            elif choice == '4':
                feature_4_pickups_by_day(db)
            elif choice == '5':
                feature_5_service_occurrences(db)
            elif choice == '6':
                print("\nThank you for using the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
