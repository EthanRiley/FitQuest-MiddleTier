from flask import Blueprint, request, jsonify, make_response, current_app
import json
import random
from src import db

trainer = Blueprint('trainer', __name__)

@trainer.route('/hireTrainer', methods=['POST'])
def test():
     the_data = request.json
     current_app.logger.info(the_data)
     trainerID=the_data['trainerID']
     rate=the_data['rate']
     specialty=the_data['specialty']
     TrainerName=the_data['TrainerName']
     query = 'insert into Trainers ( trainerID, rate, specialty, TrainerName) values ("'
     query +=  trainerID + '", ' +str(rate) + ', "' + specialty + '", "'  + TrainerName + '")'
     current_app.logger.info(query)
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses added"

@trainer.route('/retreiveDiet', methods=['GET'])
def look_at_diets():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(
        '''SELECT dietname AS label, dietID AS value
            FROM Diet''')

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

@trainer.route('/dietbreakdown', methods=['GET'])
def dbreakdown():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(
        '''select totalprotien, totalcarbs, totalfat from Diet''')

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

@trainer.route('/totalprotein', methods=['GET'])
def totalprotein():
    cursor = db.get_db().cursor()
    cursor.execute(
        '''select totalprotien from Diet''')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@trainer.route('/totalfat', methods=['GET'])
def totalfat():
    cursor = db.get_db().cursor()
    cursor.execute(
        '''select totalfat from Diet''')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@trainer.route('/totalcarbs', methods=['GET'])
def totalcarbs():
    cursor = db.get_db().cursor()
    cursor.execute(
        '''select totalcarbs from Diet''')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@trainer.route('/addToDiet', methods=['POST'])
def add_to_diet():
     the_data = request.json
     current_app.logger.info(the_data)
     carbs=the_data['totalcarbs']
     protein=the_data['totalprotein']
     fat=the_data['totalfat']
     dietname=the_data['dietname']

     # make a new dietID
     cursor = db.get_db().cursor()
     cursor.execute(
        '''select dietID from Diet''')
     column_headers = [x[0] for x in cursor.description]
     json_data = []
     theData = cursor.fetchall()
     for row in theData:
        json_data.append(row[0])
     dietID = int(max(json_data)) + 1

     query = 'insert into Diet (totalcarbs, totalprotien, totalfat, dietname, dietID) values ("'
     query +=  carbs + '", "' + protein + '", "' + fat  + '", "' + dietname + '", "' + str(dietID) + '")'
     current_app.logger.info(query)
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses"

@trainer.route('/updateDiet', methods=['PUT'])
def updateDiet():
     the_data = request.json
     current_app.logger.info(the_data)
     newcarbs=the_data['updateCarbs']
     newfat = the_data['updateFat']
     newprotein = the_data['updateProtein']
     dname = the_data['DietPicker']
     query = 'UPDATE Diet set totalcarbs = "' + str(newcarbs) + '", totalfat = "' + str(newfat)
     query += '", totalprotien = "' + str(newprotein) + '" where dietname = "( SELECT' + dname + '"'
     current_app.logger.info(query)
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses"

@trainer.route('/equipment', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_specefic_equipment():
    if ['GET']:
        cursor = db.get_db().cursor()
        cursor.execute(
            '''select * from Equipment''')
        column_headers = [x[0] for x in cursor.description]
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(column_headers, row)))
        return jsonify(json_data)
    if ['POST']:
        the_data = request.json
        current_app.logger.info(the_data)
        newcarbs=the_data['updateCarbs']
        query = 'UPDATE Diet set totalcarbs = "' + newcarbs + '"'
        current_app.logger.info(query)
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "sucesses"
