from . import main_BP
from flask import render_template, redirect, url_for, request
from . import Emulators
from .forms import AddEmuMainForm

EMULATORS = Emulators()

@main_BP.route('/')
def home():


    return render_template('home.html')

@main_BP.route('/options/')
def options():
    return render_template('options.html')

@main_BP.route('/options/add', methods=['POST', 'GET'])
def add_emu():
    form = AddEmuMainForm()
    if form.validate_on_submit():
        name = form.name.data
        EMULATORS.add_new_emulator(name)
        return redirect(url_for('main.options'))

    return render_template('add_emu.html', form=form)

