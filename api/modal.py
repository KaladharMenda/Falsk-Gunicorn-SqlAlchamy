import os
import sys
from db import aldb
import datetime
 
    
class Users(aldb.Model):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = aldb.Column(aldb.Integer, nullable=False, primary_key=True)
    phone_no = aldb.Column(aldb.VARCHAR(50), nullable=False)
    firstname = aldb.Column(aldb.VARCHAR(250), nullable=True)
    role = aldb.Column(aldb.VARCHAR(50), nullable=True)
    email = aldb.Column(aldb.VARCHAR(50), nullable=True)
    pin = aldb.Column(aldb.VARCHAR(50), nullable=True)
    created_at = aldb.Column(aldb.DateTime, default=datetime.datetime.now())

