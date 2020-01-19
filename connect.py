from pymongo import MongoClient

class ConnectMongo:

    def __init__(self):
        self.client = MongoClient(port=27017)