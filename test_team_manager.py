from unittest import TestCase
from player import Player
from staff import Staff
from team_manager import TeamManager
import inspect
import json
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open


class TestTeamManager(TestCase):

    MOCK_JSON = []

    @patch('builtins.open', mock_open(read_data=''))
    def setUp(self):
        """Set up the canucks class for test"""
        json.loads = MagicMock(return_value=[])
        horvat = Player("Bo", "Horvat", '5/4/1995', "C", 6.0, 215, 53, 'L')
        hay = Player("Hay", "Beagle", "16/10/1985", "RW/C", 7.0, 200, 27, 'R')
        alex = Player("Alex", "Biega", "4/4/1988", "D", 2.0, 300, 17, 'R')
        jim = Staff("Jim", "Benning", "29/4/1963", "General Manager", "23/05/2014")
        self.canucks = TeamManager(None)
        self.canucks.add(horvat)
        self.canucks.add(hay)
        self.canucks.add(alex)
        self.canucks.add(jim)
        self.logPoint()

    def logPoint(self):
        """utility function used for module functions and class methods"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    @patch('builtins.open', mock_open(read_data=''))
    def test_read_members_from_file(self):
        """Test to see JSON file is being read"""
        self.assertEqual(len(self.canucks.get_all()), 4)

    @patch('builtins.open', mock_open(read_data=''))
    def test_write_members_to_file(self):
        """Test to see object is being written into JSON file"""
        john = Player("John", "Bill", "16/12/1975", "RL/C", 6.8, 180, 25, 'L')
        self.canucks.add(john)
        self.canucks._write_members_to_file()
        self.assertEqual(len(self.canucks.get_all()), 5)

    def test_add(self):
        """Test if it's adding correctly and test if it raises a error in case it's provided the wrong type"""
        john = Staff("John", "Weisbrod", "8/11/1968", "Assistant General Manager", "23/05/2014")
        self.canucks.add(john)
        self.assertEqual(len(self.canucks.get_all()), 5, "Error in add function")
        with self.assertRaises(AttributeError):
            self.canucks.add("Not object test")

    def test_get(self):
        """Test if it return the correct object and if returns none in case wrong ID is provided"""
        hay = self.canucks.get(2)
        self.assertEqual(hay.get_first_name(), "Alex")
        self.assertEqual(self.canucks.get(999), None)

    def test_get_all(self):
        """Test if return the full list"""
        self.assertEqual(len(self.canucks.get_all()), 4)

    def test_get_all_by_type(self):
        """Test if returns the proper types and if it return empty list in case the wrong type is provided"""
        self.assertEqual(len(self.canucks.get_all_by_type("player")), 3)
        self.assertEqual(len(self.canucks.get_all_by_type("staff")), 1)
        self.assertEqual(self.canucks.get_all_by_type("NotExistingType"), [])

    def test_delete(self):
        """Tests if correctly deletes the object and if it raises an error in case non existent ID is provided"""
        self.canucks.delete(3)
        self.assertEqual(len(self.canucks.get_all()), 3)
        with self.assertRaises(ValueError):
            self.canucks.delete(786)

    def test_update(self):
        """Tests if it updates the object correctly and tests if returns a error if ID does not exist"""
        new_hay = Player("Hay", "Beagles", "16/10/1985", "RW/C", 7.0, 200, 27, 'R')
        new_hay.set_id(1)
        self.canucks.update(new_hay)
        obj = self.canucks.get(1)
        self.assertEqual(obj.get_last_name(), "Beagles")
        self.assertEqual(len(self.canucks.get_all()), 4)

        new_player = Player("Haay", "Beaglees", "16/10/1985", "RW/C", 7.0, 200, 27, 'R')
        new_player.set_id(55)
        with self.assertRaises(ValueError):
            self.canucks.update(new_player)

