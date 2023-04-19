from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

# checks to see if a users imput is in the database
def checkin(catname, relname, dname):
    """
    Params: 
    catname: name of column
    relname: name of table
    dname: users input
    """
    cursor = db.get_db().cursor()
    cursor.execute('select ' + catname + ' from ' + relname)
    querylist = []
    theData = cursor.fetchall()
    for row in theData:
        querylist.append(row[0])
    if dname not in querylist:
        return False
    else:
        return dname

user = Blueprint('user', __name__)

@user.route('/addUser', methods=['GET', 'POST'])
def add_new_user():
    if request.method == 'POST':
        the_data = request.json
        current_app.logger.info(the_data)
        username = the_data['username']
        # ensure username is not in the database
        check = checkin("username", "Users", username)
        if check == False:
            username = the_data['username']
        else:
            username += "I"

        userpassword = the_data['userpassword']

        # ensure password is not in the database
        check = checkin("userpassword", "Users", userpassword)
        if check == False:
            userpassword = the_data['userpassword']
        else:
            return "Try New Password "
        contact = the_data['contact']
        
        # make a new userID
        cursor = db.get_db().cursor()
        cursor.execute(
            '''select userID from Users''')
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(row[0])
        userID = int(max(json_data)) + 1


        trainerID = the_data['trainerID']

        query = 'insert into Users (username, userpassword, contact, userID, trainerID) values ("'
        query += username + '", "' + userpassword + '", "' + contact + '", "' + str(userID) + '", "' + trainerID + '")'
        current_app.logger.info(query)

        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "success"
    
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        cursor.execute('''select username as label, userID as value from Users''')
        column_headers = [x[0] for x in cursor.description]
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(column_headers, row)))
        return jsonify(json_data)


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


@user.route('/max/<string:userID>/<string:exerciseID>', methods=['GET', 'PUT'])
def get_max(userID, exerciseID):
    # route for retreiving the existing max from the database
    if request.method == 'GET':
        # get a cursor object from the database
        cursor = db.get_db().cursor()

        # check if user is in the database
        userID = checkin("userID", "Users", userID)
        if userID == False:
            return "userID Not in Database"
        
        # check if exercise is in the database
        exerciseID = checkin("exerciseID", "Exercises", exerciseID)
        if exerciseID == False:
            return "exerciseID Not in Database"

        # use cursor to query the database for a list of products
        cursor.execute(
            f'''SELECT max AS label, exerciseID AS value
                FROM UserExercises
                WHERE userID = {userID} AND exerciseID = {exerciseID}''')

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
    
    # route for adding a max to the database
    if request.method == 'PUT':
        the_data = request.json
        current_app.logger.info(the_data)
        cursor = db.get_db().cursor()

        # use cursor to query the database for a list of products
        cursor.execute(
            f'''SELECT max
                FROM UserExercises
                WHERE userID = {userID} AND exerciseID = {exerciseID}''')
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

        new_max = json_data[0]['max']
        if the_data['check1'] and the_data['check2'] and the_data['check3'] and the_data['check4'] and the_data['check5']:
            new_max = int(new_max) + 5
            increase = "Congrats You are ready to move on"
        else:
            increase = 'Keep working, not qiute ready to move up'
        query = f'''UPDATE UserExercises
                    SET max = {str(new_max)}
                    WHERE userID = "{userID}" AND exerciseID = "{exerciseID}"'''
        current_app.logger.info(query)

        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return increase
    
@user.route('/userPrograms/<string:userID>', methods=['GET'])
def get_users_program(userID):
    cursor = db.get_db().cursor()

    userID = checkin("userID", "Users", userID)
    if userID == False:
        return "userID Not in Database"

    # use cursor to query the database for a list of products
    cursor.execute(
        f'''SELECT ProgramDescription as label, UserPrograms.programID as value
            from UserPrograms JOIN Programs ON UserPrograms.programID = Programs.programID
            WHERE userID = "{userID}"''')
    
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
    
@user.route('/programDays/<string:programID>', methods=['GET'])
def get_program_days(programID):
    cursor = db.get_db().cursor()

    programID = checkin("programID", "Programs", programID)
    if programID == False:
        return "Program Not in Database"
    # use cursor to query the database for a list of products
    cursor.execute(
        f'''SELECT numDay as label, numDay as value
            from ProgramDetails
            WHERE programID = "{programID}"''')
    
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

@user.route('program/<string:programID>/<int:numDay>', methods=['GET'])
def get_program_details(programID, numDay):
    cursor = db.get_db().cursor()
    
    # make sure programID is in the database
    programID = checkin("programID", "Programs", programID)
    if programID == False:
        return "Program Not in Database"
    
    # make sure day for that program is in the database
    cursor.execute(f'''select numDay from ProgramDetails where programID = "{programID}"''')
    querylist = []
    theData = cursor.fetchall()
    for row in theData:
        querylist.append(row[0])
    if numDay not in querylist:
        return "Day " + str(numDay) + " for programID " + programID + " Not in Database"

    # use cursor to query the database for a list of products
    cursor.execute(
        f'''Select * from ProgramDetails where programID = "{programID}" and numDay = {int(numDay)}''')
    
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

@user.route('exercise/<string:exerciseID>', methods=['GET'])
def get_exercise(exerciseID):
    cursor = db.get_db().cursor()
    exerciseID = checkin("exerciseID", "Exercises", exerciseID)
    if exerciseID == False:
        return "Not in Database"
    # use cursor to query the database for a list of products
    cursor.execute(
        f'''Select * from Exercises where exerciseID = "{exerciseID}" ''')
    
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

