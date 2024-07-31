#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage.
This module also defines a class to manage file storage
for AirBnB_clone_v2.
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Add a conditional depending of the value of the env variable
if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
