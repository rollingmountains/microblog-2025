from app import app, db
from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from app.forms import LoginForm
from app.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = db.session.scalars(sa.select(Post)).all()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # when user has already logged in, redirect to index page
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # fetch user object from the database
        user = db.session.scalars(sa.select(User).where(
            User.username == form.username.data)).first()
        # when user doesn't exist or password is incorrect, redirect to login with message
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # when user is valid, set the id in session cookie which again is made available via current_user
        login_user(user, remember=form.remember_me.data)
        # for login requried, extract the page from url's next param
        next_page = request.args.get('next')
        print(next_page)

        if next_page is None or urlsplit(next_page).netloc != '':
            return redirect(url_for('index'))
        return redirect(next_page)
    return render_template('login.html', form=form, title='Sign In')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/about', methods=['GET', 'POST'])
@login_required
def about():
    return render_template('about.html', title='About')
