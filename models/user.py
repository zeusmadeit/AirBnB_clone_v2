#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=True, default="NULL")
    last_name = Column('last_name', String(128), nullable=True, default="NULL")
    # backref may need to be back_populates?Below line commented out bc console
    # would not run with it in. This line was implemented in Task 8
    places = relationship("Place", cascade="all, delete", backref="user")
    # Below line is commented out for caution and was added in Task 9
    reviews = relationship("Review", cascade="all, delete", backref="user")