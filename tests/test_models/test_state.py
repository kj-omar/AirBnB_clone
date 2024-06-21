#!/usr/bin/python3
""" State unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ State unittest tests """

    def setUp(self):
        """Creates a new State instance for each test."""
        self.state = State()

    def test_is_subclass_of_basemodel(self):
        """Verifies State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_name_attribute(self):
        """Tests the presence and type of the 'name' attribute."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertIsInstance(self.state.name, str)

    def test_name_type(self):
        """Tests the type of the 'name' attribute (can be removed)."""
        self.assertIsInstance(self.state.name, str)

    def test_cities_relationship(self):
        """Tests the one-to-many relationship with City (if applicable)."""
        from models.city import City

        if hasattr(self.state, 'cities'):
            city = City(state_id=self.state.id)
            self.assertIn(city, self.state.cities)

    def test_cities_property(self):
        """Tests that the 'cities' property retrieves related City objects (if applicable)."""
        city = City(state_id=self.state.id)
        state_cities = self.state.get_cities()
        self.assertIn(city, state_cities)

    def test_instance(self):
        """Verify if it instantiates correctly (can be removed)."""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Verify attributes are present (can be removed)."""
        self.assertTrue(hasattr(self.state, 'name'))
