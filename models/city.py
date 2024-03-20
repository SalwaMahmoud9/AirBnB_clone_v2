#!/usr/bin/python3

"""
City
"""
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """
    City
    """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        name = ''
        state_id = ''     
    else:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            'Place', backref='cities', cascade='all, delete, delete-orphan')
        
