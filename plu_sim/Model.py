from app import db
import pandas as pd
import datetime as dt
from sqlalchemy.exc import *
from exceptions.Exception import *
from sqlalchemy import func, distinct, text
from constants.Constants import *

class PLUSim(db.Model):

    __tablename__ = PLU_SIM_T_NAME 

    plu = db.Column(PLU_SIM_PLU, db.Integer, primary_key=True)
    name = db.Column(PLU_SIM_NAME, db.String(100))

    def __init__(self, plu, name):
        self.plu = plu
        self.name = name

    def __repr__(self):
        return '<PLUSim: {} {}>'.format(self.plu, self.name)

class PLUSimSchema(Schema):
    plu = fields.Integer()
    name = fields.String()

class DatabaseHelper(object):
    
    @staticmethod
    def foo():
        return