import pymongo
import ssl

client = pymongo.MongoClient(
    "mongodb+srv://test_django_login:test_django_password@cluster0.1jr2i.mongodb.net/<dbname>?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client.test
print(list(db.list_collections()))
