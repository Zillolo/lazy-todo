from app import logger
from app.plugins import loadPlugins

import logging
import sys


def initLogging():
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("user.log")
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s [%(levelname)s] - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)


def main():
    initLogging()
    logger.info("Logging initialized.")

    plugins = loadPlugins("plugins")
    logger.info("{0} plugins loaded.".format(len(plugins)))

    func = plugins.resolve(sys.argv[1])
    func()
