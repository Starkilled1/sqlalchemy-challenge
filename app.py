# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
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
    
    '''List all available api routes'''
    return ("""
    <h1>Climate App</h1>
    <h3>Available Routes:</h3>
    <ul>
        <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
        <li><a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
        <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
        <li>/api/v1.0/&lt;start&gt;</li>
        <li>/api/v1.0/&lt;start&gt;/&lt;end&gt;</li>
    </ul>
    """)


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #using recommended method for opening sessions in sqlalchemy 2.0
    with Session(engine) as session:
        #calculate most recent data in the db
        
        recent_date = session.query(func.max(Measurement.date)).scalar()
        #making and obj in order to fin the date from one year ago 
        recent_obj = dt.datetime.strptime(recent_date, '%Y-%m-%d')
        one_year_ago = recent_obj - dt.timedelta(days=366)
        
        #query to find the precipitation data and dates
        result = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
        precipitation_data = {row.date: row.prcp for row in result}
        
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    # This section uses the execute query command because is more simple
    query = text("SELECT station FROM station")
    with Session(engine) as session:
        result = session.execute(query)
        stations = [row.station for row in result]
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # defined station with most activity for the query filter
    most_active_id = 'USC00519281'
    
    #start of autoending session
    with Session(engine) as session:
        #calculate most recent data in the db
        recent_date = session.query(func.max(Measurement.date)).scalar()
        #making and obj in order to fin the date from one year ago  
        recent_obj = dt.datetime.strptime(recent_date, '%Y-%m-%d')
        one_year_ago = recent_obj - dt.timedelta(days=366)
        
        station_query = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_id).\
                        filter(Measurement.date >= one_year_ago).all()
        tobs_data = {row.date: row.tobs for row in station_query}
        
    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
def start(start):
    
    #start of autoending session
    with Session(engine) as session:
        #making sure that the start variable of the endpoint is a date
        start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()
        #query to obtain the min, avg and max using the date as a filter
        result =session.query(func.min(Measurement.tobs), 
                              func.avg(Measurement.tobs), 
                              func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
        temps = list(result[0])
    
    return jsonify(temps)
        


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    #start of autoending session
    with Session(engine) as session:
        
        #making sure that the start and end variable of the endpoint are dates
        start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()
        end_date = dt.datetime.strptime(end, "%Y-%m-%d").date()
        #query to obtain the min, avg and max using the dates as a filter
        result =session.query(func.min(Measurement.tobs), 
                              func.avg(Measurement.tobs), 
                              func.max(Measurement.tobs)).filter(Measurement.date >= start_date)\
                                                         .filter(Measurement.date <= end_date).all()
        temps = list(result[0])
    
    return jsonify(temps)


if __name__ == "__main__":
    app.run(debug=True)