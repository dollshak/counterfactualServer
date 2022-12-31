import datetime
import logging
import BussinessLayer.SystemConfig as SystemConfig
import os
from pathlib import Path


class Logger:

    def __init__(self, config: SystemConfig):
        log_path = self.get_file_path()
        format = '%(asctime)s -  %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format)

        logging.basicConfig(filename=log_path, filemode='w', level=config.LOGGER_LEVEL, format=format)
        #
        # logging = logging.getLogger(__name__)
        # logging.setLevel(config.LOGGER_LEVEL)
        # handler = logging.FileHandler(log_path)
        # handler.setLevel(config.LOGGER_LEVEL)
        # handler.setFormatter(formatter)
        #
        # logging.addHandler(handler)

    def get_file_path(self):
        cwd = os.getcwd()
        path = Path(cwd)
        parent_path = path
        # log_path = os.path.join(parent_path, "Logs", str(datetime.date.today()) + '.log')
        log_path = os.path.join(parent_path, "Logs", '2' + '.log')
        print(log_path)
        return log_path

    def debug(self, message):
        logging.debug(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)