# SQLAlchemy Challenge 

Welcome to the SQLAlchemy Challenge repository! This project is designed to analyze and explore climate data for Honolulu, Hawaii, to assist in planning a holiday vacation. The analysis is performed using Python, SQLAlchemy ORM, Pandas, and Matplotlib.

## Files

- **climate_starter.ipynb**: Jupyter Notebook containing the climate analysis and data exploration.
- **app.py**: Flask application that provides a REST API to access the climate data.
- **Resources/hawaii.sqlite**: SQLite database containing the climate data.
- **Output/**: This folder contains the png images of the notebook analysis

## Usage

### Accessing the API Routes

- **Home Page**: Lists all available routes. 
    ```
    /
    ```
- **Precipitation**: Returns JSON data of precipitation for the last 12 months. 
    ```
    /api/v1.0/precipitation 
    ```
- **Stations**: Returns JSON data of station details. 
    ```
    /api/v1.0/stations 
    ```
- **Temperature Observations (TOBS)**: Returns JSON data of temperature observations for the last year from the most active station. 
    ```
    /api/v1.0/tobs
    ```
- **Temperature Statistics**:
- For a given start date:
    ```
    /api/v1.0/<start>
    ```
- For a given start and end date:
    ```
    /api/v1.0/<start>/<end>
    ```
### Jupyter Notebook

Open the `climate_starter.ipynb` notebook in Jupyter to perform detailed climate analysis and data exploration

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

