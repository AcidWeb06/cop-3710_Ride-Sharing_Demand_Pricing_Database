import sqlite3
import csv
import os

db_path = "local_ridesharing.db"
db = sqlite3.connect(db_path)
cursor = db.cursor()

# Create tables
cursor.executescript("""
DROP TABLE IF EXISTS Ride_Service;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Ride;
DROP TABLE IF EXISTS Special_Event;
DROP TABLE IF EXISTS Demand_Surge;
DROP TABLE IF EXISTS Weather;
DROP TABLE IF EXISTS Area_Loc;
DROP TABLE IF EXISTS Service_Type;
DROP TABLE IF EXISTS Passenger;
DROP TABLE IF EXISTS Driver;

CREATE TABLE Driver (
    DRIV_ID TEXT PRIMARY KEY,
    DRIV_LNAME TEXT, DRIV_FNAME TEXT,
    DRIV_PHONE TEXT, LICENSE_NUM TEXT, DRIV_STATUS TEXT
);
CREATE TABLE Passenger (
    PASS_ID TEXT PRIMARY KEY,
    PASS_LNAME TEXT, PASS_FNAME TEXT,
    PASS_EMAIL TEXT, PASS_PHONE TEXT
);
CREATE TABLE Ride (
    RIDE_ID TEXT PRIMARY KEY,
    DRIV_ID TEXT, PASS_ID TEXT,
    REQUEST_TIME TEXT, PICKUP_LOCATION TEXT, DROPOFF_LOCATION TEXT,
    DIST_TRAVELED REAL, BASE_FARE REAL, TRIP_DURATION REAL,
    FOREIGN KEY(DRIV_ID) REFERENCES Driver(DRIV_ID),
    FOREIGN KEY(PASS_ID) REFERENCES Passenger(PASS_ID)
);
CREATE TABLE Payment (
    PAY_ID TEXT PRIMARY KEY, RIDE_ID TEXT,
    PAY_DATE TEXT, PAY_AMOUNT REAL, PAY_METHOD TEXT, PAY_STATUS TEXT,
    FOREIGN KEY(RIDE_ID) REFERENCES Ride(RIDE_ID)
);
CREATE TABLE Area_Loc (
    AREA_ID TEXT PRIMARY KEY,
    CITY_NAME TEXT, STATE_NAME TEXT, AREA_DENSITY TEXT
);
CREATE TABLE Special_Event (
    EVENT_ID TEXT PRIMARY KEY, AREA_ID TEXT,
    EVENT_NAME TEXT, EVENT_STREET TEXT, EVENT_ZIP TEXT,
    BUILDING_NUM TEXT, EVENT_START TEXT, EVENT_END TEXT,
    FOREIGN KEY(AREA_ID) REFERENCES Area_Loc(AREA_ID)
);
CREATE TABLE Service_Type (
    SERV_TYPE_ID TEXT PRIMARY KEY,
    SERV_NAME TEXT, BASE_RATE REAL
);
CREATE TABLE Ride_Service (
    RIDE_ID TEXT, SERV_TYPE_ID TEXT, APPLIED_RATE REAL,
    PRIMARY KEY(RIDE_ID, SERV_TYPE_ID)
);
""")
db.commit()


def clean(val):
    v = str(val).strip()
    if v.endswith('.0') and v[:-2].isdigit():
        v = v[:-2]
    return None if v in ('', 'nan') else v


def load_csv(file, table, csv_cols, db_cols):
    filepath = os.path.join("data", file)
    rows = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append([clean(row.get(col, '')) for col in csv_cols])
    placeholders = ','.join(['?'] * len(db_cols))
    col_str = ','.join(db_cols)
    cursor.executemany(
        f"INSERT OR IGNORE INTO {table} ({col_str}) VALUES ({placeholders})",
        rows
    )
    db.commit()
    print(f"{table}: {len(rows)} rows loaded")


load_csv("driver.csv",       "Driver",
         ["DRIV_ID","DRIV_LNAME","DRIV_FNAME","DRIV_PHONE","LICENSE_NUM","DRIV_STATUS"],
         ["DRIV_ID","DRIV_LNAME","DRIV_FNAME","DRIV_PHONE","LICENSE_NUM","DRIV_STATUS"])

load_csv("passenger.csv",    "Passenger",
         ["PASS_ID","PASS_LNAME","PASS_FNAME","PASS_EMAIL","PASS_PHONE"],
         ["PASS_ID","PASS_LNAME","PASS_FNAME","PASS_EMAIL","PASS_PHONE"])

load_csv("ride.csv",         "Ride",
         ["RIDE_ID","DRIV_ID","PASS_ID","REQUEST_TIME","PICKUP","DROPOFF","DIST_TRAVELED","BASE_FARE","TRIP_DURATION"],
         ["RIDE_ID","DRIV_ID","PASS_ID","REQUEST_TIME","PICKUP_LOCATION","DROPOFF_LOCATION","DIST_TRAVELED","BASE_FARE","TRIP_DURATION"])

load_csv("payment.csv",      "Payment",
         ["PAY_ID","RIDE_ID","PAY_DATE","PAY_AMOUNT","PAY_METHOD","PAY_STATUS"],
         ["PAY_ID","RIDE_ID","PAY_DATE","PAY_AMOUNT","PAY_METHOD","PAY_STATUS"])

load_csv("area.csv",         "Area_Loc",
         ["AREA_ID","CITY_NAME","STATE_NAME","AREA_DENSITY"],
         ["AREA_ID","CITY_NAME","STATE_NAME","AREA_DENSITY"])

load_csv("specialEvent.csv", "Special_Event",
         ["EVENT_ID","AREA_ID","EVENT_NAME","EVENT_STREET","EVENT_ZIP","BUILDING_NUM","EVENT_START","EVENT_END"],
         ["EVENT_ID","AREA_ID","EVENT_NAME","EVENT_STREET","EVENT_ZIP","BUILDING_NUM","EVENT_START","EVENT_END"])

load_csv("serviceType.csv",  "Service_Type",
         ["SERVICE_TYPE_ID","SERVICE_NAME","BASE_RATE"],
         ["SERV_TYPE_ID","SERV_NAME","BASE_RATE"])

load_csv("rideService.csv",  "Ride_Service",
         ["RIDE_ID","SERVICE_TYPE_ID","APPLIED_RATE"],
         ["RIDE_ID","SERV_TYPE_ID","APPLIED_RATE"])

cursor.close()
db.close()
print("\nDatabase ready at local_ridesharing.db")