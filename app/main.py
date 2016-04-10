"""lazy

    Usage:
        lazy (new|n)
        lazy (show|s) [<id>]
        lazy (delete|d) [<id>]
        lazy (import|i) <path>
        lazy (export|e) <path> [<id>]

    Options:
    -h, --help: Show this help message.
"""

from docopt import docopt


def main():
    # Parse commandline arguments.
    args = docopt(__doc__)

    if args['new'] or args['n']:
        # Insert a new task.
        pass
    elif args['show'] or args['s']:
        if args['<id>']:
            # Show the task whose ID most closely matches the given ID.
            pass
        else:
            # Show all tasks for the current user.
            pass
    elif args['delete'] or args['d']:
        if args['<id>']:
            # Delete the task with the ID that most closely matches the given
            # ID.
            pass
        else:
            # Prompt the user to input the ID of the task to delete.
            # Then delete the task with the ID that matches the given one best.
            pass
    elif args['import'] or args['i']:
        # Check if the given path exists and if so, import from it.
        pass
    elif args['export'] or args['e']:
        # Check if it is possible to write to the given path.
        if args['<id>']:
            # Write only the task with the ID that matches the given one best.
            pass
        else:
            # Write all tasks the current user has to the file.
            pass
