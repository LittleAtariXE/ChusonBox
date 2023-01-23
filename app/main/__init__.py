from flask import Blueprint
from .emu_config import EmuSystem, make_emulators

emulators = make_emulators()

main_BP = Blueprint('main', __name__)
from . import views
