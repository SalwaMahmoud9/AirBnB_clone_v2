#!/usr/bin/python3

"""
file_storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """new"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """save"""
        with open(FileStorage.__file_path, 'w') as f:
            var1 = {}
            var1.update(FileStorage.__objects)
            for k, v in var1.items():
                var1[k] = v.to_dict()
            json.dump(var1, f)

    def all(self, cls=None):
        """all"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            return {k: v for k, v in self.__objects.items() if type(v) == cls}
        return self.__objects

    def reload(self):
        """reload"""
        classes = {
            'BaseModel': BaseModel,
            'User': User, 'Place': Place, 'State': State,
            'City': City, 'Amenity': Amenity, 'Review': Review
        }
        try:
            var1 = {}
            with open(FileStorage.__file_path, 'r') as f:
                var1 = json.load(f)
                for k, v in var1.items():
                    self.all()[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass

    def close(self):
        """close"""
        self.reload()

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            k = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(k, None)
