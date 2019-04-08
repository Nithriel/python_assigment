from flask import Flask, request
from player import Player
from team_manager import TeamManager
from staff import Staff
import json
import os

app = Flask(__name__)

CANUCKS_DB = 'canucks.sqlite'
canucks = TeamManager(CANUCKS_DB)

@app.route('/team_manager/employee', methods=['POST'])
def add_member():
    """adds employee object based on type and assigns object an ID number"""
    content = request.json
    try:
        if content['type'] == 'staff':
            staff = Staff(content['first_name'], content['last_name'], content['date_of_birth'],
                              content['position'], content['hire_date'], content['previous_team'], content['type'])
            id = canucks.add(staff)
        elif content['type'] == 'player':
            player = Player(content['first_name'], content['last_name'], content['date_of_birth'],
                               content['position'], float(content['height']), float(content['weight']), int(content['player_number']),
                               content['shoot'], content['type'])

            id = canucks.add(player)
        else:
            raise ValueError

        response = app.response_class(
            response=str(id),
            status=200
        )

    except:
        response = app.response_class(
            response="Input invalid",
            status=400
        )
    return response


@app.route('/team_manager/employee/<id>', methods=['PUT'])
def update_member(id):
    """updates employee object based on their ID"""
    content = request.json
    try:
        id = int(id)
        if canucks.team_member_exist(id):
            if content['type'] == 'staff':
                team_member = Staff(content['first_name'], content['last_name'], content['date_of_birth'],
                                  content['position'], content['hire_date'])
                for team in content['previous_team']:
                    team_member.add_previous_team(team)
                team_member.set_id(id)
                canucks.update(team_member)
            elif content['type'] == 'player':
                team_member = Player(content['first_name'], content['last_name'], content['date_of_birth'],
                               content['position'], float(content['height']), float(content['weight']), int(content['player_number']),
                               content['shoot'])
                team_member.set_id(id)
                canucks.update(team_member)
            response = app.response_class(
                response="OK",
                status=200
            )
        else:
            response = app.response_class(
                response="Team Member does not exist",
                status=404
            )
    except:
        response = app.response_class(
            response="invalid input",
            status=400
        )
    return response


@app.route('/team_manager/employee/<int:id>', methods=['DELETE'])
def delete_member(id):
    """deletes employee object based on their ID"""
    if id <= 0:
        response = app.response_class(
            status=400
        )
        return response

    try:
        canucks.delete(id)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        status_code = 400
        if str(e) == "Team Member does not exist":
            status_code = 404

        response = app.response_class(
            response=str(e),
            status=status_code
        )

    return response


@app.route('/team_manager/employee/<id>', methods=['GET'])
def get(id):
    """returns employee object based on their ID"""
    try:
        id = int(id)
        if canucks.get(id) is None:
            response = app.response_class(
                response="Team Member does not exist",
                status=404
            )
        else:
            team_member = canucks.get(id)
            response =app.response_class(
                response=json.dumps(team_member.to_dict()),
                mimetype='application/json',
                status=200
            )
    except:
        response = app.response_class(
            response="invalid input",
            status=400
        )
    return response


@app.route('/team_manager/employee/all', methods=['GET'])
def get_all():
    """returns all employee objects"""
    response = app.response_class(
        status=200,
        response=json.dumps([team_member.to_dict() for team_member in canucks.get_all()]),
        mimetype='application/json'
    )
    return response


@app.route('/team_manager/employee/all/<type>', methods=['GET'])
def get_all_by_type(type):
    """returns employee object under staff or player type"""
    try:
        if type == 'staff' or type == 'player':
            response = app.response_class(
                status=200,
                response=json.dumps([team_member.to_dict() for team_member in canucks.get_all_by_type(type)]),
                mimetype='application/json'
            )
        else:
            raise ValueError
    except ValueError:
        response = app.response_class(
            status=400,
            response="Type is invalid"
        )
    return response


if __name__ == "__main__":
    app.run()
