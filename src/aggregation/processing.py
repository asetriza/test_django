import os
import sys
from datetime import date, datetime

from bson.json_util import dumps, loads

sys.path.append(os.getcwd())
from src.database.db_connection import db

from get_flight import flight_get, flights_all_get


directions = db.static_flight_directions
data = db.test_data


def processing_flghts():
    for i in directions.find({}):
        now = datetime.now()
        time_parsed = now.strftime("%H:%M:%S")
        today_date = date.today()
        date_parsed = str(today_date.strftime("%d/%m/%Y")).replace("-", "/")
        fly_from = i["fly_from"]
        fly_to = i["fly_to"]
        flights = flights_all_get(fly_from, fly_to, None, None)
        flights_all = {
            "date_parsed": f"{date_parsed}",
            "time parsed": f"{time_parsed}",
            "fly_from": f"{fly_from}",
            "fly_to": f"{fly_to}",
            "flights": flights,
        }
        post_id = data.insert_one(flights_all)
        print(post_id.inserted_id)
