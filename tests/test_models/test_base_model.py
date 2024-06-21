#!/usr/bin/python3
""" Base Model unittest tests """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Base Model unittest tests """

    def setUp(self):
        """Executed before each test."""
        pass

    def tearDown(self):
        """Executed after each test. Removes 'file.json' if it exists."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default_initialization(self):
        """Tests creating a BaseModel instance with default values."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_kwargs_initialization(self):
        """Tests creating a BaseModel instance with keyword arguments."""
        name = "TestName"
        created_at = datetime.datetime.utcnow()
        instance = BaseModel(name=name, created_at=created_at)
        self.assertEqual(instance.name, name)
        self.assertEqual(instance.created_at, created_at)

    def test_kwargs_invalid_type(self):
        """Tests creating a BaseModel instance with invalid keyword argument type."""
        with self.assertRaises(TypeError):
            BaseModel(id=1)  # ID should be a string

    def test_save(self):
        """Tests saving a BaseModel instance to a file."""
        instance = BaseModel()
        instance.save()

        key = f"{BaseModel.__name__}.{instance.id}"
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertIn(key, data)
            self.assertEqual(data[key], instance.to_dict())

    def test_str(self):
        """Tests the string representation of a BaseModel instance."""
        instance = BaseModel()
        expected_string = f"[{BaseModel.__name__}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_string)

    def test_to_dict(self):
        """Tests converting a BaseModel instance to a dictionary."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["created_at"], instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], instance.updated_at.isoformat())

    def test_kwargs_none(self):
        """Tests creating a BaseModel instance with None keyword arguments."""
        with self.assertRaises(TypeError):
            BaseModel()

    def test_kwargs_one(self):
        """Tests creating a BaseModel instance with one invalid keyword argument."""
        with self.assertRaises(KeyError):
            BaseModel(Name="test")  # Invalid key "Name"

    def test_updated_at_on_save(self):
        """Tests that updated_at is updated on save."""
        instance = BaseModel()
        initial_updated_at = instance.updated_at

        instance.save()
        instance.save()  # Save again

        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_delete(self):
        """Tests deleting a BaseModel instance from the file."""
        instance = BaseModel()
        instance.save()

        instance.delete()
        key = f"{BaseModel.__name__}.{instance.id}"

        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertNotIn(key, data)

    def test_init_with_args(self):
        """Tests creating a BaseModel instance with positional arguments (should raise error)."""
        with self.assertRaises(TypeError):
            BaseModel("argument")  # Positional arguments not allowed
