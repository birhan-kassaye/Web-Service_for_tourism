import models
from models.basemodel import BaseModel
from models.touristsite import TouristSite

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        self.name = "No Name"
        self.weather = "Weyna Dega"
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
