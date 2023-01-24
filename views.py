from flask import g, request, redirect, url_for
from run import app


@app.before_request
def back():
    g.back = request.referrer

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('main.home'))