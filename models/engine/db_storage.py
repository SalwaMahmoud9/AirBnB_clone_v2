#!/usr/bin/python3

"""
models
"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def all(self, cls=None):
        """all"""
        objs = []
        if cls is None:
            Classes = [User, City, State, Place, Review, Amenity]
            try:
                for Class in Classes:
                    objs = objs + self.__session.query(Class).all()
            except Exception:
                pass
        else:
            Class = eval(cls) if type(cls) == str else cls
            objs = self.__session.query(Class).all()
        return {'{}.{}'.format(type(o).__name__, o.id): o for o in objs}

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close."""
        self.__session.close()

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            self.__session.delete(obj)        
