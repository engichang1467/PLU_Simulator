# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import os
import logging
from config import Config
from flask_cors import CORS
from sqlalchemy import event
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler
from flask import Flask, render_template, request

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=OFF") # PRAGMA foreign_keys=OFF
    cursor.close()

from routes import *
from plu_sim import bp as pluSim_bp, Model as pluSimModel

app.register_blueprint(pluSim_bp)

db.create_all()
db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'PLUSim': pluSimModel.PLUSim}



# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()
