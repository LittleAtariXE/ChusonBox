from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RomsDirectory(FlaskForm):
    add_new = StringField('Dodaj nowy katalog')
    submit = SubmitField('DODAJ')

