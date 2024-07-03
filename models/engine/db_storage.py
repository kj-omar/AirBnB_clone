#!/usr/bin/python3
"""This module defines a class to manage the SQL db for hbnb clone"""


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of the DB"""
    __engine = None
    __session = None
