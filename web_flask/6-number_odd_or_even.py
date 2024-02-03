#!/usr/bin/python3
'''a script that starts a Flask web application'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''function display display “Hello HBNB!”'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''function display display “HBNB”'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''function display a text'''
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def is_cool(text):
    '''display Python followed by the value of the text variable'''
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    '''display “n is a number” only if n is an integer'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''display a HTML page only if n is an integer'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def check_number(n):
    '''isplay a HTML page only if n is an integer'''
    result = 'even' if n % 2 == 0 else 'odd'

    data = {
        'number': n,
        'result': result
    }
    return render_template('6-number_odd_or_even.html', **data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
