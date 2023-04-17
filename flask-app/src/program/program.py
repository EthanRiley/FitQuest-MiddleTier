from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

program = Blueprint('program', __name__)

@program.route('/programs', methods=['GET'])
def get_programs():
    query = '''
        SELECT ProgramDescription FROM Programs
    '''
    cursor = db.get_db().cursor()

    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@program.route('/program', methods=['POST'])
def add_program():
    pass

@program.route('/program/{programID}', methods=['GET'])
def get_program(programID):
    query = f'SELECT {programID} FROM Programs'
    cursor = db.get_db().cursor()

    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@program.route('/program/{programID}/{numDay}')
def get_program_day(programID, numDay):
    # Returns workout pattern for a given day
    query = f'''
    SELECT Pattern 
    FROM Programs JOIN ProgramDetails on Programs.ProgramID
    WHERE {programID} = ProgramDetails.ProgramID AND {numDay} = ProgramDetails.numDay'''
    cursor = db.get_db().cursor()

    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@program.route('program/{type}/{userID}', methods=['GET'])
def get_program(type, userID):
    pass