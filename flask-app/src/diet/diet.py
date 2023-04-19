from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

diet = Blueprint('diets', __name__)

@diet.route('/retreiveDiet', methods=['GET'])
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

@diet.route('/graphDiet', methods=['POST'])
def getGraphData():
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    the_data = request.json
    current_app.logger.info(the_data)
    # use cursor to query the database for a list of products
    dietname=the_data['diet_selector_graph']
    #get protein for a diet
    query = 'SELECT totalprotien AS y FROM Diet where dietID = "' + dietname + '"'
    cursor.execute(query)
    protein = []
    theData = cursor.fetchall()
    for row in theData:
        protein.append(row[0])

    # get carbs for a diet
    cursor2 = db.get_db().cursor()
    query = 'SELECT totalcarbs AS y FROM Diet where dietID = "' + dietname + '"'
    cursor2.execute(query)
    carbs = []
    theData = cursor2.fetchall()
    for row in theData:
        carbs.append(row[0])

    #get fat for a diet
    cursor3 = db.get_db().cursor()
    query = 'SELECT totalfat AS y FROM Diet where dietID = "' + dietname + '"'
    cursor3.execute(query)
    fat = []
    theData = cursor3.fetchall()
    for row in theData:
        fat.append(row[0])

    return [{"x":"Total Protein", "y":protein[0]},
            {"x":"Total Carbs", "y":carbs[0]},
            {"x":"Total Fat", "y":fat[0]}]

@diet.route('/dietbreakdown', methods=['GET'])
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

@diet.route('/addToDiet', methods=['POST'])
def add_to_diet():
     the_data = request.json
     current_app.logger.info(the_data)
     carbs=the_data['totalcarbs']
     protein=the_data['totalprotein']
     fat=the_data['totalfat']
     dietname=the_data['dietname']
     userID = the_data['targetUser']

    #check to see if the userID is in the database
     cursor = db.get_db().cursor()
     cursor.execute( '''select userID from Users''')
     json_data = []
     theData = cursor.fetchall()
     for row in theData:
        json_data.append(row[0])
     if userID not in json_data:
         return "User not in Database"


     # make a new dietID
     cursor = db.get_db().cursor()
     cursor.execute(
        '''select dietID from Diet''')
     json_data = []
     theData = cursor.fetchall()
     for row in theData:
        json_data.append(row[0])
     dietID = int(max(json_data)) + 1

     query = 'insert into Diet (totalcarbs, totalprotien, totalfat, dietname, dietID, userID) values ("'
     query += carbs + '", "' + protein + '", "' + fat  + '", "' + dietname + '", "' + str(dietID) + '", "'
     query += userID + '")'
     current_app.logger.info(query)
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses"

@diet.route('/updateDiet', methods=['PUT'])
def updateDiet():
     the_data = request.json
     current_app.logger.info(the_data)
     newcarbs=the_data['updateCarbs']
     newfat = the_data['updateFat']
     newprotein = the_data['updateProtein']
     dname = the_data['DietPicker']
     
     cursor = db.get_db().cursor()
     cursor.execute(
        '''select dietID from Diet''')
     existingUsers = []
     theData = cursor.fetchall()
     for row in theData:
        existingUsers.append(row[0])
     if dname not in existingUsers:
         return "User not in Database"
     
    
     query = 'UPDATE Diet set totalcarbs = "' + str(newcarbs) + '", totalfat = "' + str(newfat)
     query += '", totalprotien = "' + str(newprotein) + '" where dietname = "' + dname + '"'
     current_app.logger.info(query)
     
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()
     return "sucesses"

@diet.route('/equipment', methods=['GET', 'POST', 'PUT', 'DELETE'])
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

@diet.route('/deletediet', methods=['DELETE'])
def deldiet():
    try:
        the_data = request.json
        current_app.logger.info(the_data)
        delete=the_data['todelete']
        query = 'Delete from Diet where dietID = "' + delete + '"'
        current_app.logger.info(query)
            
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "sucesses"
    except:
        return "not in database"