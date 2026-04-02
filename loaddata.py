import mysql.connector 
import pandas as pd 

db = mysql.connector.connect(
    host = "db.freesql.com",
    user = "JWHALEN0130_SCHEMA_ZDAG9",
    password = "POS8$12OIN3K7M1UCY84L2237P8GaE",
    database = "Ride_Sharing_Analytics"
)

cursor = db.cursor()

def load_csv(file, table):
    df = pd.read_csv(file)

    for _, row in df.iterrows():
        placeholders = ','.join(['%s'] * len(row))
        sql = f"INSERT INTO {table} VALUES ({placeholders})"
        cursor.execute(sql, tuple(row))
    
    db.commit()
    print(f"{table} loaded")

load_csv("ride.csv", "Ride")
load_csv("driver.csv", "Driver")
load_csv("passenger.csv", "Passenger")
load_csv("driverLocation.csv", "Driver Location")
load_csv("payment.csv", "Payment")
load_csv("rideService.csv", "Driver Location")
load_csv("serviceType.csv", "Service Type")
load_csv("area.csv", "Area")
load_csv("demandSurge.csv", "Demand Surge")
load_csv("weather.csv", "Weather")
load_csv("specialEvent.csv", "Special Event")

cursor.close()
db.close()