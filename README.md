# Gojek Software Engineering - Big Data and Maching Learning (Data Science Platform Team) Interview

Author: Mengyong Lee | [LinkedIn](https://www.linkedin.com/in/mylee1/) | [Github](https://github.com/mylee16)

In this assignment, we aim to build a Web Service that provides basic analytics over [Chicago Taxi Trips dataset](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew). The dataset includes taxi trips in Chicago for the year 2020.


<p align="center">
  <img src="img/Gojek-Logo-Horizontal.jpeg" width=50%/>
  <br>                  
</p>

## Table of contents
1. [Introduction](#introduction)
1. [Usage](#usage)


## Introduction
The API is based on [fastapi](https://fastapi.tiangolo.com/). The code is in python 3.6.7 and is dockerised. The API provides 3 functionalities:
1. Total Trips per Day - Returns the total number of trips in the date range provided
`curl http://localhost:8080/average_speed_24hrs\?date\=2020-01-02`
1. Fare Heatmap - The average fare per pick up location [S2 ID](http://s2geometry.io/) at level 16 for the given date, based on the pickup time of the trip.
``
1. Average speed of trips (km/h) that ended in the past 24 hours from the provided date.
``


## Usage
1. To build the docker environment:
```docker-compose -f docker-compose.yml build```
2. To run the api service:
```docker-compose -f docker-compose.yml up```

 Configuration files for src/api and src/pipeline can be found in [src/config](/src/config). 
