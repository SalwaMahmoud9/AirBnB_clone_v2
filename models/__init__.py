#!/usr/bin/python3
"""init"""
from os import getenv
from .user import User
from .city import City
from .place import Place
from .state import State
from .review import Review
from .amenity import Amenity
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':    
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
