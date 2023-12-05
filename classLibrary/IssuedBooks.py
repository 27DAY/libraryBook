from classLibrary.BaseModel import BaseModel
from peewee import *
class IssuedBooks(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    user = CharField(column_name="user",max_length=100)
    name = CharField(column_name="name",max_length=100)
    date = FloatField(column_name = "date",null=False)
    class Meta:
        table_name = "IssuedBooks"

    def getUser(self):
        return self._user

    def getName(self):
        return self._name

    def getDate(self):
        return self._date