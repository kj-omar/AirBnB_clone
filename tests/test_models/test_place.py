#!/usr/bin/python3
""" Place unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Place unittest tests """

     def setUp(self):
        """Creates a new Place instance for each test."""
        self.place = Place()

    def test_is_subclass_of_basemodel(self):
        """Verifies Place inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_city_id_attribute(self):
        """Tests the presence and type of the 'city_id' attribute."""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_attribute(self):
        """Tests the presence and type of the 'user_id' attribute."""
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertIsInstance(self.place.user_id, str)

    def test_name_attribute(self):
        """Tests the presence and type of the 'name' attribute."""
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertIsInstance(self.place.name, str)

    def test_description_attribute(self):
        """Tests the presence and type of the 'description' attribute."""
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_type(self):
        """Tests the type of the 'number_rooms' attribute."""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_type(self):
        """Tests the type of the 'number_bathrooms' attribute."""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_type(self):
        """Tests the type of the 'max_guest' attribute."""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_type(self):
        """Tests the type of the 'price_by_night' attribute."""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_type(self):
        """Tests the type of the 'latitude' attribute."""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_type(self):
        """Tests the type of the 'longitude' attribute."""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_type(self):
        """Tests the type of the 'amenity_ids' attribute."""
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_amenities_relationship(self):
        """Tests the many-to-many relationship with Amenity (if applicable)."""
        # Assuming you have an Amenity model and a relationship defined
        from models.amenity import Amenity  # Import Amenity if you have it

        if hasattr(self.place, 'amenities'):
            amenity = Amenity()
            self.place.amenities.append(amenity)
            self.assertIn(amenity, self.place.amenities)

    def test_reviews_relationship(self):
        """Tests the one-to-many relationship with Review (if applicable)."""
        # Assuming you have a Review model and a relationship defined
        from models.review import Review  # Import Review if you have it

        if hasattr(self.place, 'reviews'):
            review = Review()
            self.place.reviews.append(review)
            self.assertIn(review, self.place.reviews)

    def test_amenities_property_lookup(self):
        """Tests that amenities property retrieves related Amenity objects."""
        amenity_id = "test_amenity_id"
        self.place.amenity_ids.append(amenity_id)

        # Assuming you have a way to retrieve Amenity objects by ID
        amenity = self.place.get_amenity(amenity_id)  # Replace with your method
        self.assertIs not None(amenity)
