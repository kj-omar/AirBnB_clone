#!/usr/bin/python3
""" python script that starts a Flask
web application
"""
from models import storage
from models.state import State
from flask import Flask, abort, render_template
app = Flask(__name__)

@app.route("/states/", defaults={'id': 0})
@app.route('/states/<id>', strict_slashes=False)
def State_city(id):
    """ state route """
    try:
        id = int(id)
    except ValueError:
        abort(404)

    new_dict = storage.all("State")
    states = list(new_dict.values())
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """close the database connection """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
