from mongoengine import Document, DateTimeField, EmailField, IntField,  \
    ReferenceField, StringField, ValidationError
import datetime, enum, Exception

from app import logger

class Priority(enum.IntEnum):
    """
    This defines the priority levels a Task can have.
    """
    LOW = 0,
    MIDDLE = 1,
    HIGH = 2

class Status(enum.IntEnum):
    """
    This defines statuses a Task can have.
    """
    OPEN = 0
    IN_PROGRESS = 1
    CLOSED = 2

class Task(Document):
    """
    This defines the basic model for a Task as we want it to be stored in the
        MongoDB.

        title (str): The title of the Task.
        description (str): A description of the Task.
        creator (str): The task creators email address.
        assigne (str): The email address of the person the Task is assigned to.
        created_at (datetime): The point in the time when the Task was created.
        status (Status): The current status of the Task.
        priority(Priority): The priority level of the Task.
    """
    title = StringField(max_length=150, required=True)
    description = StringField(max_length=800, required=True)

    creator = EmailField(max_length=120, required=True)
    assigne = EmailField(max_length=120, required=True)

    created_at = DateTimeField(default=datetime.datetime.now, required=True)

    status = IntField(default=Status.OPEN, required=True)
    priority = IntField(default=Priority.LOW, required=True)
