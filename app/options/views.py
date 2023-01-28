from . import options_BP
from flask import render_template

@options_BP.route('/home')
def home():
    return render_template('options/home.html')

