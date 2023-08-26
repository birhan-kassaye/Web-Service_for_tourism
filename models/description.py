import models
from models.basemodel import BaseModel


class Description(BaseModel):
    def __init__(self, *args, **kwargs):

        self.type = "Recreational"
        self.price = "Moderate/ Free"
        self.detail = "Put all the info not included inside here"

        super().__init__(*args, **kwargs)
