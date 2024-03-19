#!/usr/bin/python3

"""
User
"""
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    User
    """
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            'Place', backref='user', cascade='all, delete')
        reviews = relationship(
            'Review', backref='user', cascade='all, delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
