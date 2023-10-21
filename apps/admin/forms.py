from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddBusinessForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])