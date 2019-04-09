from unittest import TestCase
from player import Player
from staff import Staff
from team_manager import TeamManager
import inspect
import os
import datetime

from sqlalchemy import create_engine
from base import Base


class TestTeamManager(TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///test_team_member.sqlite')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.team_mgr = TeamManager('test_team_member.sqlite')

        self.logPoint()

    def tearDown(self):
        os.remove('test_team_member.sqlite')
        self.logPoint()

    def logPoint(self):
        """utility function used for module functions and class methods"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_add(self):
        """Test if it's adding correctly and test if it raises a error in case it's provided the wrong type"""
        team1 = Player("Bo", "Horvat", "12/02/2000", "C", 6.0, 215, 53, "L", "player")
        team2 = Staff("Jim", "Benning", "1/2/1945", "General Manager", "01/07/2015", "Boston Bruins", "staff")

        self.team_mgr.add(team1)
        self.team_mgr.add(team2)

        team_list = self.team_mgr.get_all()
        print(team_list)
        self.assertEqual(len(team_list), 2)

    def test_add_invalid(self):
        """test invalid inputs in add team member"""
        self.assertRaisesRegex(ValueError, 'Invalid Team Member Object', self.team_mgr.add, None)
        self.assertRaisesRegex(ValueError, 'Invalid Team Member Object', self.team_mgr.add, [])

    def test_update(self):
        """test update team member"""

        team1 = Player("Bo", "Horvat", "12/02/2000", "C", 6.0, 215, 53, "L", "player")
        team1_id = self.team_mgr.add(team1)

        datetime_format = datetime.datetime.strptime("12/02/2000", "%d/%m/%Y")
        retrieve_updated_team = self.team_mgr.get(team1_id)
        self.assertEqual(retrieve_updated_team.first_name, "Bo")
        self.assertEqual(retrieve_updated_team.last_name, "Horvat")
        self.assertEqual(retrieve_updated_team.date_of_birth, datetime_format)
        self.assertEqual(retrieve_updated_team.position, "C")
        self.assertEqual(retrieve_updated_team.height, 6.0)
        self.assertEqual(retrieve_updated_team.weight, 215)
        self.assertEqual(retrieve_updated_team.player_number, 53)
        self.assertEqual(retrieve_updated_team.shoot, "L")
        self.assertEqual(retrieve_updated_team.type, "player")

        datetime_format = datetime.datetime.strptime("12/02/2000", "%d/%m/%Y")
        retrieve_updated_team.first_name = "Bo"
        retrieve_updated_team.last_name = "Horvat"
        retrieve_updated_team.date_of_birth = datetime_format
        retrieve_updated_team.position = "C/LW"
        retrieve_updated_team.height = 6.1
        retrieve_updated_team.weight = 220
        retrieve_updated_team.player_number = 53
        retrieve_updated_team.shoot = "L"
        retrieve_updated_team.type = "player"
        self.team_mgr.update(retrieve_updated_team)

        retrieve_updated_team = self.team_mgr.get(team1_id)
        self.assertEqual(retrieve_updated_team.first_name, "Bo")
        self.assertEqual(retrieve_updated_team.last_name, "Horvat")
        self.assertEqual(retrieve_updated_team.date_of_birth, datetime_format)
        self.assertEqual(retrieve_updated_team.position, "C/LW")
        self.assertEqual(retrieve_updated_team.height, 6.1)
        self.assertEqual(retrieve_updated_team.weight, 220)
        self.assertEqual(retrieve_updated_team.player_number, 53)
        self.assertEqual(retrieve_updated_team.shoot, "L")
        self.assertEqual(retrieve_updated_team.type, "player")

    def test_update_invalid(self):
        """test invalid input for update_student"""
        self.assertRaisesRegex(ValueError, "Invalid Team Member Object", self.team_mgr.update, None)
        self.assertRaisesRegex(ValueError, "Invalid Team Member Object", self.team_mgr.update, [])

    def test_delete(self):
        """test delete team member"""
        team1 = Player("Bo", "Horvat", "12/02/2000", "C", 6.0, 215, 53, "L", "player")
        team1_id = self.team_mgr.add(team1)

        retrieved_team = self.team_mgr.get(team1_id)
        self.assertIsNotNone(retrieved_team)

        self.team_mgr.delete(team1_id)

        retrieved_team = self.team_mgr.get(team1_id)
        self.assertIsNone(retrieved_team)

    def test_delete_invalid(self):
        """test invalid input for update_student"""
        self.assertRaisesRegex(ValueError, "Invalid Team Member ID", self.team_mgr.delete, None)
        self.assertRaisesRegex(ValueError, "Invalid Team Member ID", self.team_mgr.delete, [])

    def test_get(self):
        """test get team member"""
        team1 = Player("Bo", "Horvat", "12/02/2000", "C", 6.0, 215, 53, "L", "player")
        team2 = Staff("Jim", "Benning", "1/2/1945", "General Manager", "01/07/2015", "Boston Bruins", "staff")

        team1_id = self.team_mgr.add(team1)
        team2_id = self.team_mgr.add(team2)

        datetime_format1 = datetime.datetime.strptime("12/02/2000", "%d/%m/%Y")

        retrieve_team1 = self.team_mgr.get(team1_id)
        self.assertIsNotNone(retrieve_team1)
        self.assertEqual(retrieve_team1.first_name, "Bo")
        self.assertEqual(retrieve_team1.last_name, "Horvat")
        self.assertEqual(retrieve_team1.date_of_birth, datetime_format1)
        self.assertEqual(retrieve_team1.position, "C")
        self.assertEqual(retrieve_team1.height, 6.0)
        self.assertEqual(retrieve_team1.weight, 215)
        self.assertEqual(retrieve_team1.player_number, 53)
        self.assertEqual(retrieve_team1.shoot, "L")
        self.assertEqual(retrieve_team1.type, "player")

        datetime_format2 = datetime.datetime.strptime("1/2/1945", "%d/%m/%Y")
        datetime_format3 = datetime.datetime.strptime("01/07/2015", "%d/%m/%Y")

        retrieve_team2 = self.team_mgr.get(team2_id)
        self.assertIsNotNone(retrieve_team2)
        self.assertEqual(retrieve_team2.first_name, "Jim")
        self.assertEqual(retrieve_team2.last_name, "Benning")
        self.assertEqual(retrieve_team2.date_of_birth, datetime_format2)
        self.assertEqual(retrieve_team2.position, "General Manager")
        self.assertEqual(retrieve_team2.hire_date, datetime_format3)
        self.assertEqual(retrieve_team2.previous_team, "Boston Bruins")
        self.assertEqual(retrieve_team2.type, "staff")

    def test_get_invalid(self):
        """"test invalid input in get_student"""
        self.assertRaisesRegex(ValueError, "Invalid Team Member ID", self.team_mgr.get, None)
        self.assertRaisesRegex(ValueError, "Invalid Team Member ID", self.team_mgr.get, [])

    def test_get_all_by_type(self):
        """test get all by type"""
        team1 = Player("Bo", "Horvat", "12/02/2000", "C", 6.0, 215, 53, "L", "player")

        team1_id = self.team_mgr.add(team1)

        team_all = self.team_mgr.get_all_by_type("player")

        player1 = team_all[0].TYPE

        self.assertEqual(player1, "player")

    def test_get_all(self):
        """test get all"""
        team_all = self.team_mgr.get_all()
        self.assertEqual(len(team_all), 0)

        team1 = Player("Bo", "Horvat", "12/02/2000", "C", 6.0, 215, 53, "L", "player")
        team2 = Staff("Jim", "Benning", "1/2/1945", "General Manager", "01/07/2015", "Boston Bruins", "staff")

        team1_id = self.team_mgr.add(team1)
        team2_id = self.team_mgr.add(team2)

        team_all = self.team_mgr.get_all()
        self.assertEqual(len(team_all), 2)