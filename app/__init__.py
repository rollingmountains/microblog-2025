from flask import Flask

app = Flask(__name__)
print(app)

print(__name__)


def registration():
    from app import routes


registration()
