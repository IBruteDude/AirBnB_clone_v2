#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60), ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60), ForeignKey('amenities.id'),
                                 primary_key=True,  nullable=False))
    amenity_ids = []
    reviews = relationship("Review", backref='place', cascade='all, delete')
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.amenity import Amenity
        amenities = relationship('Amenity', 'place_amenity', viewonly=True)
    else:
        @property
        def amenities(self):
            """an amenities property for handling associated amenities"""
            from models.amenity import Amenity
            amenity_list = []
            for amenity in storage.all(Amenity).values():
                assert type(amenity) is Amenity
                if amenity.id in Place.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            from models.amenity import Amenity
            if type(amenity) is Amenity:
                Place.amenity_ids.append(amenity.id)

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.review import Review
        list = []
        all_reviews = storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                list.append(review)
        return list
