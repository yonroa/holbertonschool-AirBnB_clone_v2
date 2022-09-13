#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print the text HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Print an specified text after the letter C"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    """Print an specified text after the word python"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def num_print(n):
    """Print if n is int"""
    if type(n) is int:
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """Render a HTML template if n is int"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
