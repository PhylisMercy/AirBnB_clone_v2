#!/usr/bin/python3
"""
script that starts a Flask web application:
Routes:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ” followed by the value of the text variable
  (replace underscore _ symbols with a space )
* /python/(<text>): display “Python ”, followed by the value of the
  text variable (replace underscore _ symbols with a space )
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Print a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb/', strict_slashes=False)
def display_HBNB():
    """
    Print a string
    """
    return 'HBNB'


@app.route('/c/<text>/', strict_slashes=False)
def C_is_fun(text):
    """
    Print a string
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def Python_is_cool(text="is cool"):
    """
    Print a string
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>/', strict_slashes=False)
def is_a_number(n):
    """
    Print a string
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>/', strict_slashes=False)
def is_a_number_template(n):
    """
    Template html
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def odd_or_even(n):
    """
    Template html: odd or even
    """
    if n % 2:
        val = 'odd'
    else:
        val = 'even'
    return render_template('6-number_odd_or_even.html', number=n, odd_even=val)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
