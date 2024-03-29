#!/usr/bin/python3
""" Module for testing file storage"""
import os
import MySQLdb
import unittest
from models.city import City
from models.state import State
from unittest.mock import patch, MagicMock
from models.engine.db_storage import DBStorage
from tests.test_models.test_base_model import test_basemodel


class TestDBStorage(test_basemodel, unittest.TestCase):
    """ Test class for dbstorage """

    def setUp(self):
        """ Test set up """
        super().setUp()
        if os.getenv('HBNB_ENV') == 'test' and os.getenv(
                'HBNB_TYPE_STORAGE') == 'db':
            self.db = MySQLdb.connect(host="localhost",
                                      user="hbnb_test",
                                      passwd="hbnb_test_pwd",
                                      database="hbnb_test_db")
            self.cursor = self.db.cursor()

    def tearDown(self):
        """Test removing json file or closing database connection"""
        super().tearDown()
        if os.getenv('HBNB_ENV') == 'test' and os.getenv(
                'HBNB_TYPE_STORAGE') == 'db':
            self.cursor.close()
            self.db.close()

    @patch('models.engine.db_storage.DBStorage.all')
    def test_all_method(self, mock_all):
        mock_all.return_value = {
            'State.1': State(id='1', name='California'),
            'City.1': City(id='1', name='Los Angeles', state_id='1')
        }

        storage = DBStorage()
        all_objects = storage.all()

        self.assertIn('State.1', all_objects)
        self.assertIn('City.1', all_objects)
        self.assertIsInstance(all_objects['State.1'], State)
        self.assertIsInstance(all_objects['City.1'], City)

    @patch('models.engine.db_storage.DBStorage._DBStorage__session',
           new_callable=MagicMock)
    def test_new_method(self, mock_session):
        """Test the new() method"""
        new_state = State(name="New York")
        storage = DBStorage()
        storage.new(new_state)
        mock_session.add.assert_called_with(new_state)

    @patch('models.engine.db_storage.DBStorage._DBStorage__session',
           new_callable=MagicMock)
    def test_save_method(self, mock_session):
        """Test the save() method"""
        new_state = State(name="Florida")
        storage = DBStorage()
        storage.new(new_state)
        storage.save()
        mock_session.commit.assert_called_once()

    @patch('models.engine.db_storage.DBStorage._DBStorage__session',
           new_callable=MagicMock)
    def test_delete_method(self, mock_session):
        """Test the delete() method"""
        state_to_delete = State(name="Texas")
        storage = DBStorage()
        storage.new(state_to_delete)
        storage.delete(state_to_delete)
        mock_session.delete.assert_called_with(state_to_delete)
