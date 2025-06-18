from flask import Flask

app = Flask(__name__)


def registration():
    from app import routes


registration()
