from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required

class AddEmuForm(FlaskForm):
    name = StringField('Podaj nazwę', validators=[data_required()])
    submit = SubmitField('Dodaj')

