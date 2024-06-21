#!/usr/bin/python3
""" Review unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Review unittest tests """

    def setUp(self):
        """Creates a new Review instance for each test."""
        self.review = Review()

    def test_is_subclass_of_basemodel(self):
        """Verifies Review inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_place_id_attribute(self):
        """Tests the presence and type of the 'place_id' attribute."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_attribute(self):
        """Tests the presence and type of the 'user_id' attribute."""
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertIsInstance(self.review.user_id, str)

    def test_text_attribute(self):
        """Tests the presence and type of the 'text' attribute."""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertIsInstance(self.review.text, str)

    def test_instance(self):
        """Verify if it instantiates correctly"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Verify attributes are present"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
