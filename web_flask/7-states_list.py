#!/usr/bin/python3
""" python script that starts a Flask
web application
"""
from models import storage
from models.state import State
from flask import Flask, abort, render_template
app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception=None):
    """close the database connection """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def State():
    """ state route """
    new_dict = storage.all(State)
    return render_template("7-states_list.html", _dict=new_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
