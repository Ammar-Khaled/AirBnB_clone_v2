#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.
and fetching data from the storage engine.

Routes:
/cities_by_states: displays a HTML page containing a list of
all City objects linked to the State sorted by name (A->Z)
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states_list = storage.all(State).values()
    cities_by_states = {}
    for state in states_list:
        cities_by_states[state] = state.cities
    return render_template('7-states_list.html', states_list=states_list,
                           cities_by_states=cities_by_states)


if __name__ == '__main__':
    app.run()
