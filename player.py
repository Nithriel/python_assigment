from team_member import TeamMember


class Player(TeamMember):

    TYPE = 'player'
    def __init__(self, first_name, last_name, date_of_birth, position, height, weight, player_number, shoot):
        """Constructs player's height, weight, player number and direction they shoot and validates inputs are valid"""
        super().__init__(first_name, last_name, date_of_birth, position)
        self._validate_float("height", height)
        self._height = height

        self._validate_float("weight", weight)
        self._weight = weight

        self._validate_int("player number", player_number)
        self._player_number = player_number

        self._validate_shoot(shoot)
        self._shoot = shoot

    def get_height(self):
        """Returns height of player in feet"""
        return self._height

    def get_weight(self):
        """Returns weight of player in pounds"""
        return self._weight

    def get_number(self):
        """Returns player jersey number for player"""
        return self._player_number

    def get_shoot(self):
        """Returns which hand player shoot"""
        return self._shoot

    def get_type(self):
        """returns object under player class"""
        return Player.TYPE

    def to_dict(self):
        """returns a dictionary representation of player"""
        dict = {}
        dict['id'] = self.get_id()
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['date_of_birth'] = self._date_of_birth.strftime("%d/%m/%Y")
        dict['position'] = self._position
        dict['height'] = self._height
        dict['weight'] = self._weight
        dict['player_number'] = self._player_number
        dict['shoot'] = self._shoot
        dict['type'] = Player.TYPE
        return dict

    @staticmethod
    def _validate_shoot(shoot):
        """Private method to validate which direction player shoot"""
        if not (shoot == "L" or shoot == "R"):
            raise Exception("Shoot option not valid")

    @staticmethod
    def _validate_float(display_name, input_value):
        """Private method to validate the input is a float"""
        if input_value is None:
            raise ValueError(display_name + " cannot be undefined")
        if input_value == "":
            raise ValueError(display_name + " cannot be empty")
        if input_value != float(input_value):
            raise ValueError(display_name + " must be a float")

    @staticmethod
    def _validate_int(display_name, input_value):
        """Private method to validate the input is a int"""
        if input_value is None:
            raise ValueError(display_name + " cannot be undefined")
        if input_value == "":
            raise ValueError(display_name + " cannot be empty")
        if input_value != int(input_value):
            raise ValueError(display_name + " must be an integer")


