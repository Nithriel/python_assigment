import datetime

class TeamMember:
    def __init__(self, first_name, last_name, date_of_birth, position):
        """Constructs all variables and test their values"""
        self._id = 0

        self._validate_string_input("first name", first_name)
        self._first_name = first_name

        self._validate_string_input("last name", last_name)
        self._last_name = last_name

        date_of_birth = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
        self._validate_datetime("date of birth", date_of_birth)
        self._date_of_birth = date_of_birth

        self._validate_string_input("position", position)
        self._position = position

    def get_first_name(self):
        """returns first name of team member"""
        return self._first_name

    def get_last_name(self):
        """returns last name of team member"""
        return self._last_name

    def get_date_of_birth(self):
        """returns date of birth of team member"""
        return self._date_of_birth

    def get_age(self):
        """Calculate the age of the team member using today's date"""
        today = datetime.datetime.today()
        age = today.year - self._date_of_birth.year - ((today.month, today.day) < (self._date_of_birth.month, self._date_of_birth.day))
        return age

    def get_position(self):
        """gets position of team member"""
        return self._position

    def get_id(self):
        """"get Id number for team member"""
        return self._id

    def get_type(self):
        """get type of team member"""
        raise NotImplementedError('Function implemented in the child')

    def set_id(self, new_id):
        """set id for team member"""
        self._validate_int("id", new_id)
        self._id = new_id

    def to__dict(self):
        """returns a dictionary representation of team member"""
        dict = {}
        dict['id'] = self.get_id()
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['date_of_birth'] = self._date_of_birth.strftime("%d/%m/%Y")
        dict['position'] = self._position
        return dict

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