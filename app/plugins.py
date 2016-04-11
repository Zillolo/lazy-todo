from app import logger
from collections import namedtuple
import json
import os


def loadPlugins(path):

    if path is None or path == "":
        logger.critical("Plugin path is invalid or malformed.")
        raise ValueError("Path is invalid or malformed.")

    if not os.path.exists(path) or not os.path.isdir(path):
        logger.critical("Plugin path does not exist or is not a directory.")
        raise ValueError(
            "Path does not exist or does not point to a directory.")

    # Iterate through all items in the directory and register any plugins
    # found.
    plugins = Plugins()

    for item in os.listdir(path):
        logger.debug("Found directory item: {0}".format(item))
        # Only take action if the item is a directory.
        if os.path.isdir(path + "/" + item):
            # Check if the hooks file exists.
            if os.path.exists(path + "/" + item + "/" + Plugins.HOOKS_FILE):
                logger.debug("A hooks file was found.")
                # Parse the hooks file.
                with open(path + "/" + item + "/" + Plugins.HOOKS_FILE) as file:
                    hooks = json.load(file)

                for hook in hooks["hooks"]:
                    plugins.add(item, hook["name"], hook["description"], hook[
                                "commands"], hook["function"], hook["args"])
                    logger.debug(
                        "Added a hook with name: {0}".format(hook["name"]))
    return plugins


def resolveHook(function):
    if function is None or function == "":
        # NOTE: Possibly return an error handler here.
        return None

    split = function.split(".")
    module = split[0:-1]
    module = "plugins." + ".".join(module)
    function = split[-1]
    logger.debug("Module: {0}, Function: {1}".format(module, function))
    module = __import__(module, fromlist=[function])
    return getattr(module, function)

Hook = namedtuple("Hook", "name description commands function args")


class Plugins:
    HOOKS_FILE = "hooks.json"

    def __init__(self):
        self.__plugins = {}

    def add(self, plugin, name, description, commands, function, args):
        if plugin not in self.__plugins.keys():
            self.__plugins[plugin] = []
        self.__plugins[plugin].append(Hook(
            name, description, commands, function, args))

    def resolve(self, command):
        for hooks in self.__plugins.values():
            for hook in hooks:
                if command in hook.commands:
                    return resolveHook(hook.function)
        return None

    def __len__(self):
        return len(self.__plugins)
