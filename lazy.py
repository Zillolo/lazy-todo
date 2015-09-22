""" lazy

    Usage:
        lazy new
        lazy remove <id>

    Options:
    -h, --help  : show this help message
"""

from docopt import docopt

from app.task import TaskError, addTask, removeTask

def new():
    title = input('Title: ')
    description = input('Description: ')
    creator = input('Creator(Email): ')
    assigne = input('Assigne(Email): ')
    priority = input('Priority(0 = LOW, 1 = MIDDLE, 2 = HIGH): ')

    if priority == "":
        # The priority string is empty, so we take the default value.
        priority = "0"

    try:
        priority = int(priority.strip())
    except ValueError:
        print('Priority must be one of the following values: 0, 1, 2')
        return

    try:
        id = addTask(title, description, creator, assigne, priority=priority)
    except TaskError as e:
        print(e)

    print("Your task has been added with the id {0}".format(id))
def remove(id):
    try:
        removeTask(id)
    except TaskError as e:
        print(e)

def main(docopt_args):

    if docopt_args['new']:
        new()
    elif docopt_args['remove']:
        remove(docopt_args['<id>'])

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
