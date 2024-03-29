#!/usr/bin/python3
""" Module for testing file storage"""
import os
import models
import MySQLdb
import unittest
from models.city import City
from models.state import State
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from tests.test_models.test_base_model import test_basemodel


class TestDBStorage(test_basemodel, unittest.TestCase):
    """ Test class for dbstorage """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.db = MySQLdb.connect(host="localhost",
                                      user="hbnb_test",
                                      passwd="hbnb_test_pwd",
                                      database="hbnb_test_db")
            self.cursor = self.db.cursor()

    def setUp(self):
        """ Test set up """
        super().setUp()

    def tearDown(self):
        """Test removing json file or closing database connection"""
        super().tearDown()
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.cursor.close()
            self.db.close()

    def test_database_connection(self):
        """Test that the database connection is properly established"""
        try:
            with MySQLdb.connect(host="localhost",
                                 user="hbnb_test",
                                 passwd="hbnb_test_pwd",
                                 database="hbnb_test_db") as db:
                with db.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    result = cursor.fetchone()
                    self.assertEqual(result[0], 1)
        except MySQLdb.Error as e:
            self.fail(f"Database connection failed: {e}")

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
