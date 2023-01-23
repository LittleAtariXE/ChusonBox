from flask import Blueprint
from .emu_config import EmuSystem, Emulators



main_BP = Blueprint('main', __name__)
from . import views
