from . import main_BP
from flask import render_template, redirect, url_for
from . import EMULATORS
from .forms import RomsDirectory

@main_BP.route('/')
def home():
    return render_template('home.html')

@main_BP.route('/options')
def options():

    return render_template('options.html', nes=EMULATORS['nes'])

@main_BP.route('/options/emulator/<system>')
def emu_options(system):
    emu = EMULATORS[system]

    return render_template('emu_options.html', emu=emu)

@main_BP.route('/options/emulator/<system>/romdirs', methods=['POST', 'GET'])
def romdirs(system):
    emu = EMULATORS[system]
    form = RomsDirectory()

    if form.validate_on_submit():
        new = form.add_new.data
        emu.add_rom_dir(new)

        return redirect(url_for('main.romdirs', system=emu.name))

    return render_template('romdirs.html', emu=emu, form=form)