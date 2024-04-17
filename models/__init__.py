#!/usr/bin/python3
"""Chooses and instantiates a storage engine based on environment.
If 'HBNB_TYPE_STORAGE' is set to 'db', uses a database storage engine.
Otherwise, defaults to a file system storage engine.
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
