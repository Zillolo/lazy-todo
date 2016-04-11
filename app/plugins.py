from collections import namedtuple
import json
import os


def loadPlugins(path):

    if path is None or path == "":
        raise ValueError("Path is invalid or malformed.")

    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError(
            "Path does not exist or does not point to a directory.")

    # Iterate through all items in the directory and register any plugins
    # found.
    plugins = Plugins()

    for item in os.listdir(path):
        # Only take action if the item is a directory.
        if os.path.isdir(path):
            # Check if the hooks file exists.
            if os.path.exists(path + Plugins.HOOKS_FILE):
                # Parse the hooks file.
                with open(path + Plugins.HOOKS_FILE) as file:
                    hooks = json.load(file)

                for hook in hooks["hooks"]:
                    plugins.add(hook["name"], hook["description"], hook[
                                "commands"], hook["function"], hook["args"])
    return plugins


def resolveHook(function):
    if function is None or function == "":
        # NOTE: Possibly return an error handler here.
        return None

    module = function.split(".")[0:len(function) - 1]
    function = function.split(".")[-1]
    func = getattr(__import__(module), function)

    return func

Plugin = namedtuple("Plugin", "name description commands function args")


class Plugins:
    HOOKS_FILE = "hooks.py"

    def __init__(self):
        self.__plugins = []

    def add(self, name, description, commands, function, args):
        self.__plugins.append(
            Plugin(name, description, commands, function, args))

    def resolve(self, command):
        for plugin in self.__plugins:
            if command in plugin.commands:
                return resolveHook(plugin.function)
        return None
