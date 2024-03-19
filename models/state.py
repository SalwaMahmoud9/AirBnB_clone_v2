#!/usr/bin/python3

"""
State
"""
import os
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State
    """
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

        @property
        def cities(self):
            """
            cities
            """
            from models.city import City
            from models import storage
            city_list = list(storage.all(City).values())
            return [city for city in city_list if city.state_id == self.id]
