import json
import logging
import logging.config
import os


def initLogging(path, key="", fallbackLevel="INFO"):
    """Initialize the logging environment by reading the configuration from a JSON-file.

        Arguments:
            path (str): The path of the JSON configuration file.
            key (str): If the config file contains more structures, specify the key for the logging configuration.
            fallbackLevel (int): The logging level to fallback to, if the config can not be read.
    """

    if os.path.exists(path):
        with open(path, "rt") as file:
            config = json.load(file)

            if key is not None and key != "":
                logging.config.dictConfig(config[key])
            else:
                logging.config.dictConfig(config)
    else:
        # Fallback to basic logging configuration.
        logging.basicConfig(level=fallbackLevel)
        logging.warn(
            "Could not load logging configuration file. Fallback enabled.")


def main():
    """Entry point for the application."""
    initLogging("config.json", key="logging")
    logger = logging.getLogger("default")
