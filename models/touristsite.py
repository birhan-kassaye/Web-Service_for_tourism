import models
from models.basemodel import BaseModel
from models.description import Description
import json

class TouristSite(BaseModel):

    city_id = ""

    def __init__(self, *args, **kwargs):
        desc = Description()
            
        
        self.name = "No Name"
        self.location = "Undefined"
        self.description = desc.to_dict()

        super().__init__(*args, **kwargs)

"""    def add_site(self, name, location, description):
        site = TouristSite(name, location, description)
        self.sites.append(site)
        self.save_sites()

    def delete_site(self, index):
        if 0 <= index < len(self.sites):
            del self.sites[index]
            self.save_sites()
        else:
            print("Invalid index!")

    def save_sites(self):
        models.storage.save()

    def load_sites(self):
        try:
            with open(self.storage_file, 'r') as file:
                site_data = json.load(file)
                self.sites = [TouristSite(data['name'], data['location'], data['description']) for data in site_data]
            print("Tourist sites loaded from storage.")
        except FileNotFoundError:
            print("No existing storage file found.")
            """
