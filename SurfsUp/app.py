###############################################
# Import the dependencies.

import numpy as np 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
import datetime as dt

from flask import Flask,jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
# Base.prepare(autoload_with=engine)
Base.prepare(engine, reflect=True)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
     return(
          f"Start at the homepage.<br/>"
          f"/api/v1.0/precipitation <br/>"
          f"/api/v1.0/stations <br/>"
          f"/api/v1.0/tobs <br/>"
          f"/api/v1.0/<start> <br/>"
          f"/api/v1.0/<start>/<end> <br/>")

#####################################################################

@app.route("/api/v1.0/precipitation")
def precipitation():

#  Convert the query results to a dictionary by using date as the key and prcp as the value.
     recent_date= dt.datetime(2017,8,23)

#  Calculate the date one year from the last date in data set.
     oneyear_prep = recent_date - dt.timedelta(365)


#  Perform a query to retrieve the data and precipitation scores
     # data = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>=oneyear_prep).all()

     results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=oneyear_prep).all()
     session.close()
# #Create dictionary 
     precipitation_data = {date: prcp for date, prcp in results}
     return jsonify(precipitation_data)

######################################################################

@app.route("/api/v1.0/stations")
def stations():
     session = Session(engine)
     results = session.query(Station.station).all()

     session.close()
# create list of stations from the dataset    
     all_stations = list(np.ravel(results)) 
     return jsonify(all_stations)

###########################################################################

@app.route("/api/v1.0/tobs")
# Query the dates and temperature observations of the most-active station for the previous year of data.
def temperature():

     recent_date= dt.datetime(2017,8,23)

#  Calculate the date one year from the last date in data set.
     oneyear_prep = recent_date - dt.timedelta(365)
     session = Session(engine)

     results = session.query(Measurement.date,Measurement.tobs).\
          filter(Measurement.station=='USC00519281').\
          filter(Measurement.date>=oneyear_prep).all()
     
     session.close()
#Create dictionary 
     temperature_data = [{"date": date, "tobs":tobs} for date, tobs in results]
     
     return jsonify(temperature_data)

######################################################################################

@app.route("/api/v1.0/<start>")
def start(start):
     """Get min, max and average temperature data from start date"""

     session = Session(engine)

# Create list for date and temperature values
     sel = [Measurement.date,
          func.min(Measurement.tobs), 
          func.max(Measurement.tobs), 
          func.avg(Measurement.tobs)]

# Perform a query to get TMIN, TAVG, and TMAX for all the dates 
# greater than or equal to the start date, taken as a parameter from the URL
     start_data = session.query(*sel).\
          filter(func.strftime("%Y-%m-%d", Measurement.date) >= start).\
          group_by(Measurement.date).\
          order_by(Measurement.date).all()

# Close the session
     session.close()
# Create a list of dictionary to store date, min, max and avg temperature values
     start_data_list = []
     for date, min, max, avg in start_data:
          start_dict = {}
          start_dict["date"] = date
          start_dict["min_temp"] = min
          start_dict["max_temp"] = max
          start_dict["avg_temp"] = avg
          start_data_list.append(start_dict)
# Return a JSON list of the minimum temperature, the average temperature, and the
# maximum temperature calculated from the given start date to the end of the dataset
     return jsonify(start_data_list)

######################################################################################

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
     """Get min, max and average temperature data from start date to end date"""

# Create our session (link) from Python to the DB
     session = Session(engine)

# Create list for date and temperature values
     sel = [Measurement.date,
          func.min(Measurement.tobs), 
          func.max(Measurement.tobs), 
          func.avg(Measurement.tobs)]

# Perform a query to get TMIN, TAVG, and TMAX for all the dates from start date to
# end date inclusive, taken as parameters from the URL
     start_end_data = session.query(*sel).\
                    filter(func.strftime("%Y-%m-%d", Measurement.date) >= start).\
                    filter(func.strftime("%Y-%m-%d", Measurement.date) <= end).\
                    group_by(Measurement.date).\
                    order_by(Measurement.date).all()
    
# Close the session
     session.close()

# Create a list of dictionary to store date, min, max and avg temperature values
     start_end_data_list = []
     for date, min, max, avg in start_end_data:
          start_dict = {}
          start_dict["date"] = date
          start_dict["min_temp"] = min
          start_dict["max_temp"] = max
          start_dict["avg_temp"] = avg
          start_end_data_list.append(start_dict)

# Return a JSON list of the minimum temperature, the average temperature, and the
# maximum temperature calculated from the given start date to the given end date
     return jsonify(start_end_data_list)

#############################################################################
if __name__=="__main__":
     app.run(debug=True)


