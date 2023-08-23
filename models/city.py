from sqlalchemy import Column, String, Integer
from models.basemodel import BaseModel, Session

class City(BaseModel):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    population = Column(Integer)

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population
        }

Base.metadata.create_all(engine)
