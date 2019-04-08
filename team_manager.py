import json
import os
from player import Player
from staff import Staff


class TeamManager:
    def __init__(self, filepath):
        """class constructor"""
        self._entities = []
        exists = os.path.isfile('{}.json'.format(filepath))
        if not exists:
            file = open("{}.json".format(filepath), "w+")
            file.write('[]')
            file.close()
        self._filepath = filepath
        self._read_members_from_file()

    def _read_members_from_file(self):
        """open and reads json file"""
        file = open("{}.json".format(self._filepath), "r")
        content = file.read()
        member_dict = json.loads(content)
        for member in member_dict:
            if member['type'] == 'player':
                team_member = Player(member['first_name'], member['last_name'], member['date_of_birth'], member['position'],
                       member['height'], member['weight'], member['player_number'], member['shoot'])
                team_member.set_id(member['id'])
            elif member['type'] == 'staff':
                team_member = Staff(member['first_name'], member['last_name'], member['date_of_birth'], member['position'],
                                    member['hire_date'])
                for team in member['previous_team']:
                    team_member.add_previous_team(team)
                    team_member.set_id(member['id'])
            self.add(team_member)
        file.close()

    def _write_members_to_file(self):
        """opens and writes to json file"""
        team_list = []
        file = open("{}.json".format(self._filepath), "w+")
        for team_member in self._entities:
            team_list.append(team_member.to_dict())
        json_string = json.dumps(team_list)
        file.write(json_string)
        file.close()

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


