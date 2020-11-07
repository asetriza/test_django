import os

import requests


API_SKYPIDCKER_URL_ENV = os.getenv("API_SKYPIDCKER_URL_ENV")
API_BOOKING_URL_ENV = os.getenv("API_BOOKING_URL_ENV")


def skypidcker_get(url_params):
    headers = {"Content-Type": "application/json"}
    r = requests.get(
        f"https://{API_SKYPIDCKER_URL_ENV}/{url_params}&partner=picky", headers=headers
    )

    return r.json()


def booking_get(url_params):
    r = requests.get(f"https://{API_BOOKING_URL_ENV}/api/v0.1/{url_params}")

    return r.json()
