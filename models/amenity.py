#!/usr/bin/python3

"""
Amenity
"""
from os import getenv
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.place import place_amenity
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    """
    Amenity
    """
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(60), nullable=False)
        place_amenities = relationship(
            'Place', secondary=place_amenity, viewonly=False
        )
    else:
        name = ''
