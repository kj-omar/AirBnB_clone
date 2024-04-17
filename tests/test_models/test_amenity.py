#!/usr/bin/python3
"""Test cases for the Amenity class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity

class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test objects"""
        super().setUp()
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """Test name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == '__main__':
    unittest.main()

