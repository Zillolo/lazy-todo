import json

def exportToFile(tasks, file):
    if tasks is None or len(tasks) == 0:
        logger.info('An export with 0 tasks was requested.')
        raise TaskError('There are no tasks to be exported.')

    if file is None:
        raise TaskError('No valid file was specified.')

    with open(file, 'w') as f:
        for task in tasks:
            #json.dump(task.to_json(), f, ensure_ascii=False)
            f.write(task.to_json())

    #TODO: Fix this.
