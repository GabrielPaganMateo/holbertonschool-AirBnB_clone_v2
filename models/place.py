#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import environ
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True),
Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref = 'place', cascade = 'all, delete')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    else:
        pass
        """@property
        def amenities(self):
            from models import storage
            for amenity in storage.all(Amenity):"""





    
    """@property
    def amenities(self):
        print("Amenities")
        from models import storage
        for amenity in storage.all(Amenity):
            if amenity.id == place_amenity.amenity_id:
                self.amenity_ids.append(amenity)
        return self.amenity_ids
    else:
        @property
        def reviews(self):
            from models import storage
            reviews = []
            for review in storage.all(Review):
                if Review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            from models import storage
            amenities = []
            for amenity in storage.all(Amenity):
                if amenity.id == place_amenity.amenity_id:
                    amenities.append(amenity)
            return amenities
        
        @property.setter
        def amenities(self, amenity):
            self.amenity_ids.append(amenity)"""