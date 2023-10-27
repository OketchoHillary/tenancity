from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[DataRequired()])


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    contact = StringField('Contact', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(message='Enter a valid email.'), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,
                                                                            message='Select a stronger password.')])
    confirm = PasswordField('Confirm Your Password', validators=[DataRequired(),
                                                                 EqualTo('password',
                                                                         message='Passwords must match.')])


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])