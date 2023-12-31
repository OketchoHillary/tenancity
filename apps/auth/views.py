import flask
from flask import request, jsonify, flash, redirect, url_for, render_template
from flask.views import MethodView
from flask_login import login_required, logout_user, login_user
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import or_
from decouple import config as env

from apps.auth.forms import SignupForm, LoginForm
from models.auth import User
from models.core import Business, BusinessAdmins
from utils import mail


class SignupView(MethodView):
    def get(self):
        form = SignupForm()
        return render_template('auth/register.html', form=form, title='Register')

    def post(self):
        form = SignupForm()
        if form.validate_on_submit():
            if form.password.data == form.confirm.data:
                existing_user = User.query.filter(or_(User.email == form.email.data, User.contact == form.contact.data)
                                                  ).first()
                if existing_user is None:
                    print('ye')
                    user = User(
                        contact=form.contact.data,
                        email=form.email.data,
                        password=form.password.data
                    )
                    user.save()
                    # Generate an activation token
                    SECRET_KEY = env('SECRET_KEY')
                    serializer = URLSafeTimedSerializer(SECRET_KEY)
                    token = serializer.dumps(user.email, salt='email-confirmation')
                    activation_link = url_for('auth.activate', token=token, _external=True)
                    send_activation_email(user.email, activation_link)
                    flash('Registered successfully', 'success')
                    return redirect(url_for('auth.login'))
                else:
                    print('mop')
                    flash('User already exist', 'error')
                    return redirect(url_for('auth.signup'))
            else:
                print('yeah')
                flash('Passwords do not match', 'error')
                return redirect(url_for('auth.signup'))


# Route for activating the user account
def activate(token):
    SECRET_KEY = env('SECRET_KEY')
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(token, salt='email-confirmation', max_age=3600)  # Token expiration time (1 hour)
        # user = next((user for user in users_db.values() if user['email'] == email), None)
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_active = True
            user.email_confirmed = True
            user.save()
            return redirect(url_for('auth.login'))
        else:
            return 'Invalid activation link.'
    except Exception as e:
        print('mememe')
        print(str(e))
        return 'Invalid or expired activation link.'


# Function to send activation email
def send_activation_email(email, activation_link):
    subject = 'Activate Your Account'
    body = f'Click on the following link to activate your account: {activation_link}'
    # send_email(subject, sender, recipients, text_body, html_body)
    message = Message(subject, recipients=[email], body=body)
    mail.send(message)


class SigninView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('auth/login.html', form=form, title='Login')

    def post(self):
        form = LoginForm()
        # pk = request.args.get('pk')
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            print(form.password.data)
            if user and user.check_password(password=form.password.data):
                login_user(user, remember=True)
                next_page = request.args.get('next')
                # business = BusinessAdmins.query.filter_by(user_id=user.id, is_current=True).first()
                return redirect(next_page or url_for('core.dashboard'))
                # return redirect(next_page or url_for('core.dashboard', pk=business.id))
            else:
                print('meee')
                flash('Invalid username/password combination', 'error')
        return redirect(url_for('auth.login'))


@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))
