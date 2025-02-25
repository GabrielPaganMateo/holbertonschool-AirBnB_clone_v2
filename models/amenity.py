#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
from os import environ


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary=place_amenity,
                                       back_populates='amenities')
