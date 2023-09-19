#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), name="state_id", nullable=False)
    name = Column(String(128), nullable=False)
