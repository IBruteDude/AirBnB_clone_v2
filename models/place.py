#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models import storage
from sqlalchemy.orm import relationship

class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    reviews = relationship("Review", backref='place')

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.review import Review
        list = []
        all_reviews = storage.all(Review)
        for review in  all_reviews.values():
            if review.place_id == self.id:
                list.append(review)
        return list
