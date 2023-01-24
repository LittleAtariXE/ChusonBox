from . import main_BP
from flask import render_template, redirect, url_for, request, g
from . import Emulators
from .forms import AddEmuMainForm, EditEmuForm

EMULATORS = Emulators()

@main_BP.route('/')
def home():


    return render_template('home.html')

@main_BP.route('/options/')
def options():
    return render_template('options.html')

@main_BP.route('/options/edit')
def options_edit():
    return render_template('options_edit.html', emu=EMULATORS)

@main_BP.route('/options/add', methods=['POST', 'GET'])
def add_emu():
    form = AddEmuMainForm()
    if form.validate_on_submit():
        name = form.name.data
        EMULATORS.add_new_emulator(name)
        return redirect(url_for('main.edit_emu', name=name))

    return render_template('add_emu.html', form=form)

@main_BP.route('/options/edit/<name>', methods=['POST', 'GET'])
def edit_emu(name):
    emu = getattr(EMULATORS, name)
    form = EditEmuForm()
    if form.validate_on_submit():
        emu.system = form.system.data
        emu.emu1 = form.emulator1.data
        emu.emu2 = form.emulator2.data
        emu.option1 = form.option1.data
        emu.option2 = form.option2.data
        emu.add_ext(form.ext.data)
        emu.save_emu_config()

        return redirect(url_for('main.edit_emu', name=emu.name))

    return render_template('edit_emu.html', form=form, emu=emu)

