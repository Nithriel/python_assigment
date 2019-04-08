from sqlalchemy import Column, String
from team_member import TeamMember
import datetime


class Staff(TeamMember):

    TYPE = 'staff'

    hire_date = Column(String(10))
    previous_team = Column(String(250))

    def __init__(self, first_name, last_name, date_of_birth, position, hire_date, previous_team, type):
        """Constructs staff's previous team history as list if available and validates hire date is datetime"""
        super().__init__(first_name, last_name, date_of_birth, position, type)
        self.previous_team = previous_team

        hire_date = datetime.datetime.strptime(hire_date, "%d/%m/%Y")

        self._validate_datetime("hire_date", hire_date)
        self.hire_date = hire_date


    # def get_previous_team(self):
    #     """checks if staff has worked on previous teams and return list"""
    #     if len(self._previous_team) == 0:
    #         return "Not worked on previous team before"
    #     else:
    #         return self._previous_team
    #
    # def add_previous_team(self, team_name):
    #     """add previous team to list"""
    #     self._validate_string("team name", team_name)
    #     self._previous_team.append(team_name)
    #     return "{} team added to previous teams list".format(team_name)
    #
    # def get_hire_date(self):
    #     """return the hire date of when staff joined the team"""
    #     return self._hire_date

    def get_length_of_tenure(self):
        """return length of tenure based on date of hire to today's date"""
        today = datetime.datetime.today()
        tenure = today.year - self.hire_date.year - (
                    (today.month, today.day) < (self.hire_date.month, self.hire_date.day))
        return tenure

    # def get_type(self):
    #     """Returns the type"""
    #     return "staff"

    def to_dict(self):
        """returns a dictionary representation of staff"""
        dict = {}
        dict['id'] = self.id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['date_of_birth'] = self.date_of_birth
        dict['position'] = self.position
        dict['hire_date'] = self.hire_date
        dict['previous_team'] = self.previous_team
        dict['type'] = Staff.TYPE
        return dict

    @staticmethod
    def _validate_string(display_name, input_value):
        """private method to validate input is a string"""

        if input_value != str(input_value):
            raise ValueError(display_name + " must be a string")

    @staticmethod
    def _validate_datetime(display_name, input_value):
        """Private method to validate the input value is a datetime type"""

        if type(input_value) != datetime.datetime:
            raise ValueError(display_name + " must be a datetime type")


