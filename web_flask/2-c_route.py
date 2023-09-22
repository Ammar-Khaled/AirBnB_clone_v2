#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/: displays "Hello HBNB!"
/hbnb: displays "HBNB"
/c/<text>: displays "C " followed by the value of the text variable
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run()
