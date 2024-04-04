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
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

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
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """close"""
        self.reload()
    
    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(key, None)

