from sqlalchemy import Column, Integer, String, DateTime
import datetime
from base import Base


class TeamMember(Base):

    __tablename__ = 'canucks'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    position = Column(String(100), nullable=False)
    type = Column(String(10), nullable=False)

    def __init__(self, first_name, last_name, date_of_birth, position, type):
        """Constructs all variables and test their values"""
        self._validate_string_input("first name", first_name)
        self.first_name = first_name

        self._validate_string_input("last name", last_name)
        self.last_name = last_name

        date_of_birth = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
        self._validate_datetime("date of birth", date_of_birth)
        self.date_of_birth = date_of_birth

        self._validate_string_input("position", position)
        self.position = position

        self.type = type

    def get_age(self):
        """Calculate the age of the team member using today's date"""
        today = datetime.datetime.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def to__dict(self):
        """returns a dictionary representation of team member"""
        raise NotImplementedError("Subclass implements this method")

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """Private helper to validate string values"""

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty")

        if type(str_value) != str:
            raise ValueError(display_name + " must be a string")

    @staticmethod
    def _validate_int(display_name, input_value):
        """Private method to validate the input value is a int type"""

        if input_value != int(input_value):
            raise ValueError(display_name + " must be a integer type")

    @staticmethod
    def _validate_datetime(display_name, input_value):
        """Private method to validate the input value is a datetime type"""

        if type(input_value) is None:
            raise ValueError(display_name + " cannot be undefined")

        if type(input_value) == "":
            raise ValueError(display_name + " cannot be empty")

        if type(input_value) != datetime.datetime:
            raise ValueError(display_name + " must be a datetime type")
