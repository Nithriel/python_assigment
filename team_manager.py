from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from player import Player
from staff import Staff
from team_member import TeamMember


class TeamManager:
    STAFF_TYPE = "staff"
    PLAYER_TYPE = "player"

    def __init__(self, db_filename):
        """class constructor"""
        if db_filename is None or db_filename == "":
            raise ValueError("Invalid Database File")
        engine = create_engine('sqlite:///' + db_filename)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add(self, object):
        """adds a new team member"""
        if object is None or not isinstance(object, (Player, Staff)):
            raise ValueError('Invalid Team Member Object')
        session = self._db_session()
        session.add(object)
        session.commit()
        member_id = object.id
        session.close()
        return member_id

    def get(self, id):
        """Return a object that matches the provided ID, in case no ID matches return None"""
        if id is None or type(id) != int:
            raise ValueError("Invalid Team Member ID")
        session = self._db_session()
        existing_team_member = session.query(Player).filter(Player.id == id).filter(Player.type == TeamManager.PLAYER_TYPE).first()
        if existing_team_member is None:
            existing_team_member = session.query(Staff).filter(Staff.id == id).filter(Staff.type == TeamManager.STAFF_TYPE).first()
        session.close()
        return existing_team_member

    def get_all(self):
        """Return the list of objects"""
        team_list = []
        session = self._db_session()
        player_all = session.query(Player).filter(Player.type == "player").all()
        staff_all = session.query(Staff).filter(Staff.type == "staff").all()
        for player in player_all:
            team_list.append(player)
        for staff in staff_all:
            team_list.append(staff)
        session.close()
        return team_list

    def get_all_by_type(self, type):
        """Return a list of objects that matches the provided type"""
        session = self._db_session()
        if type == 'player':
            list = session.query(Player).filter(Player.type == "player").all()
        elif type == 'staff':
            list = session.query(Staff).filter(Staff.type == "staff").all()
        else:
            raise ValueError
        return list

    def delete(self, id):
        """Remove the object that contains the provided ID, in case the ID does not exist, it raises a NameError"""
        if id is None or type(id) != int:
            raise ValueError("Invalid Team Member ID")
        session = self._db_session()
        existing_team_member = session.query(TeamMember).filter(TeamMember.id == id).first()
        if existing_team_member is None:
            raise ValueError("Team Member does not exist")
        session.delete(existing_team_member)
        session.commit()
        session.close()

    def update(self, new_team_member):
        session = self._db_session()
        if new_team_member is None or not isinstance(new_team_member, TeamMember):
            raise ValueError("Invalid Team Member Object")
        elif new_team_member.type == self.PLAYER_TYPE:
            existing_team_member = session.query(Player).filter(Player.id == new_team_member.id).first()
            if existing_team_member is None:
                raise ValueError("Team Member does not exist")
            existing_team_member.first_name = new_team_member.first_name
            existing_team_member.last_name = new_team_member.last_name
            existing_team_member.date_of_birth = new_team_member.date_of_birth
            existing_team_member.position = new_team_member.position
            existing_team_member.height = new_team_member.height
            existing_team_member.weight = new_team_member.weight
            existing_team_member.player_number = new_team_member.player_number

        elif new_team_member.type == self.STAFF_TYPE:
            existing_team_member = session.query(Staff).filter(Staff.id == new_team_member.id).first()
            if existing_team_member is None:
                raise ValueError("Team Member does not exist")
            existing_team_member.first_name = new_team_member.first_name
            existing_team_member.last_name = new_team_member.last_name
            existing_team_member.date_of_birth = new_team_member.date_of_birth
            existing_team_member.position = new_team_member.position
            existing_team_member.hire_date = new_team_member.hire_date
            existing_team_member.previous_team = new_team_member.previous_team
        session.commit()
        session.close()

    @classmethod
    def _validate_object_input(cls, display_name, obj_value):
        """helper to validate object values"""

        if obj_value is None:
            raise ValueError(display_name + " must be defined")


