Summary: The purpose of this course project is to create SQL-based database that will be used for ride analytics for ride-sharing companies like Lyft and Ubebr. The database will be used to keep track of trips, ride fares, and demand surges, which are sudden spikes in ride-sharing activity. Trips can be tracked by having the drivers share their locations in real time. Recording a driver's latitude and longitude, along with a timestamp of when the driver was that location in the database can used to determine a given driver's location. Ride fares can be calculated by using the distance traveled, the time spent in the vehicle, and demand surges, which can cause the price of a trip to increase, depending on the number of drivers available. Furthermore, passenger discounts and the type of ride-sharing service (e.g. Uber Pool, UberX, UberXL) used are also used to calculate the total fare. The database must include measures to detect these demand surges, which involves looking at the number of ride requests and available drivers in an area during a specific period. Special events such as concerts and changes in weather such as rain and snow, can also have an effect on demand surges, so including data on weather patterns and special events in the database can help detect demand surges for ride-sharing applications. 

The stakeholders involved include ride-sharing companies such as Uber and Lyft, specifically data scientists and management boards. Data scientists can use and analyze the database to determine when demand surges occur, and management boards can use the analytics from the database to improve the user interface of their apps. Ride-sharing drivers and customers are also classified as steakholders becuase drivers can use the database in order to optimize their trips and customers are the main users of ride-sharing companies such as Uber. 

<img width="1229" height="1131" alt="Final_CourseProject_ER_Diagram drawio" src="https://github.com/user-attachments/assets/ff1c585a-c90b-45a9-b692-ec603586630a" />

https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city

https://www.kaggle.com/datasets/yasserh/uber-fares-dataset

https://www.kaggle.com/datasets/techabinesh/uber-dataset-for-eda

https://www.weather.gov/okx/LocalClimatologicalData

https://www.nyc.gov/site/nypd/stats/traffic-data/traffic-data-trafficstat.page

How to use this GitHub repository

Step 1: Run create_db.sql to create the database

Step 2: If the data being used to populate the database are all contained within a single csv file, run preprocess.py to seperate the data into their respective csv files, which will contain the data for each table in the database. If the data is seperated into their respective tables, move to Step 3

Step 3: Run the Python script load_data_local.py to load the data into the database using the command: python load_data_local.py

Step 4: Run the Python script app.py to access the database menu using the command: python -m streamlit run app.py

(Note: load_data_local.py and app.py both use SQLite3, so your OracleDB credentials are not required) 

