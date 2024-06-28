from sqlalchemy import Column, String
from .base_model import BaseModel
from .base import Base
from sqlalchemy.orm import relationship, back_populates

class User(BaseModel, Base):
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Relationship to Review objects
    reviews = relationship("Review",
                           back_populates="user",
                           cascade="all, delete-orphan",
                           passive_deletes=True)
