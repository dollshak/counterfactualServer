import datetime
import logging
import os
from pathlib import Path

from server.Tools.SystemConfig import SystemConfig


class Logger:

    def __init__(self, config: SystemConfig = SystemConfig()):
        self.config = config
        log_path = self.get_file_path()
        self.format = '%(asctime)s -  %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(self.format)
        logging.basicConfig(filename=log_path, filemode='w', level=config.LOGGER_LEVEL, format=self.format)

    def get_file_path(self):
        parent_path = self.config.LOGGER_PATH
        log_path = os.path.join(parent_path, str(datetime.date.today()) + '.log')
        # print(log_path)
        return log_path

    def debug(self, message):
        logging.debug(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)
