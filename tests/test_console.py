#!/usr/bin/python3
"""
Unittest module for the console.
"""
import unittest

import unittest
from console import HBNBCommand
from models import storage
from models.user import User
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.backup = sys.stdout
        self.get_output = StringIO()
        sys.stdout = self.get_output

    def tearDown(self):
        sys.stdout = self.backup

    def test_create(self):
        HBNBCommand().onecmd('create User email="user@example.com" password="pwd"')
        self.assertIn('User', storage.all().keys())