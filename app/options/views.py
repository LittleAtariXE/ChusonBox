from . import options_BP
from flask import render_template
from ..emubox import Emulators
from .forms import AddEmuForm

EMULATORS = Emulators()

@options_BP.route('/home')
def home():
    return render_template('options/home.html')

@options_BP.route('/add_emu', methods=['POST', 'GET'])
def add_emu():
    form = AddEmuForm()
    return render_template('options/add_emu.html', form=form)

