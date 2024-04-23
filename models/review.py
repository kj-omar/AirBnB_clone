#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(
        String(length=60),
        ForeignKey('places.id'),
        nullable=False
    )
    user_id = Column(
        String(length=60),
        ForeignKey('users.id'),
        nullable=False
    )
    text = Column(
        String(length=1024),
        nullable=False
    )
