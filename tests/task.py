from bson.objectid import ObjectId
from mongoengine import ValidationError
from nose.tools import raises
import datetime

from app.task import Priority, Status, Task, TaskError, addTask, removeTask

def test_Set_Title_String():
    task = Task()

    task.title = "Hello"
    assert task.title == "Hello"

@raises(ValidationError)
def test_Set_Title_Int():
    task = Task()

    task.title = 1

    # Should throw ValidationError, since title field is not a String.
    task.save()

def test_Set_Priority_High():
    task = Task()
    assert task.priority == Priority.LOW

    task.priority = Priority.HIGH
    assert task.priority == Priority.HIGH

def test_Add_Task_Full():
    addTask('Title', 'Description', 'email@email.com', 'email@email.com',
        status = Status.CLOSED, created_at = datetime.datetime.now,
        priority = Priority.MIDDLE)

    # Retrieve the just inserted document
    task = Task.objects(title = 'Title').first()
    assert Task is not None

    # Remove the inserted task
    task.delete()

@raises(TaskError)
def test_Add_Task_Title_Int():
    addTask(1, '', 'email@email.com', 'email@email.com')

def test_Remove_Task():
    task = Task()
    task.title = 'Title'
    task.description = ''
    task.creator = 'email@email.com'
    task.assigne = 'email@email.com'

    task.save()

    removeTask(task.id)
    task = Task.objects(id = task.id).first()
    assert task is None

@raises(TaskError)
def test_Remove_Task_Wrong_Id():
    removeTask(ObjectId('000000000000000000000000'))
