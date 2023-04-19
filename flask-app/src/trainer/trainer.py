from flask import Blueprint, request, jsonify, make_response, current_app
import json
import random
from src import db

trainer = Blueprint('trainer', __name__)

@trainer.route('/hireTrainer', methods=['POST'])
def hire_new_trainer():
     the_data = request.json
     current_app.logger.info(the_data)
     rate=the_data['rate']
     specialty=the_data['specialty']
     TrainerName=the_data['TrainerName']

     # make a new trainerID
     cursor = db.get_db().cursor()
     cursor.execute(
        '''select trainerID from Trainers''')
     json_data = []
     theData = cursor.fetchall()
     for row in theData:
        json_data.append(row[0])
     trainerID = int(max(json_data)) + 1

     # checks to see if a trainername already exists in the database
     cursor = db.get_db().cursor()
     cursor.execute('select TrainerName from Trainers')
     querylist = []
     theData = cursor.fetchall()
     for row in theData:
        querylist.append(row[0])
     if TrainerName in querylist:
        return "Name Already Exists In database Try Adding M.I"
     else:
        query = 'insert into Trainers ( trainerID, rate, specialty, TrainerName) values ("'
        query +=  str(trainerID) + '", ' + str(rate) + ', "' + specialty + '", "'  + TrainerName + '")'
        current_app.logger.info(query)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success! "


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
