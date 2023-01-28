from flask import Blueprint




main_BP = Blueprint('main', __name__)
from . import views
