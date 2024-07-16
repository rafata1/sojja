from pymongo import MongoClient

from config import config


def get_connection_string():
    return f"mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_HOST}:{config.MONGO_PORT}"


class MongoDB:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
            cls._client = MongoClient(get_connection_string())
        return cls._instance

    def get_db(self):
        return self._client[config.MONGO_DB_NAME]

    def get_client(self):
        return self._client
