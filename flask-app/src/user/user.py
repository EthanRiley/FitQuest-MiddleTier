from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

user = Blueprint('user', __name__)

@user.route('/addUser', methods=['POST'])
def add_new_user():
     the_data = request.json
     current_app.logger.info(the_data)
     username=the_data['username']
     userpassword=the_data['userpassword']
     contact=the_data['contact']
     userID=the_data['userID']
     trainerID = the_data['trainerID']
     query = 'insert into Users ( username, userpassword, contact, userID, trainerID) values ("'
     query +=  username + '", "' +userpassword + '", "' + contact + '", '  + userID+ ', "'  + trainerID + '")'
     current_app.logger.info(query)
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses"

# get all the trainer that is trained by the trainer 
@user.route('/allTrainer', methods=['GET'])
def get_allTrainer():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(
        '''SELECT TrainerName AS label, trainerID AS value
            FROM Trainers''')

    # grab the column headers from the returned data
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

@user.route('/trainer_info', methods=['GET'])
def get_trainer_info():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(
        '''SELECT TrainerName AS Name, specialty, rate
            FROM Trainers''')

    # grab the column headers from the returned data
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