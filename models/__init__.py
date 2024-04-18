#!/usr/bin/python3
<<<<<<< HEAD
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
=======
"""This module instantiates an instance of the Storage will be used"""

from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD
=======

>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
storage.reload()
