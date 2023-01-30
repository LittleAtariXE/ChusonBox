from . import main_BP
from flask import render_template, redirect, url_for, request, g
from ..emubox import Emulators
from .forms import AddEmuMainForm, EditEmuForm, RomsDirectoryForm

EMULATORS = Emulators()

@main_BP.route('/')
def start():
    return render_template('start.html')

@main_BP.route('/home')
def home():
    return render_template('home.html')


# @main_BP.route('/options/')
# def options():
#     return render_template('options.html')
#
# @main_BP.route('/options/edit')
# def options_edit():
#     return render_template('options_edit.html', emu=EMULATORS)
#
# @main_BP.route('/options/add', methods=['POST', 'GET'])
# def add_emu():
#     form = AddEmuMainForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         EMULATORS.add_new_emulator(name)
#         return redirect(url_for('main.edit_emu', name=name))
#
#     return render_template('add_emu.html', form=form)
#
# @main_BP.route('/options/edit/<name>', methods=['POST', 'GET'])
# def edit_emu(name):
#     emu = getattr(EMULATORS, name)
#     form = EditEmuForm()
#     if form.validate_on_submit():
#         emu.system = form.system.data
#         emu.emu1 = form.emulator1.data
#         emu.emu2 = form.emulator2.data
#         emu.option1 = form.option1.data
#         emu.option2 = form.option2.data
#         emu.add_ext(form.ext.data)
#         emu.save_emu_config()
#
#         return redirect(url_for('main.edit_emu', name=emu.name))
#
#     return render_template('edit_emu.html', form=form, emu=emu)
#
# @main_BP.route('/start')
# def start():
#     return render_template('start.html', emu=EMULATORS)
#
# @main_BP.route('/start/<name>')
# def start_emu(name):
#     emu = getattr(EMULATORS, name)
#     return render_template('start_emu.html', emu=emu)
#
# @main_BP.route('/start/<name>/option', methods=['POST', 'GET'])
# def start_emu_option(name):
#     emu = getattr(EMULATORS, name)
#     form = RomsDirectoryForm()
#     if form.validate_on_submit():
#         new = form.add_new.data
#         emu.add_rom_dir(new)
#
#         return redirect(url_for('main.start_emu_option', name=emu.name))
#
#
#     return render_template('start_emu_option.html', emu=emu, form=form)
#
# @main_BP.route('/start/<name>/game_list', methods=['POST', 'GET'])
# def start_game(name):
#     emu = getattr(EMULATORS, name)
#
#     if request.method == 'POST':
#         button = request.form.getlist('game')
#         if button[0] == 'roms_scan':
#             emu.scan_dirs()
#             return redirect(url_for('main.start_game', name=emu.name))
#         else:
#             emu.run_game(button[0])
#
#     return render_template('start_game.html', emu=emu)
#


