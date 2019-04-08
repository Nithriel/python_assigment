from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from player import Player
from staff import Staff
from team_member import TeamMember

STAFF_TYPE = "staff"
PLAYER_TYPE = "player"


class TeamManager:
    def __init__(self, db_filename):
        """class constructor"""
        if db_filename is None or db_filename == "":
            raise ValueError("Invalid Database File")

        engine = create_engine('sqlite:///' + db_filename)

        # Bind the engine to the metadata of the Base class so that the
        # declarative can be accessed through a DBSession instance
        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)

    def add(self, object):
        """Add the object to the list of objects and assign it a unique ID"""
        gen_id = 0
        list_of_id = [i.get_id() for i in self._entities]
        for i in list_of_id:
            if gen_id in list_of_id:
                gen_id = gen_id + 1
        object.set_id(gen_id)
        self._entities.append(object)
        self._write_members_to_file()
        return gen_id

    def get(self, get_id):
        """Return a object that matches the provided ID, in case no ID matches return None"""
        for object in self._entities:
            if object.get_id() == int(get_id):
                return object
        return None

    def get_all(self):
        """Return the list of objects"""
        return self._entities

    def get_all_by_type(self, type):
        """Return a list of objects that matches the provided type"""
        type_list = []
        for object in self._entities:
            if object.get_type() == type:
                type_list.append(object)
        return type_list

    def delete(self, delete_id):
        """Remove the object that contains the provided ID, in case the ID does not exist, it raises a NameError"""
        list_of_id = [i.get_id() for i in self._entities]
        if delete_id in list_of_id:
            for object in self._entities:
                if object.get_id() == delete_id:
                    self._entities.remove(object)
                    self._write_members_to_file()
        else:
            raise ValueError

    def team_member_exist(self, id):
        """checks if team member already exists based on ID"""
        list_of_id = [i.get_id() for i in self._entities]
        if int(id) in list_of_id:
            return True
        else:
            return False

    def update(self, new_obj):
        """Substitute the object in the list in case they have the same ID, if it does not, it raises a NameError"""
        list_of_id = [i.get_id() for i in self._entities]
        new_id = new_obj.get_id()
        if new_id in list_of_id:
            for obj in self._entities:
                if obj.get_id() == new_id:
                    self.delete(obj.get_id())
                    self._entities.append(new_obj)
                    self._write_members_to_file()
        else:
            raise ValueError

    @classmethod
    def _validate_object_input(cls, display_name, obj_value):
        """helper to validate object values"""

        if obj_value is None:
            raise ValueError(display_name + " must be defined")


