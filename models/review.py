#!/usr/bin/python3

"""
Review
"""
from os import getenv
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """
    Review
    """
    __tablename__ = 'reviews'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ''
        place_id = ''
        user_id = ''
