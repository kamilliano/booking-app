from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Bookings import db

#TODO 
connection_string= r'mysql://sqlalchemy:sn@pp333!wow@127.0.0.1:3306'

db = SQLAlchemy()


try:
    engine = db.create_engine(connection_string) # connect to server
    engine.execute("CREATE DATABASE test1234") #create db
    engine.execute("USE test1234") # select new db
except:
    pass
