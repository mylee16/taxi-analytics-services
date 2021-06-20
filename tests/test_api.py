from fastapi.testclient import TestClient
import pandas as pd
from src.api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_return_total_trip_of_day():
    response = client.get("/total_trips/?start=2020-01-01&end=2020-01-01")
    assert response.status_code == 200
    assert response.json() == {"data": [{"date": "2020-01-01", "total_trips": 20798}]}


def test_return_average_fare_heatmap():
    response = client.get("/average_fare_heatmap/?date=2020-01-01")
    result = response.json()
    heatmap_dict = dict()
    for sub in result["data"]:
        print(sub)
        heatmap_dict[str(sub["s2id"])] = sub["fare"]

    assert response.status_code == 200
    assert heatmap_dict["9803813108609712128"] == 43.79


def test_return_average_speed_24hrs():
    response = client.get("/average_speed_24hrs/?date=2020-01-01")

    assert response.status_code == 200
    assert response.json() == {"data": [{"average_speed": 27.62}]}
