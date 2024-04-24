#!/usr/bin/python3
"""Script that runs a Flask web application"""

from flask import Flask, render_template
from models.city import City
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def Cities():
    """ list of City objects linked to the State sorted by name"""
    state = storage.all("State").value
    return render_template('8-cities_by_states.html', state=state)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000')
