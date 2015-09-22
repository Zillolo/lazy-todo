from mongoengine import Document, DateTimeField, EmailField, IntField,  \
    ReferenceField, StringField
import datetime, enum

class Priority(enum.IntEnum):
    LOW = 0,
    MIDDLE = 1,
    HIGH = 2

"""
This defines the basic model for a Task as we want it to be stored in the
    MongoDB.
"""
class Task(Document):
    title = StringField(max_length=150, required=True)
    description = StringField(max_length=800, required=True)

    creator = EmailField(max_length=120, required=True)
    assigne = EmailField(max_length=120, required=True)

    created_at = DateTimeField(default=datetime.datetime.now, required=True)

    status = IntField(default=0, required=True)
    priority = IntField(default=Priority.LOW, required=True)
