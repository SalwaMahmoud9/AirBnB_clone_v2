#!/usr/bin/python3
"""init"""
from os import getenv
from .user import User
from .city import City
from .place import Place
from .state import State
from .review import Review
from .amenity import Amenity
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') != 'db':
    storage = FileStorage()  
else:
    storage = DBStorage()
storage.reload()
