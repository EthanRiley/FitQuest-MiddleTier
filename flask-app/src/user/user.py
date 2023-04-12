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
     query = 'insert into Users ( username, userpassword, contact, userID) values ("'
     query +=  username + '", "' +userpassword + '", "' + contact + '", '  + userID+ ')'
     current_app.logger.info(query)
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses"