from peewee import *

db = SqliteDatabase('Turtle.db')

class Turtle(Model):
    name = CharField()
    
    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Turtle])