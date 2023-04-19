USE fitquest;

INSERT INTO Users (userID, username, userpassword, contact, created_at)
VALUES ('501', 'test_user', 'test_user', '8166666666', '2018-01-01 00:00:00');

INSERT INTO Exercises (exerciseID, target, instructions, type, rating, exerciseName)
VALUES ('11', 'Chest', 'Lay on bench and lift weights', 'Strength', '5', 'Bench Press');

INSERT INTO UserExercises (exerciseID, userID, max, reaction, ratedate)
VALUES ('11', '501', '250', '1', '2018-01-01 00:00:00');

INSERT INTO Exercises (exerciseID, target, instructions, type, rating, exerciseName)
VALUES ('12', 'Legs', 'Put the weight on your back and squat', 'Strength', '5', 'Squat');

INSERT INTO UserExercises (exerciseID, userID, max, reaction, ratedate)
VALUES ('12', '501', '300', '1', '2018-01-01 00:00:00');


INSERT INTO Trainers(trainerID, rate, specialty, TrainerName)
VALUES ('002163162', 20.00, 'Womans Strength', 'Tom Smith'),
       ('000111222', 100.00, 'Endurance', 'Jane Dont');



INSERT INTO Users(trainerID, username, userpassword, contact, userID)
VALUES ('002163162', 'LauraMarks', 'IloveMyDog', 'laura@marks.com', '1234'),
       ('002163162', 'SpongeBobSquarepants', 'weenieHotJnrs', '1-800-2723', '700');

INSERT INTO TrainerHistory (TrainerID, userID, hours)
VALUES ('002163162', '700', 900);



INSERT INTO Foods (foodID, foodName, NumServings, carbs, protien, fat)
VALUES ('20000', 'Avocado', 0.5, 900, 0, 0),
       ('6969', 'Mayo', 1 , 900, 0, 0);

INSERT INTO Diet (totalcarbs, totalprotien, totalfat, dietID, userID, dietname)
VALUES (100, 2, 3, '99090', '1234', 'keto');


INSERT INTO DietFoods (foodID, dietID, foodName, mealNum, servings, carbs, protien, fat)
VALUES ('20000', '99090', 'avocado', '0022723', 1, 0.1, 20,20);


INSERT INTO Weight (userID, weight)
VALUES ('700', 99);


INSERT INTO Equipment (machineid, machinestatus, machineName)
VALUES ('221234', 'Busy', 'SquatRack2');


INSERT INTO Staff (employeeID, hourlyRate, Ename, supID)
VALUES ('5001', 16.26, 'Steve', '12');


INSERT INTO WorkOrders (workOrderID, employeeID, machineID)
VALUES ('13', '5001', '221234');

INSERT INTO UserRequests (machineid, userID)
VALUES ('221234', '700');


INSERT INTO Programs (programID, numdays, ProgramDescription)
VALUES ('007700', '10', 'The Strongin: Makes u Real Strong');


INSERT INTO Exercises (exerciseID, target, instructions, type, rating, exerciseName)
VALUES ('0', 'lats', 'grab the bar, pull up', 'Upper Body', 8.5, 'Pull Up');

INSERT INTO UserExercises (exerciseID, max, reaction, userID)
VALUES ('0', 1, 'get me my epipen', '700');


INSERT INTO ProgramDetails (programID, exerciseID, numDay, pattern)
VALUES ('007700', '0', 2, 'do this, then that');


INSERT INTO UserPrograms (userID, programID)
VALUES ('700', '007700');


INSERT INTO Programs (programID, numDays, programDescription)
VALUES ('11', '2', '2 day upper lower split');

INSERT INTO ProgramDetails (programID, exerciseID, numDay, pattern)
VALUES ('11', '1', 1, '.8');

INSERT INTO UserPrograms (programID, userID)
VALUES ('11', '501');
