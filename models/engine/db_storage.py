#!/usr/bin/env python3
"""
Defines the DBStorage class
"""
from dotenv import load_dotenv
from models.basemodel import Base
from models.basemodel import BaseModel
from models.touristsite import TouristSite
from models.description import Description
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote

load_dotenv()

db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_host = getenv('DB_HOST')
db_name = getenv('DB_DATABASE')

classes = {
        'City': City,
        'TouristSite': TouristSite
        }


class DBStorage:
    """
    Database Storage configuration and representation
    of the web service
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        db_url =  'mysql+mysqldb://' + db_user + ':' + db_pass + '@' + db_host + '/' + db_name
        self.__engine = create_engine(db_url, echo=True)


    def all(self, cls=None):
        """
        Reterives all objects of a given class
        in the database
        """
        dic = {}
        if cls is None:
            for i in classes:
                objs = self.__session.query(classes[i]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dic[key] = obj
        else:
            if cls in classes:
                objs = self.__session.query(classes[cls]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dic[key] = obj
        return dic


    def new(self, obj):
        """
        Adds a new object to the session created
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves object to the database
        """
        self.__session.commit()

    def reload(self):
        """
        Reloads objects from the database
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(sess_factory)
        self.__session = Session
