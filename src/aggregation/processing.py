import os
import sys
from datetime import date

from bson.json_util import dumps, loads

sys.path.append(os.getcwd())
from src.database.db_connection import db

from get_flight import flight_get, flights_all_get


directions = db.static_flight_directions
data = db.test_data


def processing():
    for i in directions.find({}):
        date_parsed = date.today()
        fly_from = i["fly_from"]
        fly_to = i["fly_to"]
        flights = flights_all_get(fly_from, fly_to, None, None)
        flights_all = {
            "date_parsed": f"{date_parsed}",
            "fly_from": f"{fly_from}",
            "fly_to": f"{fly_to}",
            "flights": flights,
        }
        post_id = data.insert_one(flights_all)
        print(post_id.inserted_id)
