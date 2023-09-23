#!/usr/bin/python3
"""This module instantiates an object of desired storage class."""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

tables = {'State', 'City', 'Place', 'User', 'Review', 'Amenity'}
classes = {
    'Base': Base, 'BaseModel': BaseModel, 'User': User, 'State': State,
    'City': City, 'Amenity': Amenity, 'Review': Review, 'Place': Place,
}

storage = None
if (getenv('HBNB_TYPE_STORAGE') == 'db'):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
