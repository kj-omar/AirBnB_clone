#!/usr/bin/python3
"""Start a Flask web application: drisplay
 states, and states by id"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page: list of states"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Display a HTML page: list of states by id"""
    state_id = None
    for s in storage.all(State).values():
        if s.id == id:
            state_id = s.id
    return render_template('9-states.html', state=state_id)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()
