from app import app
from flask import render_template


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
        },
        {
            'author': {'username': 'will'},
            'post': 'Live life the fullest'
        },
        {
            'author': {'username': 'linda'},
            'post': 'Life is a one jolly bus ride'
        }
    ]

    return render_template('index.html', user=user, posts=posts)
