#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024),
                        nullable=False)
        place_id = Column(String(60),
                            ForeignKey('places.id'),
                            nullable=False)
        user_id = Column(String(60),
                            ForeignKey('users.id'),
                            nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)