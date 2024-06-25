#!/usr/bin/python3
# models/review.py
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Review class representing a review for a place by a user."""
    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize Review object."""
        super().__init__(*args, **kwargs)
