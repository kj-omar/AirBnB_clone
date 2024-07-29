#!/usr/bin/python3
"""
Review Module - contains the Review class
"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    """
    Review class inherits from BaseModel and Base.
    Represents a review for a place by a user.
    """

    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes Review object.
        """
        super().__init__(*args, **kwargs)
