#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/: displays "Hello HBNB!"
/hbnb: displays "HBNB"
/c/<text>: displays "C " followed by the value of the text variable
/python/<text>: displays "Python ", followed by the value of the text var
The default value of text is "is cool"
/number/<n>: displays "n is a number" only if n is an integer
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


@app.route("/python", strict_slashes=False)
@app.route("/python/(<text>)", strict_slashes=False)
def python_text(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def n_if_only_int(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run()
