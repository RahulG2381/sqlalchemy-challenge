# sqlalchemy-challenge
# SurfsUP - Climate Data Analysis and Climate API app
The project analyzes the Climate and Station data for holiday vacation in Honolulu, Hawaii. The project performs climate analysis about the area by exploring climate data and creating an app.
It has two parts
1.	Analyse and Explore the Climate Data
2.	Design Your Climate App
## Part 1:
In this segment of the project, Python and SQLAlchemy are employed to conduct a fundamental climate analysis and explore data within the SQLite climate database. This involves utilizing SQLAlchemy functions such as create_engine() and automap_base() to establish a connection to the database and map tables into classes, namely 'station' and 'measurement'. Subsequently, the data is scrutinized through the creation of sessions, execution of queries, and subsequent closure of the sessions. The analysis leverages ORM queries, Pandas, and Matplotlib for a comprehensive exploration of the data.
## Precipitation Analysis
1.	Finding the most recent date in the dataset.
2.	Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3.	Selecting only the "date" and "prcp" values.
4.	Loading the query results into a Pandas DataFrame. Explicitly set the column names.
5.	Sorting the DataFrame values by "date".
6.	Ploting the results by using the DataFrame plot method,
7.	Useing Pandas to print the summary statistics for the precipitation data.

## Station Analysis
1.	Designing a query to calculate the total number of stations in the dataset.
2.	Designing a query to find the most-active stations (that is, the stations that have the most rows). 
3.	Design a query to get the previous 12 months of temperature observation (TOBS) data. 
4.	Close the session.

## Part 2: Design Your Climate App
After completing our initial analysis, i desinged a Flask API based on the queries to develope app. To do so, i have then used Flask to create my routes as follows:
1.	/
•	To start the homepage.
•	Listed all the available routes.
2.	/api/v1.0/precipitation
•	Converted the query results to a dictionary by using date as the key and prcp as the value.
•	Returned the JSON representation of your dictionary.
3.	/api/v1.0/stations
•	Returned a JSON list of stations from the dataset.
4.	/api/v1.0/tobs
•	Query the dates and temperature observations of the most-active station for the previous year of data.
•	Return a JSON list of temperature observations for the previous year.
5.	/api/v1.0/<start> and /api/v1.0/<start>/<end>
•	Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
•	For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
•	For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


