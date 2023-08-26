from models.basemodel import BaseModel
from models.touristsite import TouristSite
from models.city import City
from models.engine.filestorage import FileStorage

if __name__ == '__main__':
    city = City()
    new = TouristSite()
    new.city_id = city.id
    new2 = TouristSite()
    new2.city_id = city.id
    new3 = TouristSite()
    new3.city_id = city.id
    new.save()
    new2.save()
    new3.save()
    city.save()
    print(city.places)
