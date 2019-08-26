
import csv
from forms import *
from app import app
from testingPy.test import *
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, flash, redirect,url_for, redirect, request, send_file

@app.route('/')
@app.route('/home')
def home():
    print("You are now on home page")
    return render_template('home.html', title='Welcome Home')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print("Upload page is here")

    if (request.method == 'POST'):
        file = request.files.get('inputFile')
        print("Checking if the file exist")
        if (not file):
            return "No File"
        print("File Exist")

        df = pd.read_csv(file)
        Everything().addEverything(df)

        flash("Database if updated")

    return render_template('upload.html', title="Upload Here")