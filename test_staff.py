from unittest import TestCase
from staff import Staff
import datetime
import inspect


class TestStaff(TestCase):

    def setUp(self):
        """validates Satff object input"""
        self.staff = Staff("Jim", "Benning", "1/2/1945", "General Manager", "01/07/2015")
        self.logPoint()

    def logPoint(self):
        """utility function used for module functions and class methods"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_arguments(self):
        """test constructor for empty or undefined or non string parameters"""
        self.assertRaisesRegex(ValueError, 'first name cannot be undefined', Staff, None, None, None, None, None)
        self.assertRaisesRegex(ValueError, 'first name cannot be empty', Staff, "", "", "", "", "")
        self.assertRaisesRegex(ValueError, 'first name must be a string', Staff, 1, 1, 1, 1, 1)

        self.assertRaisesRegex(ValueError, 'last name cannot be undefined', Staff, "Jim", None, None, None, None)
        self.assertRaisesRegex(ValueError, 'last name cannot be empty', Staff, "Jim", "", "", "", "")
        self.assertRaisesRegex(ValueError, 'last name must be a string', Staff, "Jim", 1, 1, 1, 1)

        #constructor argument for date time not created, as function already validates when converting to datetime.


        self.assertRaisesRegex(ValueError, 'position cannot be undefined', Staff, "Jim", "Benning", "1/2/1945", None, None)
        self.assertRaisesRegex(ValueError, 'position cannot be empty', Staff, "Jim", "Benning", "1/2/1945", "", "")
        self.assertRaisesRegex(ValueError, 'position must be a string', Staff, "Jim", "Benning", "1/2/1945", 1, 1)


    def test_get_first_name(self):
        """validates first name input"""
        self.assertEqual(self.staff.get_first_name(), "Jim")

    def test_get_last_name(self):
        """validates last name input"""
        self.assertEqual(self.staff.get_last_name(), "Benning")

    def test_get_date_of_birth(self):
        """validates day, month, year in date of birth"""
        dob = self.staff.get_date_of_birth()
        self.assertEqual(dob.year, 1945)
        self.assertEqual(dob.month, 2)
        self.assertEqual(dob.day, 1)

    def test_get_age(self):
        """gets today's date, checks current year and and subtract from DOB year and subjects the greater of date of month and date"""
        dob = self.staff.get_date_of_birth()
        today = datetime.datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        self.assertEqual(age, self.staff.get_age())

    def test_get_position(self):
        """validates player's position"""
        self.assertEqual(self.staff.get_position(), 'General Manager')

    def test_get_id(self):
        """validates staff's position"""
        self.assertEqual(self.staff.get_id(), 0)
        self.staff.set_id(5)
        self.assertEqual(self.staff.get_id(), 5)

    def test_get_previous_team(self):
        """validates staff's previous team affiliations if any"""
        self.assertEqual(self.staff.get_previous_team(), "Not worked on previous team before")
        self.staff.add_previous_team("Boston Bruins")
        self.assertEqual(self.staff.get_previous_team(), ["Boston Bruins"])

    def test_add_previous_team(self):
        """validates prevous team affiliations"""
        self.assertEqual(self.staff.add_previous_team('Boston Bruins'), 'Boston Bruins team added to previous teams list')

    def test_get_length_of_tenure(self):
        """gets length of tensure from today's date from date of hire"""
        tenure = self.staff.get_hire_date()
        today = datetime.datetime.today()
        length = today.year - tenure.year - ((today.month, today.day) < (tenure.month, tenure.day))
        self.assertEqual(length, self.staff.get_length_of_tenure())

    def test_get_hire_date(self):
        """"validates hiring date, month, year"""
        hire = self.staff.get_hire_date()
        self.assertEqual(hire.year, 2015)
        self.assertEqual(hire.month, 7)
        self.assertEqual(hire.day, 1)

    def test_get_type(self):
        """validates staff member is staff under the staff subclass"""
        self.assertEqual(self.staff.get_type(), "staff")