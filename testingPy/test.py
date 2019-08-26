from app import db
from plu_sim.Model import *


class Everything(object):

    @staticmethod
    def addEverything(file):
        DatabaseHelper().addAllCSV(file)
        print("Database bas been updated")


'''
from testingPy.test import *
'''