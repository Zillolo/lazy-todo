import json

def exportToFile(tasks, file):
    if tasks is None or len(tasks) == 0:
        logger.info('An export with 0 tasks was requested.')
        raise TaskError('There are no tasks to be exported.')

    if file is None:
        raise TaskError('No valid file was specified.')

    with open(file, 'w') as f:
        for task in tasks:
            f.write(task.to_json())

    #TODO: Fix this. Wtf did I mean here?

def importFromFile(file):
    if file is None or file == "":
        logger.info('Can not import from invalid file: {0}'.format(file))
        raise TaskError('There are no tasks to be imported.')

    with open(file) as f:
        tasks = json.load(f)

    for task in tasks:
        t = Task()
        t['_id'] = task['_id']
        t['title'] = task['title']
        t['description'] = task['description']
        t['creator'] = task['creator']
        t['assignee'] = task['assignee']
        t['created_at'] = task['created_at']
        t['status'] = task['status']
        t['priority'] = task['priority']

        addTask(id = task['_id'], title = task['title'],
            description = task['description'], creator = task['creator'])

        logger.debug('Task: {0}'.format(task))

        t.save()
