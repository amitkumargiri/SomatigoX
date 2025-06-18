from pymongo import MongoClient

"""
This is MongoConnector class implemented as Singleton pattern.

Author: Amit Kumar Giri (allyamit@gmail.com)
"""
class MongodbConnector:

    _instance = None  # Class-level singleton reference

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MongodbConnector, cls).__new__(cls)
        return cls._instance

    def __init__(self, uri="mongodb://localhost:27017/", db_name="test"):
        if not hasattr(self, "_initialized"):
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self._initialized = True  # Avoid reinitialization

    def get_db(self):
        return self.db
