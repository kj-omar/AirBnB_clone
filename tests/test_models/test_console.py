import unittest
from console import HBNBCommand


class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_state(self):
        output = self.console.onecmd('create State name="California"')
        self.assertTrue('-' in output)  # Assuming UUID is returned

        # Add assertions to check if the State object is created correctly

    def test_create_place(self):
        output = self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms4
                number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        self.assertTrue('-' in output)  # Assuming UUID is returned

        # Add assertions to check if the Place object is created correctly


if __name__ == '__main__':
    unittest.main()
