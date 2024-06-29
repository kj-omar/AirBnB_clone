#!/usr/bin/python3
""""
 Test for db_storage.py
 """
import unittest
from models.engine.db_storage import DBStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class TestDBStorage(unittest.TestCase):
    """ unite test for db_storage.py"""
    def test_docstrings(self):
        """test docstrings"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def test_all(self):
        """test all method"""
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_new(self):
        """test new method"""
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        obj_len = len(obj)
        new_obj = State()
        new_obj.name = "California"
        storage.new(new_obj)
        storage.save()
        self.assertEqual(len(obj), obj_len + 1)

    def test_save(self):
        """test save method"""
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        obj_len = len(obj)
        new_obj = State()
        new_obj.name = "California"
        storage.new(new_obj)
        storage.save()
        storage.reload()
        obj = storage.all()
        self.assertEqual(len(obj), obj_len + 1)

    def test_delete(self):
        """test delete method"""
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        obj_len = len(obj)
        new_obj = State()
        new_obj.name = "California"
        storage.new(new_obj)
        storage.save()
        storage.delete(new_obj)
        storage.save()
        storage.reload()
        obj = storage.all()
        self.assertEqual(len(obj), obj_len)

    def test_reload(self):
        """ test reload method """
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        obj_len = len(obj)
        new_obj = State()
        new_obj.name = "California"
        storage.new(new_obj)
        storage.save()
        storage.reload()
        obj = storage.all()
        self.assertEqual(len(obj), obj_len + 1)
