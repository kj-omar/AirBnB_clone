#!/usr/bin/python3
"""Starts a flask app that uses db storage"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Renders 10-hbhb_filters.html"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbhb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """Ends current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
