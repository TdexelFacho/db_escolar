from peewee import Model, AutoField, CharField, ForeignKeyField
from basedato.db import db

class curso(Model):
    id = AutoField()
    nombre = CharField(unique=True)
    descripcion = CharField()
    DNI = CharField()
    Email = CharField()
    Telefono = CharField()
    Fech_nacimiento = CharField()
    curso = ForeignKeyField(curso)


    class Meta:
        database = db
        table_name = 'cursos'