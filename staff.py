from team_member import TeamMember
import datetime


class Staff(TeamMember):

    TYPE = 'staff'

    def __init__(self, first_name, last_name, date_of_birth, position, hire_date):
        """Constructs staff's previous team history as list if available and validates hire date is datetime"""
        super().__init__(first_name, last_name, date_of_birth, position)
        self._previous_team = []

        hire_date = datetime.datetime.strptime(hire_date, "%d/%m/%Y")

        self._validate_datetime("hire_date", hire_date)
        self._hire_date = hire_date

    def get_previous_team(self):
        """checks if staff has worked on previous teams and return list"""
        if len(self._previous_team) == 0:
            return "Not worked on previous team before"
        else:
            return self._previous_team

    def add_previous_team(self, team_name):
        """add previous team to list"""
        self._validate_string("team name", team_name)
        self._previous_team.append(team_name)
        return "{} team added to previous teams list".format(team_name)

    def get_hire_date(self):
        """return the hire date of when staff joined the team"""
        return self._hire_date

    def get_length_of_tenure(self):
        """return length of tenure based on date of hire to today's date"""
        today = datetime.datetime.today()
        tenure = today.year - self._hire_date.year - (
                    (today.month, today.day) < (self._hire_date.month, self._hire_date.day))
        return tenure

    def get_type(self):
        """Returns the type"""
        return "staff"

    def to_dict(self):
        """returns a dictionary representation of staff"""
        dict = {}
        dict['id'] = self.get_id()
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['date_of_birth'] = self._date_of_birth.strftime("%d/%m/%Y")
        dict['position'] = self._position
        dict['hire_date'] = self._hire_date.strftime("%d/%m/%Y")
        dict['previous_team'] = self._previous_team
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


