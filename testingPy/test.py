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
            clear = os.system('clr')
            clear2 = os.system('clear')
            return clear or clear2


'''
from testingPy.test import *
'''