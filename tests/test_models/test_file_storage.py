import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.base = BaseModel()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()
        self.objects = storage._FileStorage__objects
        self.file_path = storage._FileStorage__file_path

    def tearDown(self):
        """Restore standard file path and remove file if exists"""
        storage._FileStorage__file_path = self.file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method of FileStorage"""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn('BaseModel.' + self.base.id, all_objects)
        self.assertIn('User.' + self.user.id, all_objects)
        self.assertIn('Place.' + self.place.id, all_objects)
        self.assertIn('State.' + self.state.id, all_objects)
        self.assertIn('City.' + self.city.id, all_objects)
        self.assertIn('Amenity.' + self.amenity.id, all_objects)
        self.assertIn('Review.' + self.review.id, all_objects)

    def test_new(self):
        """Test new method of FileStorage"""
        new_obj = BaseModel()
        key = 'BaseModel.' + new_obj.id
        self.assertIn(key, self.objects)
        self.assertEqual(self.objects[key], new_obj)

    def test_save_reload(self):
        """Test save and reload methods of FileStorage"""
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        # Create a new FileStorage instance to reload the data
        new_storage = storage.FileStorage()
        new_storage.reload()

        self.assertEqual(len(new_storage.all()), len(self.objects))
        for key in self.objects:
            self.assertIn(key, new_storage.all())
            self.assertEqual(self.objects[key].to_dict(),
                             new_storage.all()[key].to_dict())

    def test_delete(self):
        """Test delete method of FileStorage"""
        new_obj = BaseModel()
        key = 'BaseModel.' + new_obj.id
        self.assertIn(key, self.objects)

        storage.delete(new_obj)
        self.assertNotIn(key, self.objects)


if __name__ == "__main__":
    unittest.main()

