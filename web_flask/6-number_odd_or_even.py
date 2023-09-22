#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/: displays "Hello HBNB!"
/hbnb: displays "HBNB"
/c/<text>: displays "C " followed by the value of the text variable
(and replaces underscore _ symbols with a space )
/python/<text>: displays "Python ", followed by the value of the text var
(and replaces underscore _ symbols with a space )
The default value of text is "is cool"
/number/<n>: displays "n is a number" only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
/number_odd_or_even/<n>: display a HTML page only if n is an integer
and shows whether it is even or odd
"""

from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_n_if_only_int(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def template_int_n_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run()
