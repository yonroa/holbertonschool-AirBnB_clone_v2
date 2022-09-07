#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
class Amenity(BaseModel, Base):
    """"""
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)