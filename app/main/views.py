from . import main_BP
from flask import render_template, redirect, url_for, request
from . import emulators
from .forms import RomsDirectory

@main_BP.route('/')
def home():
    nes = emulators['nes']

    return render_template('home.html', nes=nes)


@main_BP.route('/options/')
def options():
    return render_template('options.html')

@main_BP.route('/options/add', methods=['POST', 'GET'])
def add_emu():
    return render_template('add_emu.html')

