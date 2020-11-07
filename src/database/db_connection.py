import os
import ssl

import pymongo


MONGODB_CONNECTION_STRING_ENV = os.getenv("MONGODB_CONNECTION_STRING_ENV")

client = pymongo.MongoClient(
    f"{MONGODB_CONNECTION_STRING_ENV}",
    ssl=True,
    ssl_cert_reqs=ssl.CERT_NONE,
)

db = client.test_django_db