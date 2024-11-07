from logging.handlers import RotatingFileHandler
import sys


def get_logging_config(app_name: str):
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "main": {
                "format": "%(asctime)s.%(msecs)03d [%(levelname)8s] [%(module)s:%(funcName)s:%(lineno)d] %(message)s",
                "datefmt": "%d.%m.%Y %H:%M:%S%z",
            },
            "errors": {
                "format": "%(asctime)s.%(msecs)03d [%(levelname)8s] [%(module)s:%(funcName)s:%(lineno)d] %(message)s",
                "datefmt": "%d.%m.%Y %H:%M:%S%z",
            },
        },
        "handlers": {
            "stdout": {"class": "logging.StreamHandler", "level": "DEBUG", "formatter": "main", "stream": sys.stdout},
            "stderr": {
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "errors",
                "stream": sys.stderr,
            },
            "file_info": {
                "()": RotatingFileHandler,
                "level": "INFO",
                "formatter": "main",
                "filename": f"logs/{app_name}.log",
                "maxBytes": 5000000,
                "backupCount": 3,
                "encoding": "utf-8",
            },
            "file_debug": {
                "()": RotatingFileHandler,
                "level": "DEBUG",
                "formatter": "main",
                "filename": f"logs/{app_name}_debug.log",
                "maxBytes": 5000000,
                "backupCount": 3,
                "encoding": "utf-8",
            },
        },
        "loggers": {"root": {"level": "DEBUG", "handlers": ["stdout", "stderr", "file_info", "file_debug"]}},
    }
