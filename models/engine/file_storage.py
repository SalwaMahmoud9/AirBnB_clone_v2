#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """storage engine
    Methods:
        all: all
        new: new
        save: save
        reload: reload
    Attributes:
        __file_path (str): __file_path
        __objects (dict): __objects
        class_dict (dict): class_dict
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel,
                  "User": User,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Place": Place,
                  "Review": Review
                  }

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(obj_dict, file)

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                new_obj_dict = json.load(file)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
