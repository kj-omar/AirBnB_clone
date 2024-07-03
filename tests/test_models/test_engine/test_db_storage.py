#!/usr/bin/python3
""" Module for testing DBStorage """

import unittest
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State


class TestConsoleDBStorage(unittest.TestCase):
    """Tests for the console with DBStorage"""

    def setUp(self):
        """Set up test environment"""
        self.hbnb = HBNBCommand()
        DBStorage._DBStorage__objects.clear()
        self.hbnb.onecmd("create User email=\"test\\@email.com\"")

    def test_create_with_db(self):
        """Test creating a User instance with DBStorage"""
        all_objs = DBStorage.all(User)
        for key, obj in all_objs.items():
            if type(obj).__name__ == "User" and obj.email == "test@email.com":
                break
        else:
            self.fail("User not found or email incorrect")

class TestBaseModelDBStorage(unittest.TestCase):
    """Tests BaseModel interaction with DBStorage"""

    def setUp(self):
        """Set up test environment"""
        DBStorage._DBStorage__objects.clear()
        self.model = BaseModel()

    def test_save_and_reload(self):
        """Test saving and reloading a BaseModel instance"""
        self.model.save()
        DBStorage.reload()
        objs = DBStorage.all(BaseModel)
        self.assertIn(self.model.id, objs)

class TestModelsDBStorage(unittest.TestCase):
    """Tests various models with DBStorage"""

    def setUp(self):
        """Set up test environment"""
        DBStorage._DBStorage__objects.clear()
        self.user = User(email="test\\@email.com")
        self.place = Place(name="Test Place")
        self.state = State(name="Test State")

    def test_create_and_get_all(self):
        """Test creating and retrieving all objects"""
        self.user.save()
        self.place.save()
        self.state.save()
        DBStorage.reload()
        all_objs = DBStorage.all()
        self.assertIn(self.user.id, all_objs)
        self.assertIn(self.place.id, all_objs)
        self.assertIn(self.state.id, all_objs)

class TestDBStorage(unittest.TestCase):
    """Tests DBStorage functionalities"""

    def setUp(self):
        """Set up test environment"""
        DBStorage._DBStorage__objects.clear()
        self.user = User(email="test\\@email.com")

    def test_new_and_save(self):
        """Test adding new object and saving"""
        DBStorage.new(self.user)
        DBStorage.save()
        all_objs = DBStorage.all(User)
        self.assertIn(self.user.id, all_objs)

    def test_delete(self):
        """Test deleting an object"""
        DBStorage.delete(self.user)
        all_objs = DBStorage.all(User)
        self.assertNotIn(self.user.id, all_objs)

    def test_reload(self):
        """Test reloading storage from database"""
        DBStorage.reload()
        all_objs = DBStorage.all(User)
        self.assertIn(self.user.id, all_objs)


if __name__ == "__main__":
    unittest.main()
