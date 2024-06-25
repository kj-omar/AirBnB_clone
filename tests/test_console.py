#!/usr/bin/python3
"""Defines unittests for console.py."""

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os
import unittest

class TestHBNBCommand(unittest.TestCase):
    """HBNB console unittests."""

    @classmethod
    def setUpClass(cls):
        """Testing setup"""
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Testing cleanup."""
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create_errors(self):
        """Test output for create command errors."""
        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n",op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n",op.getvalue())

    def test_create_command_validity(self):
        """Test create command."""
        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create BaseModel")
            base_model =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create User")
            user =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create State")
            state =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create Place")
            place =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create City")
            city =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create Review")
            rv =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("create Amenity")
            am =op.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(base_model,op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all User")
            self.assertIn(user,op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all State")
            self.assertIn(state,op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all Place")
            self.assertIn(place,op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all City")
            self.assertIn(city,op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all Review")
            self.assertIn(rv,op.getvalue())

        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(am,op.getvalue())

<<<<<<< HEAD
    def test_create_command_with_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as op:
            call = ('create Place city_id="0100" name="Our_House" number_rooms=10 latitude=56.81 longitude=55.739')
            self.HBNB.onecmd(call)
            place =op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            self.HBNB.onecmd("all Place")
            output =op.getvalue()
            self.assertIn(place, output)
            self.assertIn("'city_id': '0100'", output)
            self.assertIn("'name': 'Our House'", output)
            self.assertIn("'number_rooms': 10", output)
            self.assertIn("'latitude': 56.81", output)
            self.assertIn("'longitude': 55.739", output)
=======
        #def test_create_command_with_kwargs(self):
        #    """Test create command with kwargs."""
        #    # Test create command with additional key-value pairs
        #    with patch("sys.stdout", new=StringIO()) as op:
        #        call = (f'create Place city_id="0001" name="My_house" number_rooms=4 latitude=37.77 longitude=43.434')  # noqa
        #        self.HBNB.onecmd(call)
        #        place =op.getvalue().strip()
        #     # Test if the created instance and kwargs are in the
        #     #    output of "all" command
        #    with patch("sys.stdout", new=StringIO()) as op:
        #        self.HBNB.onecmd("all Place")
        #        output =op.getvalue()
        #        self.assertIn(place, output)
        #        self.assertIn("'city_id': '0001'", output)
        #        self.assertIn("'name': 'My house'", output)
        #        self.assertIn("'number_rooms': 4", output)
        #        self.assertIn("'latitude': 37.77", output)
        #        self.assertIn("'longitude': 43.434", output)
>>>>>>> 263cb865d962dcbe7a8650a44f53812cdb583860


if __name__ == "__main__":
    unittest.main()
