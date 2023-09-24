#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/states: displays a HTML page with the list of
all State objects present in DBStorage sorted by name (A->Z)
/states/<id>: displays a HTML page of the state wtih <id>
and its cities if found
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states_list=states_list)


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    states_list = storage.all(State).values()
    for state in states_list:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html'), 404

if __name__ == '__main__':
    app.run()
