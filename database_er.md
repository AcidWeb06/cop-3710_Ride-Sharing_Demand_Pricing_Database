<img width="1230" height="1071" alt="CourseProject_PartB drawio (1)" src="https://github.com/user-attachments/assets/bc3ecc86-cebe-45ab-b1a5-80361d36323f" />

Table Driver
  DRIV_ID - Identifier
  DRIV_LNAME - Simple
  DRIV_FNAME - Simple
  DRIV_PHONE - Optional
  LICENSE_NUM - Required
  DRIV_LONGITUDE - Single-valued
  DRIV_LATITUDE - Single-valued
  DRIV_STATUS - Single-valued

Table Driver Location
  DRIV_ID - Identifier
  DRIV_TIMESTAMP - Identifier
  LONGITUDE - Required
  LATITUDE - Required

Table Passenger 
  PASS_ID - Identifier
  PASS_LNAME - Simple
  PASS_FNAME - Simple 
  PASS_PHONE - Optional
  PASS_EMAIL - Single-valued

Table Ride
  RIDE_ID - Identifier
  DRIV_ID - Required
  PASS_ID - Required 
  REQUEST_TIME - Single-valued
  PICKUP_LOCATION - Required
  DROPOFF_LOCATION - Required 
  DIST_TRAVELED - Required 
  BASE_FARE - Required 
  TRIP_DURATION - Single-valued
  SUR_MULTIPLIER - Required
  TOTAL_FARE - Single-valued 

Table Payment
  PAY_ID - Identifer 
  RIDE_ID - Required
  PAY_DATE - Single-valued
  PAY_AMOUNT - Simple 
  PAY_METHOD - Single-valued
  PAY_STATUS - Simple

Table Ride Service
  RIDE_ID - Identifer
  SERVICE_TYPE_ID - Identifier
  APPLIED_RATE - Single-valued

Table Service Type
  SERVICE_TYPE_ID - Identifier
  SERVICE_NAME - Single-valued 
  BASE_RATE - Single-valued

Table Area
  AREA_ID - Identifer 
  CITY_NAME - Single-valued
  STATE_NAME - Simple
  AREA_DENSITY - Single-valued

Table Special Event
  EVENT_ID - Identifier
  AREA_ID - Required 
  EVENT_NAME - Simple
  EVENT_LOCATION - Composite 
  EVENT_START - Single-valued
  EVENT_END - Single-valued 

Table Weather
  WEATHER_ID -Identifier
  AREA_ID - Required 
  WEAT_TIME - Single-valued
  WEAT_CONDITION - Simple 
  TEMPERATURE - Single-valued 

Table Demand Surge
  SUR_ID - Identifier 
  AREA_ID - Required 
  START_TIME - Single-valued
  END_TIME - Single-valued
  SUR_MULTIPLIER - Single-valued 
  SUR_REASON - Required 
