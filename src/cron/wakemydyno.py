import os

import requests


API_HEROKU_URL_ENV = os.getenv("API_HEROKU_URL_ENV")


def wake_dyno():
    r = requests.get(
        f"https://{API_HEROKU_URL_ENV}"
    )
    return r.json()
