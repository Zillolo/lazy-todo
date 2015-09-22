from mongoengine import Document, DateTimeField, EmailField, IntField,  \
    ReferenceField, StringField, ValidationError
import datetime, enum

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
    title = StringField(max_length=150, unique=True, required=True)
    description = StringField(max_length=800, required=True)

    creator = EmailField(max_length=120, required=True)
    assigne = EmailField(max_length=120, required=True)

    created_at = DateTimeField(default=datetime.datetime.now, required=True)

    status = IntField(default=Status.OPEN, required=True)
    priority = IntField(default=Priority.LOW, required=True)

class TaskError(Exception):
    """
    An exception to be used for all error that can occure during handling of tasks.
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

def addTask(title, description, creator, assigne, created_at=None, status=None,
    priority=None):
    """
    Adds a new task to the list.
    """
    task = Task()
    task.title = title
    task.description = description
    task.creator = creator
    task.assigne = assigne

    if created_at is not None:
        task.created_at = created_at
    if status is not None:
        task.status = status
    if priority is not None:
        task.priority = priority

    try:
        logger.debug('A new task will be inserted. (Title: {0})'.format(
            task.title))

        task.save()
    except ValidationError as e:
        logger.exception('An exception has been encountered during the insertion of'
            'a task.')
        raise TaskError('Couldn\'t add your task to the list.')
