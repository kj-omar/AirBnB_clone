import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models import storage


class TestDBStorage(unittest.TestCase):
    """Test cases for the DBStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.base = BaseModel()
        self.city = City()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.review = Review()
        self.amenity = Amenity()
        self.storage = storage.DBStorage()

    def tearDown(self):
        """Remove all stored instances"""
        for obj in storage.all().values():
            storage.delete(obj)
        storage.save()

    def test_all(self):
        """Test all method of DBStorage"""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn('BaseModel.' + self.base.id, all_objects)
        self.assertIn('City.' + self.city.id, all_objects)
        self.assertIn('User.' + self.user.id, all_objects)
        self.assertIn('Place.' + self.place.id, all_objects)
        self.assertIn('State.' + self.state.id, all_objects)
        self.assertIn('Review.' + self.review.id, all_objects)
        self.assertIn('Amenity.' + self.amenity.id, all_objects)

    def test_new(self):
        """Test new method of DBStorage"""
        new_obj = BaseModel()
        key = 'BaseModel.' + new_obj.id
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], new_obj)

    def test_save(self):
        """Test save method of DBStorage"""
        new_obj = BaseModel()
        key = 'BaseModel.' + new_obj.id
        storage.save()
        new_storage = storage.DBStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key], new_obj)

    def test_delete(self):
        """Test delete method of DBStorage"""
        new_obj = BaseModel()
        key = 'BaseModel.' + new_obj.id
        self.assertIn(key, storage.all())
        storage.delete(new_obj)
        self.assertNotIn(key, storage.all())

    def test_reload(self):
        """Test reload method of DBStorage"""
        storage.save()
        storage.reload()
        self.assertEqual(len(storage.all()), 1)
        new_storage = storage.DBStorage()
        self.assertEqual(len(new_storage.all()), 1)


if __name__ == "__main__":
    unittest.main()

