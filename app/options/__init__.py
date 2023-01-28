from flask import Blueprint

options_BP = Blueprint('options', __name__, url_prefix='/options')

from . import views
