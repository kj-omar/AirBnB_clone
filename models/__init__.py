#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os

# _type = {**os.environ}['HBNB_TYPE_STORAGE']
# if str(_type) == 'db':
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
