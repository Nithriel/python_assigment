from unittest import TestCase
from player import Player
import datetime
import inspect


class TestPlayer(TestCase):

    def setUp(self):
        """validates Player object input"""
        self.player = Player("Bo", "Horvat", '5/4/1995', "C", 6.0, 215, 53, 'L')
        self.logPoint()

    def logPoint(self):
        """utility function used for module functions and class methods"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_arguments(self):
        """test constructor for empty or undefined or non string parameters"""
        self.assertRaisesRegex(ValueError, 'first name cannot be undefined', Player, None, None, None, None, None, None,
                               None, None)
        self.assertRaisesRegex(ValueError, 'first name cannot be empty', Player, "", "", "", "", "", "", "", "")
        self.assertRaisesRegex(ValueError, 'first name must be a string', Player, 1, 1, 1, 1, 1, 1, 1, 1)

        self.assertRaisesRegex(ValueError, 'last name cannot be undefined', Player, "Bo", None, None, None, None, None,
                               None, None)
        self.assertRaisesRegex(ValueError, 'last name cannot be empty', Player, "Bo", "", "", "", "", "", "", "")
        self.assertRaisesRegex(ValueError, 'last name must be a string', Player, "Bo", 1, 1, 1, 1, 1, 1, 1)

        #constructor argument for date time not created, as function already validates when converting to datetime.

        self.assertRaisesRegex(ValueError, 'position cannot be undefined', Player, "Bo", "Horvat", '5/4/1995', None,
                               None, None, None, None)
        self.assertRaisesRegex(ValueError, 'position cannot be empty', Player, "Bo", "Horvat", '5/4/1995', "", "", "",
                               "", "")
        self.assertRaisesRegex(ValueError, 'position must be a string', Player, "Bo", "Horvat", '5/4/1995', 1, 1, 1, 1,
                               1)

        self.assertRaisesRegex(ValueError, 'height cannot be undefined', Player, "Bo", "Horvat", '5/4/1995', 'C',
                               None, None, None, None)
        self.assertRaisesRegex(ValueError, 'height cannot be empty', Player, "Bo", "Horvat", '5/4/1995', "C", "", "",
                               "", "")
        self.assertRaisesRegex(ValueError, 'height must be a float', Player, "Bo", "Horvat", '5/4/1995', 'C', '1', 1, 1,
                               1)

        self.assertRaisesRegex(ValueError, 'weight cannot be undefined', Player, "Bo", "Horvat", '5/4/1995', 'C',
                               6.0, None, None, None)
        self.assertRaisesRegex(ValueError, 'weight cannot be empty', Player, "Bo", "Horvat", '5/4/1995', "C", 6.0, "",
                               "", "")
        self.assertRaisesRegex(ValueError, 'weight must be a float', Player, "Bo", "Horvat", '5/4/1995', 'C', 6.0, '1', 1,
                               1)

        self.assertRaisesRegex(ValueError, 'player number cannot be undefined', Player, "Bo", "Horvat", '5/4/1995', 'C',
                               6.0, 215, None, None)
        self.assertRaisesRegex(ValueError, 'player number cannot be empty', Player, "Bo", "Horvat", '5/4/1995', "C",
                               6.0, 215, "", "")
        self.assertRaisesRegex(ValueError, 'player number must be an integer', Player, "Bo", "Horvat", '5/4/1995', 'C',
                               6.0, 215, '1', 1)

        self.assertRaisesRegex(Exception, 'Shoot option not valid', Player, "Bo", "Horvat", '5/4/1995', 'C',
                               6.0, 215, 53, 'Both')

    def test_get_first_name(self):
        """validates first name input"""
        self.assertEqual(self.player.get_first_name(), "Bo")

    def test_get_last_name(self):
        """validates last name input"""
        self.assertEqual(self.player.get_last_name(), "Horvat")

    def test_get_date_of_birth(self):
        """validates day, month, year in date of birth"""
        dob = self.player.get_date_of_birth()
        self.assertEqual(dob.year, 1995)
        self.assertEqual(dob.month, 4)
        self.assertEqual(dob.day, 5)

    def test_get_age(self):
        """gets today's date, checks current year and and subtract from DOB year and subjects the greater of date of month and date"""
        dob = self.player.get_date_of_birth()
        today = datetime.datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        self.assertEqual(age, self.player.get_age())


    def test_get_position(self):
        """validates player's position"""
        self.assertEqual(self.player.get_position(), 'C')

    def test_get_id(self):
        """validates player's ID number"""
        self.assertEqual(self.player.get_id(), 0)
        self.player.set_id(5)
        self.assertEqual(self.player.get_id(), 5)

    def test_get_height(self):
        """validates player's height"""
        self.assertEqual(self.player.get_height(), 6.0)

    def test_get_weight(self):
        """validates player's weight"""
        self.assertEqual(self.player.get_weight(), 215)

    def test_get_number(self):
        """validates player's jersey number"""
        self.assertEqual(self.player.get_number(), 53)

    def test_get_shoot(self):
        """validates which hand player shoots"""
        self.assertEqual(self.player.get_shoot(), 'L')

    def test_get_type(self):
        """validates player is a player under the player subclass"""
        self.assertEqual(self.player.get_type(), 'player')

