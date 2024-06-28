#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage.reload()
=======
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

istorage.reload()
>>>>>>> clone
