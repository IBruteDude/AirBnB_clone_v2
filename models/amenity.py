#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = None
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        from models.place import Place
        if Amenity.place_amenities is None:
            Amenity.place_amenities = relationship('Place', secondary=Place.place_amenity)
