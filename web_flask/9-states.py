#!/usr/bin/python3
""" python script that starts a Flask
web application
"""
from models import storage
from models.state import State
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def States():
    """ state route """
    new_dict = storage.all("State")
    states = list(new_dict.values())
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def State_city(id):
    """ state_city route """

    new_dict = storage.all("State")
    states = list(new_dict.values())
    state = next((state for state in states if state.id == id), None)
    return render_template("9-states.html", states=[state], id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """close the database connection """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
