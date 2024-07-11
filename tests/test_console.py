import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestConsoleCreateCommand(unittest.TestCase):
    """Tests for the create command with parameters"""

    def setUp(self):
        """Set up test environment"""
        self.hbnb = HBNBCommand()

    def test_create_with_params(self):
        """Test creating a BaseModel instance with parameters"""
        string = (
            f"create BaseModel name=\"MyModel\" number={1234.56} "
            f"float_attr={3.14} int_attr={7}"
        )

        self.hbnb.onecmd(string)
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if type(obj).__name__ == "BaseModel" and obj.name == "MyModel":
                self.assertEqual(obj.number, 1234.56)
                self.assertEqual(obj.float_attr, 3.14)
                self.assertEqual(obj.int_attr, 7)
                break
        else:
            self.fail("Object not found or attributes incorrect")

    def test_create_with_string_param(self):
        """Test creating a User instance with a string parameter"""
        self.hbnb.onecmd("create User email=\"test\\@email.com\"")
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if type(obj).__name__ == "User" and obj.email == "test@email.com":
                break
        else:
            self.fail("User not found or email incorrect")

    def test_create_with_underscore(self):
        """Test creating an instance with
          an underscore in the attribute name"""
        self.hbnb.onecmd("create BaseModel name=\"My_little_house\"")
        all_objs = storage.all()
        for key, obj in all_objs.items():
            type_n = f"BaseModel"
            obj_n = f"My little house"

            if type(obj).__name__ == type_n and obj.name == obj_n:
                break
        else:
            self.fail("BaseModel not found or name incorrect")

    def test_create_with_unrecognized_param(self):
        """Test creating an instance with an unrecognized parameter"""
        self.hbnb.onecmd("create BaseModel unrecognized=param")
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if type(obj).__name__ == "BaseModel":
                self.assertNotIn("unrecognized", obj.__dict__)
                break
        else:
            self.fail("BaseModel not found")


if __name__ == "__main__":
    unittest.main()
