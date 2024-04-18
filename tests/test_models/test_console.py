import unittest
from unittest.mock import patch
import io
import sys
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the console module"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        self.console.stdout = io.StringIO()

    def tearDown(self):
        """Restore standard input and output"""
        sys.stdout = sys.__stdout__

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        self.console.onecmd("create BaseModel")
        self.assertTrue(len(mock_stdout.getvalue().strip()) == 36)
        self.assertTrue(len(storage.all()) == 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn(obj_id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"destroy BaseModel {obj_id}")
        self.assertFalse(storage.all())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("all")
        self.assertIn("[BaseModel]", mock_stdout.getvalue())

