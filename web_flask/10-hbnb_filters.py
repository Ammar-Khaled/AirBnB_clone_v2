#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/hbnb_filters: displays an HTML page like 6-index.html
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown SQLAlchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states_list = storage.all(State).values()
    amenities_list = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states_list=states_list,
                           amenities_list=amenities_list)


if __name__ == '__main__':
    app.run(debug=True)
