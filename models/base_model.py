#!/usr/bin/python3
"""Defines a base model class."""
import models
import json
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """docstring for BaseModel"""
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, **kwargs):
        """Initialize a Base.

        Args:
            id: id of the Base.
            created_at: created_at of the Base.
            updated_at: iupdated_atd of the Base.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key not in ["__class__", "created_at", "updated_at"]:
                    setattr(self, key, value)
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return class name, id, and the dictionary"""
        attributes = {}
        attributes.update(self.__dict__)
        attributes.pop('_sa_instance_state', None)
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, attributes)        

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary"""
        dic = {}
        dic.update(self.__dict__)
        dic.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic.pop('_sa_instance_state', None)
        return dic 
       
    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def delete(self):
        """Delete"""
        models.storage.delete(self)

    

    
