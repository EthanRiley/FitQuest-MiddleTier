USE FitQuest;

INSERT INTO Users (userID, username, userpassword, contact, created_at)
VALUES ('1', 'test_user', 'test_user', '8166666666', '2018-01-01 00:00:00');

INSERT INTO Exercises (exerciseID, target, instructions, type, rating, exerciseName)
VALUES ('1', 'Chest', 'Lay on bench and lift weights', 'Strength', '5', 'Bench Press');

INSERT INTO UserExercises (exerciseID, userID, max, reaction, ratedate)
VALUES ('1', '1', '250', '1', '2018-01-01 00:00:00');

INSERT INTO Exercises (exerciseID, target, instructions, type, rating, exerciseName)
VALUES ('2', 'Legs', 'Put the weight on your back and squat', 'Strength', '5', 'Squat');

INSERT INTO UserExercises (exerciseID, userID, max, reaction, ratedate)
VALUES ('2', '1', '300', '1', '2018-01-01 00:00:00');

INSERT INTO Programs (programID, numDays, programDescription)
VALUES ('1', '2', '2 day upper lower split');

INSERT INTO ProgramDetails (programID, exerciseID, numDay, pattern)
VALUES ('1', '1', 1, '.8');

INSERT INTO UserPrograms (programID, userID)
VALUES ('1', '1');
