from sqlalchemy import Column, Integer, String, Float
from team_member import TeamMember


class Player(TeamMember):

    TYPE = 'player'

    height = Column(Float)
    weight = Column(Float)
    player_number = Column(Integer)
    shoot = Column(String(1))

    def __init__(self, first_name, last_name, date_of_birth, position, height, weight, player_number, shoot, type):
        """Constructs player's height, weight, player number and direction they shoot and validates inputs are valid"""
        super().__init__(first_name, last_name, date_of_birth, position, type)
        self._validate_float("height", height)
        self.height = height

        self._validate_float("weight", weight)
        self.weight = weight

        self._validate_int("player number", player_number)
        self.player_number = player_number

        self._validate_shoot(shoot)
        self.shoot = shoot


    # def get_height(self):
    #     """Returns height of player in feet"""
    #     return self._height
    #
    # def get_weight(self):
    #     """Returns weight of player in pounds"""
    #     return self._weight
    #
    # def get_number(self):
    #     """Returns player jersey number for player"""
    #     return self._player_number
    #
    # def get_shoot(self):
    #     """Returns which hand player shoot"""
    #     return self._shoot
    #
    # def get_type(self):
    #     """returns object under player class"""
    #     return Player.TYPE

    def to_dict(self):
        """returns a dictionary representation of player"""
        dict = {}
        dict['id'] = self.id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['date_of_birth'] = self.date_of_birth.strftime("%d/%m/%Y")
        dict['position'] = self.position
        dict['height'] = self.height
        dict['weight'] = self.weight
        dict['player_number'] = self.player_number
        dict['shoot'] = self.shoot
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


