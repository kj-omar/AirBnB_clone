#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """Resets storage for each test case."""
        storage.reload()  # Clear any existing data

    def tearDown(self):
        """Removes storage file after each test."""
        try:
            os.remove('file.json')
<<<<<<< HEAD
        except ValueError:
=======
        except FileNotFoundError:
>>>>>>> master
            pass

    def test_obj_list_empty(self):
        """Tests if __objects is initially empty."""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """Tests if a new object is added correctly."""
        new_obj = BaseModel()
        self.assertIn(new_obj.id, storage.all().keys())  # Check by ID in storage

    def test_all(self):
        """Tests if __objects is returned as a dict."""
        new_obj = BaseModel()
        self.assertIsInstance(storage.all(), dict)

    def test_base_model_instantiation(self):
        """Tests if saving a BaseModel doesn't create 'file.json'."""
        new_obj = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_save(self):
        """Tests if FileStorage.save() creates 'file.json'."""
        new_obj = BaseModel()
        new_obj.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_updates_file(self):
        """Tests if FileStorage.save() updates the file."""
        new_obj = BaseModel()
        new_obj.save()
        original_size = os.path.getsize('file.json')
        new_obj.name = "Updated Name"
        new_obj.save()
        self.assertGreater(os.path.getsize('file.json'), original_size)

    def test_reload(self):
        """Tests if FileStorage.reload() loads objects from file."""
        new_obj = BaseModel()
        new_obj.save()
        storage.reload()
        loaded_obj = storage.all().get(f"{new_obj.__class__.__name__}.{new_obj.id}")
        self.assertIsInstance(loaded_obj, BaseModel)
        self.assertEqual(loaded_obj.id, new_obj.id)

    def test_reload_empty_file(self):
        """Tests if FileStorage.reload() handles an empty file."""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_nonexistent_file(self):
        """Tests if FileStorage.reload() handles a missing file."""
        self.assertEqual(storage.reload(), None)  # No error, returns None

    def test_type_path(self):
        """Tests if __file_path is a string."""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Tests if __objects is a dict."""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Tests if object keys in storage are formatted correctly."""
        new_obj = BaseModel()
        expected_key = f"{new_obj.__class__.__name__}.{new_obj.id}"
        self.assertIn(expected_key, storage.all().keys())

    def test_storage_var_created(self):
        """Tests if the storage object is created correctly."""
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

    def test_get_reviews_empty(self):
        """Tests get_reviews with no reviews for a place."""
        reviews = storage.get_reviews("non-existent_place_id")
        self.assertEqual(len(reviews), 0)

    def test_get_reviews_with_reviews(self):
        """Tests get_reviews with existing reviews for a place."""
        place_id = "test_place_id"
        for _ in range(3):
            review
