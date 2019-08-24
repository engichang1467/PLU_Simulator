from flask import Blueprint, request, Flask

bp = Blueprint('plu_sim', __name__)

from plu_sim import Controller, Model