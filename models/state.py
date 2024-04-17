#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            values_city = models.storage.all("City").values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city