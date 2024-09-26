from peewee import MySQLDataBase

#Local
db = MySQLDataBase(
    'db-crud',
    user='root',
    password="",
    host="localhost",
    port=3306
)