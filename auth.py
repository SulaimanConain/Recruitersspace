import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import RegistrationControls, User
from models import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    try:
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password) and user.email != 'president@sentec.com' and not RegistrationControls.query.one().isRegistration:
            flash('Registrations are Closed')
            return redirect(url_for('auth.login'))

        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)
            return redirect(url_for('main.registrations'))

        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
    except:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    if os.environ['IS_SIGNUP'] == 'True':
        return render_template('signup.html')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    if os.environ['IS_SIGNUP'] == 'True':

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists.')
            return redirect(url_for('auth.signup'))

        new_user = User(email=email, name=name,
                        password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
