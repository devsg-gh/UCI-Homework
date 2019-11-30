#Adding the dependecies
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br>"
	    f"/api/v1.0/tobs<br>"
	    f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    prcp_data = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date).all()
    session.close()
 #Convert the query results to a Dictionary using date as the key and prcp as the value.           
    results = dict(prcp_data)
 #Return the JSON representation of your dictionary.
    return jsonify(results)


@app.route("/api/v1.0/stations")
def station():
#Return a JSON list of stations from the dataset.
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations names"""
    # Query all passengers
    results = session.query(Station.station).all() 

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():

#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.

    session = Session(engine)
    last_date = session.query(func.max(Measurement.date)).scalar()
    parsed_max_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    last_year_date = parsed_max_date - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date,Measurement.tobs).\
            filter(Measurement.date >= last_year_date.date()).all()
    session.close()

     # Convert list of tuples into normal list
    tobs_dict = dict(tobs_data)
    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>")
def start_date(start):
    """Fetch a JSON list of minimum temperatures, average temperatures, and max temperatures for a given start"""
    session = Session(engine)
    
    start_result = session.query(func.min(Measurement.tobs).label("TMIN"), func.avg(Measurement.tobs).label("TAVG"), func.max(Measurement.tobs).label("TMAX")).\
        filter(Measurement.date >= start).all()
    session.close()

    start_temp_info = []
    #converting list in to a dictionary
    for row in start_result:
        row_dict = {}
        row_dict["minimum temperature"] = row.TMIN
        row_dict["maximum temperature"] = row.TMAX
        row_dict["average temperature"] = row.TAVG
        start_temp_info.append(row_dict)

    return jsonify(start_temp_info)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Fetch a JSON list of minimum temperatures, average temperatures, and max temperatures for a given start"""
    session = Session(engine)
    
    start_end_result = session.query(func.min(Measurement.tobs).label("TMIN"), func.avg(Measurement.tobs).label("TAVG"), func.max(Measurement.tobs).label("TMAX")).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    #converting list in to a dictionary
    temp_info = []
    
    for row in start_end_result:
        row_dict = {}
        row_dict["minimum temperature"] = row.TMIN
        row_dict["maximum temperature"] = row.TMAX
        row_dict["average temperature"] = row.TAVG
        temp_info.append(row_dict)

    return jsonify(temp_info)

 
if __name__ == '__main__':
    app.run(debug=True)

