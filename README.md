# Gojek Software Engineering - Big Data and Maching Learning (Data Science Platform Team) Interview

<p align="center">
  <img src="img/Gojek-Logo-Horizontal.jpeg" width=50%/>
  <br>                  
</p>


Author: Mengyong Lee | [LinkedIn](https://www.linkedin.com/in/mylee1/) | [Github](https://github.com/mylee16)

In this assignment, we aim to build a Web Service that provides basic analytics over [Chicago Taxi Trips dataset](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew). The dataset includes taxi trips in Chicago for the year 2020.


## Table of contents
1. [Introduction](#introduction)
1. [Usage](#usage)
1. [Design](#design)
1. [References](#references)


## Introduction
The API is based on [fastapi](https://fastapi.tiangolo.com/). The code is in python 3.6.7 and is dockerised using docker-compose. The API provides 3 functionalities:

1. Total Trips per Day - Returns the total number of trips in the date range provided.
```curl http://localhost:8080/total_trips?start=2020-01-01&end=2020-01-31```
1. Fare Heatmap - The average fare per pick up location [S2 ID](http://s2geometry.io/) at level 16 for the given date, based on the pickup time of the trip.
```curl http://localhost:8080/average_fare_heatmap/?date=2020-01-01```
1. Average speed of trips (km/h) that ended in the past 24 hours from the provided date.
```curl http://localhost:8080/average_speed_24hrs/?date=2020-01-01```

## Usage
1. To build the docker environment:
run ```bin/setup```
2. To run the api service:
run ```bin/run```

 Configuration files for src/api and src/pipeline can be found in [src/config](/src/config). 

## Design
This project consist of two main components, `src/api.py` and `src/pipeline.py`. The project is then dockerised and packages executables in `bin/run` and `bin/setup`. 

1. `src/pipeline.py`

`src/pipeline` takes in the url of the parquet file, and output a preprocessed csv file. `src/pipeline` consist of a few components, namely 1. data_downloader, 2. feature_engineering. data_downloader downloads the parquet data using gdown package into /data directory. feature_engineering reads in a pandas dataframe, creates `date` and `s2id` features, and remove other unnecessary columns. The processed output is saved under `data/processed_data.csv`.


2. `src/api.py`

`src/api.py` uses FastAPI to serve. FastAPI is chosen as it provides good documentation via swagger. Documentation can be access through `http://localhost:8080/docs`.
There are 3 GET functionalities, 1. total_trips, 2. average_fare_heatmap, and 3.average_speed_24hrs. `src/api.py` reads in a preprocessed CSV in order to reduce memory consumption and to speed up serving. Data manupulation are done in Pandas framework.

3. `bin/setup`

The project is dockerised using docker-compose. First, pytest is run to check for code coverage. Next, the dockerfile is executed, including installing python packages and build the container.  


4. `bin/run`

`bin/run` runs the docker container and start the API service. Port and host can be configured in `src/config.yaml`


## References
- [Chicago Taxi Trips dataset](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew)
- [s2geometry](http://s2geometry.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
