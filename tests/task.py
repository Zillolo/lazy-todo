from bson.objectid import ObjectId
from mongoengine import ValidationError
from nose.tools import raises
import datetime

from ..app.task import Priority, Status, Task, TaskError, addTask, \
    fetchByAssignee, removeTaskById

def test_Add_Task():
    # Add a mock task to the collection.
    id = addTask('Mock task', 'I am a mock task!', 'mock@task.com', 'mock@task.com')

    # Query for the just inserted task.
    task = Task.objects(id = id).first()

    assert task is not None

    # Clean up
    task.delete()

@raises(TaskError)
def test_Add_Task_Invalid():
    # Add a task with invalid information to the collection.
    # This should result in a TaskError being thrown.
    addTask(1, 2, 3, 4)

def test_Fetch_By_Assignee():
    # Insert a mock task into the collection.
    task = Task()
    task.title = 'Mock task'
    task.description = 'I am a mock task!'
    task.creator = 'mock@task.com'
    task.assignee = 'mock@task.com'

    task.save()

    # Try fetching the newly inserted task.
    tasks = fetchByAssignee('mock@task.com')

    assert tasks is not None
    if tasks is not None:
        assert len(tasks) == 1

    # Clean up.
    tasks[0].delete()

@raises(TaskError)
def test_Fetch_By_Assignee_Invalid():
    # Fetch without any tasks in the repository.
    tasks = fetchByAssignee('mock@task.com')
    print(tasks)

def test_Remove_Task_By_Id():
    # Insert a mock task into the collection.
    task = Task()
    task.title = 'Mock task'
    task.description = 'I am a mock task!'
    task.creator = 'mock@task.com'
    task.assignee = 'mock@task.com'

    task.save()

    # Remove the task from the repository.
    removeTaskById(task.id)

    # Try to fetch it.
    task = Task.objects(id = task.id).first()
    assert task is None

@raises(TaskError)
def test_Remove_Task_By_Id_Invalid():
    removeTaskById(ObjectId('000000000000000000000000'))

@raises(TaskError)
def test_All():
    # Add a new mock task to the repository.
    id = addTask('Mock task', 'I am a mock task!', 'mock@task.com', 'mock@task.com')

    # Try to fetch it from the repository.
    tasks = fetchByAssignee('mock@task.com')
    assert tasks is not None
    if tasks is not None:
        assert len(tasks) == 1

    # Delete it from the repository.
    removeTaskById(tasks[0].id)

    # Try to fetch it again.
    # This should result in a TaskError.
    tasks = fetchByAssignee('mock@task.com')
