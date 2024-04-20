<<<<<<< HEAD
#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
=======
#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
    else:
        place_id = ""
        user_id = ""
        text = ""
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
=======
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
