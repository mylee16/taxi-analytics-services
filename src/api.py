import yaml
import uvicorn
import pandas as pd
from fastapi import FastAPI

with open("src/config.yaml", "r") as file:
    _CONFIG = yaml.safe_load(file)

data = pd.read_csv(_CONFIG["processed_file_path"])
app = FastAPI()


@app.get("/total_trips/")
def return_total_trip_of_day(start: str, end: str):
    """ Returns total trips per day """
    total_trips = data[["date", "unique_key"]][(data["date"] >= start) & (data["date"] <= end)]\
                    .groupby(["date"]).count()\
                    .reset_index()\
                    .rename({"unique_key": "total_trips"}, axis=1)

    return {"data": total_trips.to_dict('records')}


@app.get("/average_fare_heatmap/")
def get_average_fare_heatmap(date: str):
    """ Returns average fare per pickup location at level 16"""
    fare_heatmap = data[["date", "s2id", "fare"]][(data["date"] == date) & (data['s2id'] != 0)]\
                    .groupby(["s2id"]).mean()\
                    .reset_index()

    return {"data": fare_heatmap.to_dict('records')}


@app.get("/average_speed_24hrs/")
def get_average_speed(date: str):
    """Average speed of trips in km/hr that ended in the past 24 hours from the provided date"""
    total_distance_travelled_km = data[["trip_miles"]][data["date"] == date].sum()[0]*1.60934
    total_time_taken_hours = data[["trip_seconds"]][data["date"] == date].sum()[0]/3600
    avg_speed = round(total_distance_travelled_km / total_time_taken_hours, 2)

    return_dict = [{"average_speed": avg_speed}]
    return {"data": return_dict}


if __name__ == '__main__':
    print("Starting analytics at port", _CONFIG["port"])
    uvicorn.run(app, host=_CONFIG["host"], port=_CONFIG["port"])
