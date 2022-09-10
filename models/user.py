#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if HBNB_TYPE_STORAGE == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            "Place",
            cascade="all,delete",
            backref=backref("user", cascade="all,delete"),
            passive_deletes=True,
            single_parent=True
        )
        reviews = relationship(
            "Review",
            cascade="all,delete",
            backref=backref("user", cascade="all,delete"),
            passive_deletes=True,
            single_parent=True
        )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
