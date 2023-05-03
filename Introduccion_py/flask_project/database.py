# from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
import certifi

MONGODB_URI = 'mongodb+srv://gnuxdar:Jowrowa585H0jr71@clusterac.bqbulz0.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()


def dbConnection():
    try:
        # Create a new client and connect to the server
        client = MongoClient(MONGODB_URI, tlsCAFile=ca)
        db = client['db_products']
        # client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
    except ConnectionError:
        print('Error de conexion con la DB')
    return db
