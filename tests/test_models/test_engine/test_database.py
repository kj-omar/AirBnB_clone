#!/usr/bin/python3
""" Module for testing Mysql database"""
import unittest
import MySQLdb
from console import HBNBCommand  # Assuming the console command is implemented in a file called console.py



class TestMySQLStorage(unittest.TestCase):

    def setUp(self):
        """Set up database connection and create cursor"""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close the database connection"""
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        """Test creating a State record in MySQL"""
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        HBNBCommand().onecmd('create State name="California"')

        self.cursor.execute("SELECT COUNT(*) FROM states;")
        new_count = self.cursor.fetchone()[0]

        self.assertEqual(new_count, initial_count + 1)
