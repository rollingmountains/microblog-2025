from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sunshine'}
    posts = [
        {
            'author': {'username': 'john'},
            'post': 'This is a beautiful day'
        },
        {
            'author': {'username': 'susan'},
            'post': 'Life is a beautiful ride'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'User {form.username.data} is succesfully logged in and {form.remember_me.data}.')
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Sign In')
