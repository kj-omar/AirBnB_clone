#!/usr/bin/python3
""" User unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ User unittest tests """

    def setUp(self):
        """Creates a new User instance for each test."""
        self.user = User()

    def test_is_subclass_of_basemodel(self):
        """Verifies User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_email_attribute(self):
        """Tests the presence and type of the 'email' attribute."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertIsInstance(self.user.email, str)

    def test_password_attribute(self):
        """Tests the presence and type of the 'password' attribute."""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertIsInstance(self.user.password, str)

    def test_first_name_attribute(self):
        """Tests the presence and type of the 'first_name' attribute."""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_attribute(self):
        """Tests the presence and type of the 'last_name' attribute."""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertIsInstance(self.user.last_name, str)

    def test_instance(self):
        """Verify if it instantiates correctly"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Verify that the attributes are present"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    # No need to repeat type checks for attributes as they are already covered

    def test_relationships(self):
        """Check class relationships"""
        self.assertTrue(hasattr(self.user, 'places'))
        self.assertTrue(hasattr(self.user, 'reviews'))

    def test_relationships_type(self):
        """Check relationship types"""
        from models.place import Place
        from models.review import Review

        self.assertIsInstance(self.user.places, list)
        self.assertIsInstance(self.user.reviews, list)
        self.assertTrue(all(isinstance(place, Place) for place in self.user.places))
        self.assertTrue(all(isinstance(review, Review) for review in self.user.reviews))

    def test_relationships_backref(self):
        """Check the relationships backref"""
        from models.place import Place
        from models.review import Review

        place = Place(user=self.user)
        review = Review(user=self.user)
        self.assertIn(place, self.user.places)
        self.assertIn(review, self.user.reviews)

    def test_relationships_cascade_delete(self):
        """Check the elimination cascade"""
        from models.place import Place
        from models.review import Review

        place = Place(user=self.user)
        review = Review(user=self.user)
        self.assertIn(place, self.user.places)
        self.assertIn(review, self.user.reviews)
        self.user.delete()
        self.assertNotIn(place, self.user.places)
        self.assertNotIn(review, self.user.reviews)
