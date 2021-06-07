from typing import Optional
from fastapi import FastAPI
import pandas as pd
from src.utils import feature_engineering

app = FastAPI()

data = pd.read_parquet("data/chicago_taxi_trips_2020.parquet")
data = feature_engineering(data)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/total_trips/")
def return_total_trip_of_day(start: str, end: str):
    total_trips = data[["date", "unique_key"]][(data["date"] >= start) & (data["date"] <= end)]\
                .groupby(["date"]).count()\
                .reset_index()\
                .rename({"unique_key": "total_trips"}, axis=1)

    return {"data": total_trips.to_dict('records')}


@app.get("/average_fare_heatmap/")
def get_average_fare_heatmap(date: str):
    fare_heatmap = data[["date", "s2id", "fare"]][(data["date"]==date) & (data['s2id']!=0)]\
                    .groupby(["s2id"]).mean()\
                    .reset_index()

    return {"date": fare_heatmap.to_dict('records')}


@app.get("/average_speed_24hrs/")
def get_average_speed(date: str):
    total_distance_travelled_km = data[["trip_miles"]][data["date"] == date].sum()[0]*1.60934
    total_time_taken_hours = data[["trip_seconds"]][data["date"] == date].sum()[0]/3600
    avg_speed = round(total_distance_travelled_km / total_time_taken_hours, 2)

    return_dict = [{"average_speed": avg_speed}]

    return {"data": return_dict}
