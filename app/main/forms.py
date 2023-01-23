from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required

class RomsDirectory(FlaskForm):
    add_new = StringField('Dodaj nowy katalog')
    submit = SubmitField('DODAJ')

class AddEmuMainForm(FlaskForm):
    name = StringField('Podaj Nazwe', validators=[data_required()])
    submit = SubmitField('DODAJ')

class AddEmuForm(FlaskForm):
    system = StringField('Nazwa Systemu Emulacji')
    emulator1 = StringField('Emulator 1')
    emulator2 = StringField('Emulator 2')
    option1 = StringField('Parametry do wywłania Emulatora 1')
    option2 = StringField('Parametry do wywłania Emulatora 2')
    submit = SubmitField('ZAPISZ')

