from flask import request, jsonify, flash, redirect, url_for, render_template
from flask.views import MethodView
from sqlalchemy import or_

from apps.auth.forms import SignupForm, LoginForm
from models.auth import User


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



class SigninView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template('auth/login.html', form=form, title='Login')

    def post(self):
        form = LoginForm()
        return render_template('auth/login.html', form=form)
