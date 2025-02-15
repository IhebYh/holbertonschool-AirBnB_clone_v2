#!/usr/bin/python3
"""flask app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Route /c/<text>"""
    return "C %s" % text.replace("_", " ")


@app.route('/python',
           defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Route /python/<text>"""
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route /number/<int:n>"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route /number_template/<int:n>"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Route /number_odd_or_even/<int:n>"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
