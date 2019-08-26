from app import db
import pandas as pd
import datetime as dt
from sqlalchemy.exc import *
from constants.Constants import *
from exceptions.Exception import *
from sqlalchemy import func, distinct, text

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
    def getPLUs():
        return PLUSim.query.all()

    @staticmethod
    def getPLU(search):
        return PLUSim.query.get(int(search))

    @staticmethod
    def convertArr(a, column):
        l = []
        if (column == "plu"):
            for i in a:
                l.append(i.plu)
        elif (column == "name"):
            for i in a:
                l.append(i.name)
        return l
    
    @staticmethod
    def addAllCSV(file):
        plu = file['plu']
        name = file['name']
        for i in range(len(plu)):
            e = PLUSim.query.get(int(plu[i]))
            if (e == None):
                a = PLUSim(plu=int(plu[i]), name=str(name[i]))
                db.session.add(a)
        db.session.commit()
    
    @staticmethod
    def removePLU(search):
        a = PLUSim.query.get(int(search))
        db.session.delete(a)
        db.session.commit()

    @staticmethod
    def deleteEverything():
        a = PLUSim.query.all()
        for i in a:
            db.session.delete(i)
        db.session.commit()