from mongoengine import ValidationError
from nose.tools import raises

from app.task import Priority, Task

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
