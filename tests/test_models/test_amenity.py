#!/usr/bin/python3
""" Amenity unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Amenity unittest tests """

    def setUp(self):
        """Creates a new Amenity instance for each test."""
        self.amenity = Amenity()

    def test_is_subclass_of_basemodel(self):
        """Verifies Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_name_attribute(self):
        """Tests the presence and type of the 'name' attribute."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertIsInstance(self.amenity.name, str)

    def test_name_default_value(self):
        """Verifies the default value of the 'name' attribute."""
        self.assertEqual(self.amenity.name, '')

    def test_place_amenities_relationship(self):
        """Tests the many-to-many relationship with Place (if applicable)."""
        # Assuming you have a Place model and a relationship defined
        from models.place import Place  # Import Place if you have it

        if hasattr(self.amenity, 'place_amenities'):
            place = Place()
            self.amenity.place_amenities.append(place)
            self.assertIn(place, self.amenity.place_amenities)

    def test_to_dict_includes_name(self):
        """Verifies 'name' is included in the dictionary representation."""
        amenity_dict = self.amenity.to_dict()
        self.assertIn('name', amenity_dict)
