from flask_mongoengine import MongoEngine
from mongoengine import Document, DictField, IntField

db = MongoEngine()


class BuildingKind(Document):
    int_id = IntField()


class EntityChange(Document):
    old_data = DictField()
    new_data = DictField()
