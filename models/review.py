from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base  # Importing BaseModel and Base from your project

class Review(BaseModel, Base):
    __tablename__ = 'reviews'  # Table name
    
    text = Column(String(1024), nullable=False)  # Column for review text (max 1024 characters, not nullable)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)  # Foreign key to places table
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)  # Foreign key to users table
    
    place = relationship("Place", back_populates="review")
    user = relationship("User", back_populates="reviews")
