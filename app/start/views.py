from . import start_BP
from flask import render_template

@start_BP.route('/home')
def home():
    return render_template('start/home.html')
