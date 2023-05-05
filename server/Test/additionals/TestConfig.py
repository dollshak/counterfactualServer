import datetime
import logging


class TestConfig:
    def __init__(self):
        # LOGGER CONFIG
        self.LOGGER_PATH = ".../Logs/"
        self.LOGGER_LEVEL = logging.DEBUG
        self.MONGO_URI = "mongodb+srv://Shaked:123@counterfactualdb.wejhesh.mongodb.net/?retryWrites=true&w=majority"
        self.DB_NAME = 'counterfactual'
        self.ALGORITHMS_DIR_PATH_MODULES = 'server.businessLayer.CF_Algorithms.'
        self.ALGORITHMS_DIR_PATH = "..//businessLayer//CF_Algorithms"
