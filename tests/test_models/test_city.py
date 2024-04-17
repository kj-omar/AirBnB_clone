#!/usr/bin/python3
"""Test cases for the City class"""

import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.city import City

class TestCity(TestBaseModel):
    """Test cases for the City class"""

    def setUp(self):
        """Set up test objects"""
        super().setUp()
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id attribute"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == '__main__':
    unittest.main()

