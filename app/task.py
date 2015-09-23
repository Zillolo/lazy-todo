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
        assignee (str): The email address of the person the Task is assigneed to.
        created_at (datetime): The point in the time when the Task was created.
        status (Status): The current status of the Task.
        priority(Priority): The priority level of the Task.
    """
    title = StringField(max_length=150, unique=True, required=True)
    description = StringField(max_length=800, required=True)

    creator = EmailField(max_length=120, required=True)
    assignee = EmailField(max_length=120, required=True)

    created_at = DateTimeField(default=datetime.datetime.now, required=True)

    status = IntField(default=Status.OPEN, required=True)
    priority = IntField(default=Priority.LOW, required=True)

    def __str__(self):
        """
        Returns a string representation of the Task.
        It is formatted as follows:
        ID: <ID>
        Title: <Title>
        Creator: <Creator>
        Assignee: <assignee>
        Created: <Created>
        Status: <Status>
        Priority: <Priority>

        Description: <Description>
        """
        return ('ID: {7}\nTitle: {0}\nCreator: {2}\nAssignee: {3}\n'
            'Created: {4}\nStatus: {5}\nPriority: {6}\n'
            '\nDescription: {1}\n'.format(self.title,
                self.description, self.creator, self.assignee, self.created_at,
                self.status, self.priority, self.id))

class TaskError(Exception):
    """
    An exception to be used for all errors that can occure during handling of
        tasks.
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

def addTask(title, description, creator, assignee, created_at=None, status=None,
    priority=None):
    """
    Adds a task with the supplied parameters to the collection.

    Args:
        title (str): The title of the Task.
        description (str): A description of the Task.
        creator (str): The email address of the creator.
        assignee (str): The email address of the person the task will be
            assigneed to.
        created_at (datetime): The datetime of creation.
        status (Status): The status of the Task.
        priority (Priority): The priority level of the Task.

    Returns:
        ObjectId: The ObjectId of the newly inserted Task.
    """
    task = Task()
    task.title = title
    task.description = description
    task.creator = creator
    task.assignee = assignee

    # Check whether optional field values have been supplied.
    if created_at is not None:
        task.created_at = created_at
    if status is not None:
        task.status = status
    if priority is not None:
        task.priority = priority

    try:
        logger.debug('A new task will be inserted. (Title: \'{0}\')'.format(
            task.title))

        task.save()
    except ValidationError as e:
        # This can happen if an error occured during insertion, or if the fields
        # of the Task are invalid.
        logger.exception('An exception has been encountered during the '
            'insertion of a task.')
        raise TaskError('Couldn\'t add your task to the list.')

    return task.id

def showByAssigne(assigne):
    try:
        tasks = Task.objects(assigne = assigne).all()
    except ValidationError:
        raise TaskError('The action returned no valid tasks.')

    if tasks is None:
        raise TaskError('The action returned no valid tasks.')

    return tasks

def removeTask(id):
    """
    Removes a task from the list, identified by it's ObjectId.
    """
    try:
        task = Task.objects(id = id).first()
    except ValidationError:
        raise TaskError('The specified task does not exist in the collection.')

    if task is None:
        raise TaskError('The specified task does not exist in the collection.')
    task.delete()
