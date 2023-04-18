from flask import Blueprint, request, jsonify, make_response, current_app
import json
import random
from src import db

trainer = Blueprint('trainer', __name__)

@trainer.route('/hireTrainer', methods=['POST'])
def hire_new_trainer():
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

