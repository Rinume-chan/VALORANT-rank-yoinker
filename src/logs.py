import logging
from logging.handlers import RotatingFileHandler

class LoggingClass:
    def __init__(self):
        self.logFileOpened = False
        self.logger = logging.getLogger()

        max_bytes = 32 * 1024 * 1024  # 32 MiB
        handler = RotatingFileHandler(filename='yoinker.log', encoding='utf-8', mode='w', maxBytes=max_bytes, backupCount=5)
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname}]: {message}', dt_fmt, style='{')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message: str):
        """We don't really need any extensive logs, so we will just throw everything under INFO"""
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)


Logging = LoggingClass()
