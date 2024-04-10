#!/usr/bin/python3
"""Start a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates')


def load_states():
    return sorted(storage.all(State).values(), key=lambda x: x.name)


@app.teardown_appcontext
def remove_current_session(exception):
    """Close the SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Get the list of all states"""
    states = load_states()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id_found(id):
    """Get the list of cities related to the state id"""
    states = load_states()
    for state in states:
        if state.id == id:
            state.cities = sorted(state.cities, key=lambda y: y.name)
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', message='Not found!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
