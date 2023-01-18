from flask import Blueprint
from .config_emu import emulators

EMULATORS = emulators

main_BP = Blueprint('main', __name__)
from . import views
