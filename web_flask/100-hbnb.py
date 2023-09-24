#!/usr/bin/python3
"""
This module starts a Flask web application that
is listening on 0.0.0.0, port 5000.

Routes:
/hbnb: display a HTML page like 8-index.html.
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown SQLAlchemy session"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """ Displays an HTML page like 8-index.html """
    states_list = storage.all(State).values()
    amenities_list = storage.all(Amenity).values()
    places_list = storage.all(Place).values()
    return render_template('100-hbnb.html', states_list=states_list,
                           amenities_list=amenities_list,
                           places_list=places_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
