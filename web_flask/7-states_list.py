#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/states_list: display a HTML page with the list of
all State objects present in DBStorage sorted by name (A->Z)
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown SQLAlchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def all_states():
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == '__main__':
    app.run()
