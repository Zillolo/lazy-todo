""" lazy

    Usage:
        lazy (new|n)
        lazy (show|s) [<id>]
        lazy (delete|del|d) <id>
        lazy (import|imp) <path>
        lazy (export|exp) <path> [<id>]

    Options:
    -h, --help  : show this help message
"""

from docopt import docopt

from app import config
from app.data import exportToFile
from app.task import Task, TaskError, addTask, removeTaskById, fetchByAssignee

def new():
    title = input('Title: ')
    description = input('Description: ')
    creator = config['User']['email']
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
        tasks = fetchByAssignee(config['User']['email'])
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

def exportTask(path, id):
    task = Task.objects(id = id).first()
    if task is None:
        print('The specified task was not found.')
        return

    exportToFile([task], path)

def exportAll(path):
    tasks = Task.objects(assignee = config['User']['email']).all()
    exportToFile(tasks, path)

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
        elif docopt_args['import'] or docopt_args['imp']:
            print('Not currently implemented.')
        elif docopt_args['export'] or docopt_args['exp']:
            if docopt_args['<id>']:
                exportTask(docopt_args['<path>'],docopt_args['<id>'])
            else:
                exportAll(docopt_args['<path>'])
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
