#!/usr/bin/python3
""" City unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ City unittest tests """

    def setUp(self):
        """Creates a new City instance for each test."""
        self.city = City()

    def test_is_subclass_of_basemodel(self):
        """Verifies City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_attribute(self):
        """Tests the presence and type of the 'state_id' attribute."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertIsInstance(self.city.state_id, str)

    def test_name_attribute(self):
        """Tests the presence and type of the 'name' attribute."""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertIsInstance(self.city.name, str)

    def test_places_relationship(self):
        """Tests the one-to-many relationship with Place (if applicable)."""
        # Assuming you have a Place model and a relationship defined
        from models.place import Place  # Import Place if you have it

        if hasattr(self.city, 'places'):
            place = Place(city_id=self.city.id)
            self.assertIn(place, self.city.places)

    def test_to_dict_includes_state_id_and_name(self):
        """Verifies 'state_id' and 'name' are included in the dictionary representation."""
        city_dict = self.city.to_dict()
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
