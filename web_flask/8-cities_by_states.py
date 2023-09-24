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
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states_list = storage.all(State).values()
    return render_template('8-cities_by_states.html', states_list=states_list)


if __name__ == '__main__':
    app.run()
