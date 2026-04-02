import pandas as pd

raw_data = pd.read_csv("C:\\Users\\jwhal\\OneDrive\\Documents\\RideSharingAnalytics.csv")

raw_data.columns = raw_data.columns.str.strip()

raw_data = raw_data.drop_duplicates()
raw_data = raw_data.dropna(subset=["ride_id", "driv_id", "pass_id"])

ride_df = raw_data[[
    'ride_id', 
    'driv_id', 
    'pass_id', 
    'request_time', 
    'pickup', 
    'dropoff', 
    'dist_travled', 
    'base_fare', 
    'trip_duration', 
    'demsur_multiplier'
]].drop_duplicates()

ride_df.columns = [
    "RIDE_ID", 
    "DRIV_ID", 
    "PASS_ID", 
    "REQUEST_TIME", 
    "PICKUP_LOCATION", 
    "DROPOFF_LOCATION", 
    "DIST_TRAVELED", 
    "BASE_FARE", 
    "TRIP_DURATION", 
    "DEMSUR_MULTIPLIER"
]

ride_df.to_csv("csv_output/ride.csv", index=False)

driver_df = raw_data[[
    'driv_id', 
    'driv_lname', 
    'driv_fname', 
    'driv_phone', 
    'license_num', 
    'driv_longitude', 
    'driv_latitude', 
    'driv_status'
]].drop_duplicates()

driver_df.columns = [
    "DRIV_ID", 
    "DRIV_LNAME", 
    "DRIV_FNAME", 
    "DRIV_PHONE", 
    "LICENSE_NUM", 
    "DRIV_LONGITUDE", 
    "DRIV_LATITUDE", 
    "DRIV_STATUS"
]

driver_df.to_csv("csv_output/driver.csv", index=False)

passenger_df = raw_data[[
    'pass_id',
    'pass_lname', 
    'pass_fname', 
    'pass_email', 
    'pass_phone'
]].drop_duplicates()

passenger_df.columns = [
    "PASS_ID",
    "PASS_LNAME", 
    "PASS_FNAME", 
    "PASS_EMAIL", 
    "PASS_PHONE"
]

passenger_df.to_csv("csv_output/passenger.csv", index=False)

driverLocation_df = raw_data[[
    'driv_id', 
    'driv_timestamp',
    'longitude', 
    'latitude'
]].drop_duplicates()

driverLocation_df.columns = [
    "DRIV_ID", 
    "DRIV_TIMESTAMP",
    "LONGITUDE", 
    "LATITUDE"
]

driverLocation_df.to_csv("csv_output/driverLocation.csv", index=False)

payment_df = raw_data[[
    'pay_id', 
    'ride_id', 
    'pay_date', 
    'pay_amount', 
    'pay_method', 
    'pay_status'
]].drop_duplicates()

payment_df.columns = [
    "PAY_ID", 
    "RIDE_ID", 
    "PAY_DATE", 
    "PAY_AMOUNT", 
    "PAY_METHOD", 
    "PAY_STATUS"
]

payment_df.to_csv("csv_output/payment.csv", index=False)

rideService_df = raw_data[[
    'ride_id', 
    'service_type_id', 
    'applied_rate'
]].drop_duplicates()

rideService_df.columns = [
    "RIDE_ID", 
    "SERVICE_TYPE_ID", 
    "APPLIED_RATE"
]

rideService_df.to_csv("csv_output/rideService.csv", index=False)

serviceType_df = raw_data[[
    'service_type_id', 
    'service_name', 
    'base_rate'
]].drop_duplicates()

serviceType_df.columns = [
    "SERVICE_TYPE_ID", 
    "SERVICE_NAME", 
    "BASE_RATE"
]

serviceType_df.to_csv("csv_output/serviceType.csv", index=False)

area_loc_df = raw_data[[
    'area_id',
    'city_name', 
    'state_name', 
    'area_density'
]].drop_duplicates()

area_loc_df.columns = [
    "AREA_ID",
    "CITY_NAME", 
    "STATE_NAME", 
    "AREA_DENSITY"
]

area_loc_df.to_csv("csv_output/area.csv", index=False)

demandSurge_df = raw_data[[
    'demsur_id',
    'area_id', 
    'starting_time', 
    'ending_time', 
    'demsur_multiplier', 
    'demsur_reason'
]].drop_duplicates()

demandSurge_df.columns = [
    "DEMSUR_ID",
    "AREA_ID", 
    "STARTING_TIME", 
    "ENDING_TIME", 
    "DEMSUR_MULTIPLIER", 
    "DEMSUR_REASON"
]

demandSurge_df.to_csv("csv_output/demandSurge.csv", index=False)

weather_df = raw_data[[
    'weather_id', 
    'area_id', 
    'weat_time', 
    'weat_condtion', 
    'temperature'
]].drop_duplicates()

weather_df.columns = [
    "WEATHER_ID", 
    "AREA_ID", 
    "WEAT_TIME", 
    "WEAT_CONDITION", 
    "TEMPERATURE"
]

weather_df.to_csv("csv_output/weather.csv", index=False)

specialEvent_df = raw_data[[
    'event_id', 
    'area_id', 
    'event_name', 
    'event_street', 
    'event_zip', 
    'building_num', 
    'event_start', 
    'event_end'
]].drop_duplicates()

specialEvent_df.columns = [
     "EVENT_ID", 
     "AREA_ID", 
     "EVENT_NAME", 
     "EVENT_STREET", 
     "EVENT_ZIP", 
     "BUILDING_NUM", 
     "EVENT_START", 
     "EVENT_END"
]

specialEvent_df.to_csv("csv_output/specialEvent.csv", index=False)


