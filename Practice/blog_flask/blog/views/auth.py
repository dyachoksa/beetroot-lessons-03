from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

from blog.extensions import db
from blog.forms import RegistrationForm, LoginForm
from blog.models import User
from blog.tasks import send_welcome_email

auth = Blueprint("auth", __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            return render_template('auth/register.html', form=form, error="User already exists")

        user = User(name=form.name.data, email=form.email.data)
        user.hash_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        send_welcome_email.delay(user.id)

        flash('Registration has been successful. Now you can login.', 'success')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return render_template('auth/register.html', form=form, error="Incorrect credentials")

        if not user.verify_password(form.password.data):
            return render_template('auth/register.html', form=form, error="Incorrect credentials")

        login_user(user)

        flash('Logged in successfully.', 'success')

        return redirect(url_for('pages.index'))

    return render_template('auth/login.html', form=form)


@auth.get('/logout')
@login_required
def logout():
    logout_user()

    flash('Logged out. See you soon!', 'success')

    return redirect(url_for('pages.index'))
