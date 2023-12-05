from classLibrary.BaseModel import BaseModel
from peewee import *
class Books(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    name = CharField(column_name="name",max_length=100)
    author = CharField(column_name="author",max_length=100)
    description = FloatField(column_name = "description",null=False)
    class Meta:
        table_name = "Books"

    def getName(self):
        return self._name

    def getAuthor(self):
        return self._author

    def getDescription(self):
        return self._description