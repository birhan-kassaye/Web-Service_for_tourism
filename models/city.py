import models
from os import getenv
from models.basemodel import BaseModel, Base
from models.touristsite import TouristSite
from sqlalchemy import Column, String, Integer, Enum


class City(BaseModel, Base):
    if getenv('STORAGE_TYPE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(20), unique=True)
        weather = Column(String(40))
        population = Column(Integer)
        region = Column(String(20))

    def __init__(self, *args, **kwargs):
        self.name = "No Name"
        self.weather = 'Weyna Dega'
        self.population = 100000
        self.region = "Gambella"
        super().__init__(*args, **kwargs)

    @property
    def places(self):
        places = []
        for i in models.storage.all(TouristSite).values():
            if i.city_id == self.id:
                places.append(i.to_dict())
        return (places)
