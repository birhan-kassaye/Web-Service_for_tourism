from models.basemodel import BaseModel, Base;
from sqlalchemy import Column, String, Text
from os import getenv


class Description(BaseModel, Base):

    if getenv('STORAGE_TYPE') == 'db':
        __tablename__ = 'description'
        type = Column(String, nullable=False)
        price = Column(String, nullable=False)
        detail = Column(Text, nullable=False)

    def __init__(self, *args, **kwargs):

        self.type = "Recreational"
        self.price = "Moderate/ Free"
        self.detail = "Put all the info not included inside here"

        super().__init__(*args, **kwargs)
