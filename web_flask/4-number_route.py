#!/usr/bin/python3
"""flask web app"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """home page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays text variable"""
    text_var = text.replace('_', ' ')
    return 'C {}'.format(text_var)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def pyhton_text(text='is cool'):
    """displays text variable"""
    text_var = text.replace('_', ' ')
    return 'Python {}'.format(text_var)


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """displays a number"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
