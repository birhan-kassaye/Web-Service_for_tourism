import json
from models.basemodel import BaseModel
from models.touristsite import TouristSite
from models.city import City

classes = {
        'BaseModel': BaseModel, 
        'City': City,
        'TouristSite': TouristSite
        }

class FileStorage:
    """FileStorage Representation"""

    __file = 'app/static/file.json'
    __objects = {}


    def all(self, cls=None):
        """Reterives all objects of the given class"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects



    def new(self, obj):
        """Adds a newly created object to objects"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves all created instances"""
        json_objects = {}
        for key in self.__objects.keys():
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file, 'w') as f:
            json.dump(json_objects, f)

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]


    def reload(self):
        """Reloads existing objects from the file"""
        try:
            with open(FileStorage.__file) as f:
                json_objects = json.load(f)
                for key, value in json_objects.items():
                    cls_name = value["__class__"]
                    obj = eval(cls_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
