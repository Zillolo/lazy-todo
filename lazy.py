""" lazy

    Usage:
        lazy (new|n)
        lazy (show|s) [<id>]
        lazy (delete|del|d) <id>

    Options:
    -h, --help  : show this help message
"""

from docopt import docopt

from app.task import TaskError, addTask, removeTaskById, fetchByAssignee

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

def showForCurrentUser():
    try:
        tasks = fetchByAssignee('test@test.com')
        print('===============================================================')
        for task in tasks:
            print(task)
            print('===============================================================')
    except TaskError:
        print('No tasks found.')

def delete(id):
    try:
        removeTaskById(id)
    except TaskError as e:
        print(e)

def main(docopt_args):

    try:
        if docopt_args['new'] or docopt_args['n']:
            new()
        elif docopt_args['show'] or docopt_args['s']:
            if docopt_args['<id>']:
                print('Not currently implemented.')
            else:
                showForCurrentUser()
        elif docopt_args['delete'] or docopt_args['del'] or docopt_args['d']:
            delete(docopt_args['<id>'])
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
