# import datetime
# import logging
# import os
# from pathlib import Path
#
from server.businessLayer.SystemConfig import SystemConfig
#
#
# class Logger:
#
#     def __init__(self, config: SystemConfig):
#         log_path = self.get_file_path()
#         format = '%(asctime)s -  %(name)s - %(levelname)s - %(message)s'
#         formatter = logging.Formatter(format)
#
#         logging.basicConfig(filename=log_path, filemode='w', level=config.LOGGER_LEVEL, format=format)
#
#     def get_file_path(self):
#         cwd = os.getcwd()
#         path = Path(cwd)
#         parent_path = path
#         # log_path = os.path.join(parent_path, "Logs", str(datetime.date.today()) + '.log')
#         log_path = os.path.join(parent_path, "Logs", '2' + '.log')
#         print(log_path)
#         return log_path
#
#     def debug(self, message):
#         logging.debug(message)
#
#     def warning(self, message):
#         logging.warning(message)
#
#     def error(self, message):
#         logging.error(message)
#
#     def critical(self, message):
#         logging.critical(message)
#

class Logger:

    def __init__(self, config: SystemConfig):
        pass
