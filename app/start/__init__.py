from flask import Blueprint

start_BP = Blueprint('start', __name__, url_prefix='/start')
from . import views
