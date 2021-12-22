from mongoengine.fields import EmailField, EmbeddedDocumentField, StringField
from mongoengine_goodjson import Document
from mongoengine_goodjson.document import EmbeddedDocument


class Location(EmbeddedDocument):
    province = StringField()
    district = StringField()
    town = StringField()


class Users(Document):
    full_name = StringField(required=True, min_length=3, max_length=30)
    email = EmailField(requred=True)
    address = EmbeddedDocumentField(Location)
