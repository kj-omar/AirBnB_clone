#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from models.place import Place
from models.state import State
from console import HBNBCommand
from unittest.mock import MagicMock, patch
from models.engine.file_storage import FileStorage
from tests.test_models.test_base_model import test_basemodel


class test_console(test_basemodel):
    """ Class to test the file storage method """

    def setUp(self):
        self.console = HBNBCommand()

    @patch('builtins.print')
    def test_do_create_int(self, mock_print):
        try:
            HBNBCommand.do_create(self, "Place number_rooms=four")
        except ValueError:
            self.assertNotIsInstance(int, type(Place.number_rooms))

    @patch('builtins.print')
    def test_do_create_float(self, mock_print):
        try:
            HBNBCommand.do_create(self, "Place latitude=thirty")
        except ValueError:
            self.assertNotIsInstance(float, type(Place.latitude))

    def test_create_state_db(self):
        """ Test if a state is created when calling do_create"""
        if os.getenv('HBNB_ENV') == 'test' and os.getenv(
                'HBNB_TYPE_STORAGE') == 'db':
            self.cursor.execute(
                "SELECT COUNT(*) from states")
            number_states_before = self.cursor.fetchone()[0]

            HBNBCommand().do_create("State name=Louisiana")

            self.cursor.execute(
                "SELECT COUNT(*) from states")
            number_states_after = self.cursor.fetchone()[0]
            self.assertEqual(number_states_after - number_states_before, 1)

            self.cursor.execute(
                "SELECT * FROM states WHERE name='Louisiana'")
            new_state = self.cursor.fetchone()
            self.assertIsNotNone(new_state)
            self.assertEqual(new_state[1], "Louisiana")


if __name__ == '__main__':
    unittest.main()
