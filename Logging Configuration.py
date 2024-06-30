import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    @staticmethod
    def log(message, level=logging.INFO):
        logging.log(level, message)

    @staticmethod
    def debug(message):
        Logger.log(message, logging.DEBUG)

    @staticmethod
    def info(message):
        Logger.log(message, logging.INFO)

    @staticmethod
    def warning(message):
        Logger.log(message, logging.WARNING)

    @staticmethod
    def error(message):
        Logger.log(message, logging.ERROR)

    @staticmethod
    def critical(message):
        Logger.log(message, logging.CRITICAL)
