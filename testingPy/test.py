import os
from app import db
from plu_sim.Model import *


class Everything(object):

    @staticmethod
    def addEverything(file):
        DatabaseHelper().addAllCSV(file)
        print("Database bas been updated")

    @staticmethod
    def clear():
        clear = os.system('clear')


'''
from testingPy.test import *
'''