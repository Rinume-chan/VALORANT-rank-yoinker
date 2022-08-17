import pathlib
import logging
from logging.handlers import RotatingFileHandler


class LoggingClass:
    def __init__(self):
        self.logFileOpened = False
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        filename = 'vry.log'

        max_bytes = 10 * 1024 * 1024  # 10 MiB
        handler = RotatingFileHandler(
            filename=filename,
            encoding='utf-8',
            mode='w',
            maxBytes=max_bytes,
            backupCount=10,
            delay=True  # We set delay=True to avoid generating an empty file if we rollover early
        )
        # We do a rollover at the start so new instances start writing in their own files
        # https://stackoverflow.com/questions/44635896/how-to-create-a-new-log-file-every-time-the-application-runs
        if pathlib.Path(filename).is_file():
            handler.doRollover()

        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname}]: {message}', dt_fmt, style='{')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message: str):
        """We don't really need any extensive logs, so we will just throw everything under INFO"""
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message, exc_info=True)


Logging = LoggingClass()
