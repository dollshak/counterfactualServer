import datetime
import logging


class SystemConfig:
    def __init__(self):
        # LOGGER CONFIG
        self.LOGGER_PATH = ".../Logs/"
        self.LOGGER_LEVEL = logging.DEBUG
        self.MONGO_URI = "mongodb+srv://Shaked:123@counterfactualdb.wejhesh.mongodb.net/?retryWrites=true&w=majority"
        self.DB_NAME = 'counterfactual'