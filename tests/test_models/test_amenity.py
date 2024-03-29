#!/usr/bin/python3
""" Unittests for amenity class """
import models
import unittest
from os import getenv
from datetime import datetime
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(unittest.TestCase):
    """ Test class amenity"""

    def test_instantiation(self, *args, **kwargs):
        """ Test the amenity instantiation"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertIsNotNone(new_amenity.id)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)

    def test_attributes(self):
        """ Test amenities attributes """
        new_amenity = Amenity()
        new_amenity.name = "Spa"
        self.assertEqual(new_amenity.name, "Spa")

        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertIsInstance(new_amenity.place_amenities, list)

    def test_amenity_save_and_update(self):
        amenity = Amenity()
        amenity.name = "Outdoor"
        created_at = amenity.created_at
        updated_at = amenity.updated_at

        amenity.save()
        self.assertNotEqual(amenity.updated_at, updated_at)
        self.assertEqual(amenity.created_at, created_at)

        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertIsNotNone(models.storage.get(Amenity, amenity.id))
        else:
            self.assertIsNotNone(models.storage.all().get(
                f"Amenity.{amenity.id}"))

    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity.name = "Wifi"
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["name"], "Wifi")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
