
DROP SCHEMA IF EXISTS `FitQuest`;
CREATE SCHEMA IF NOT EXISTS `FitQuest` DEFAULT CHARACTER SET latin1 ;
USE `FitQuest`;

create table if not exists Trainers (
	trainerID VARCHAR(10) NOT NULL,
	rate DECIMAL(6, 2) NOT NULL,
	startdate DATETIME DEFAULT CURRENT_TIMESTAMP(),
	specialty VARCHAR(20),
	TrainerName varchar(50),
    PRIMARY KEY (trainerID)
);

INSERT INTO Trainers(trainerID, rate, specialty, TrainerName)
VALUES ('002163162', 20.00, 'Womans Strength', 'Tom Smith'),
       ('000111222', 100.00, 'Endurance', 'Jane Dont');


create table if not exists Users (
    trainerID VARCHAR(10),
	username    varchar(50)  NOT NULL,
    userpassword varchar(50) NOT NULL,
    contact varchar(100) NOT NULL,
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP(),
    userID       VARCHAR(10)          NOT NULL,
    PRIMARY KEY (userID),
    UNIQUE INDEX (userpassword),
    UNIQUE INDEX (userID),
    CONSTRAINT U_t_key
        FOREIGN KEY (trainerID)
            REFERENCES Trainers (trainerID)
            ON UPDATE cascade
            ON DELETE CASCADE
);

INSERT INTO Users(trainerID, username, userpassword, contact, userID)
VALUES ('002163162', 'LauraMarks', 'IloveMyDog', 'laura@marks.com', '1234'),
       ('002163162', 'SpongeBobSquarepants', 'weenieHotJnrs', '1-800-2723', '700');

create table if not exists TrainerHistory (
	TrainerID VARCHAR(10),
	userID VARCHAR(10),
	hours DECIMAL(8,2),
	CONSTRAINT t_key
        FOREIGN KEY (trainerID)
            REFERENCES Trainers (trainerID)
            ON UPDATE cascade
            ON DELETE CASCADE
);

INSERT INTO TrainerHistory (TrainerID, userID, hours)
VALUES ('002163162', '700', 900);


create table if not exists Foods (
	foodID VARCHAR(10),
	foodName VARCHAR(20),
	NumServings DECIMAL(6, 2),
	carbs DECIMAL(6, 2),
	protien DECIMAL(6, 2),
	fat DECIMAL(6, 2),
	PRIMARY KEY (foodID)
);

INSERT INTO Foods (foodID, foodName, NumServings, carbs, protien, fat)
VALUES ('20000', 'Avocado', 0.5, 900, 0, 0),
       ('6969', 'Mayo', 1 , 900, 0, 0);

create table if not exists Diet (
	totalcarbs DECIMAL(8, 2),
	totalprotien DECIMAL(8, 2),
	totalfat DECIMAL(8, 2),
	dietID VARCHAR(10) NOT NULL,
	foodID VARCHAR(10),
	PRIMARY KEY (dietID),
	CONSTRAINT diet_key
        FOREIGN KEY (foodID)
            REFERENCES Foods (foodID)
);

INSERT INTO Diet (totalcarbs, totalprotien, totalfat, dietID)
VALUES (100, 2, 3, '99090');

create table if not exists DietFoods (
	foodID VARCHAR(10),
	dietID VARCHAR(10),
	foodName VARCHAR(20),
	logdate DATETIME DEFAULT CURRENT_TIMESTAMP(),
	mealNum VARCHAR(10) NOT NULL ,
	servings INT,
	unitsize DECIMAL(6, 2),
	carbs DECIMAL(6, 2),
	protien DECIMAL(6, 2),
	fat DECIMAL(6, 2),
	PRIMARY KEY (mealNum),
	CONSTRAINT food_k
        FOREIGN KEY (foodID)
            REFERENCES Foods (foodID),
    CONSTRAINT diet_k
        FOREIGN KEY (dietID)
            REFERENCES Diet (dietID)
);

INSERT INTO DietFoods (foodID, dietID, foodName, mealNum, servings, unitsize, carbs, protien, fat)
VALUES ('20000', '99090', 'avocado', '0022723', 1, 1000, 0.1, 20,20);

create table if not exists Weight (
	userID VARCHAR(10),
	weight INT,
	PRIMARY KEY (weight),
	CONSTRAINT weight_k FOREIGN KEY (userID) REFERENCES Users (userID)
);

INSERT INTO Weight (userID, weight)
VALUES ('700', 99);

create table if not exists Equipment (
	machineid VARCHAR(10) NOT NULL,
	datepurchased DATETIME DEFAULT CURRENT_TIMESTAMP(),
	machinestatus VARCHAR(4),
	machineName VARCHAR(99),
	PRIMARY KEY (machineid)
);

INSERT INTO Equipment (machineid, machinestatus, machineName)
VALUES ('221234', 'Busy', 'SquatRack2');

create table if not exists Staff (
	startdate DATETIME DEFAULT CURRENT_TIMESTAMP(),
	employeeID VARCHAR(10) NOT NULL,
	biweeklyhours DECIMAL(5, 2) DEFAULT 0.00,
	hourlyRate DECIMAL(5, 2),
	Ename VARCHAR(40),
	supID VARCHAR(10) NOT NULL,
	PRIMARY KEY (employeeID),
	CONSTRAINT sup_k FOREIGN KEY (supID) REFERENCES Staff (employeeID)
);

INSERT INTO Staff (employeeID, hourlyRate, Ename, supID)
VALUES ('99', 16.26, 'Steve', '99');

create table if not exists WorkOrders (
	workOrderID VARCHAR(10) NOT NULL,
	dateplaced DATETIME DEFAULT CURRENT_TIMESTAMP(),
	employeeID VARCHAR(10) NOT NULL,
	machineID VARCHAR(10) NOT NULL,
	PRIMARY KEY (workOrderID),
	CONSTRAINT staff_k FOREIGN KEY (employeeID) REFERENCES Staff (employeeID)
	    ON DELETE CASCADE,
	CONSTRAINT e_key FOREIGN KEY (machineID) REFERENCES Equipment (machineID)
                                      ON DELETE CASCADE
);

INSERT INTO WorkOrders (workOrderID, employeeID, machineID)
VALUES ('1', '99', '221234');

create table if not exists UserRequests (
	machineid VARCHAR(10) NOT NULL ,
	userID VARCHAR(10) NOT NULL,
	CONSTRAINT req_k FOREIGN KEY (userID) REFERENCES Users (userID)
	    ON DELETE CASCADE,
	CONSTRAINT equipment_key FOREIGN KEY (machineID) REFERENCES Equipment (machineID)
                                      ON DELETE CASCADE
);

INSERT INTO UserRequests (machineid, userID)
VALUES ('221234', '700');

create table if not exists Programs (
	programID VARCHAR(10),
	numdays VARCHAR(10),
	ProgramDescription VARCHAR(200),
	PRIMARY KEY (programID)
);

INSERT INTO Programs (programID, numdays, ProgramDescription)
VALUES ('007700', '10', 'The Strongin: Makes u Real Strong');

create table if not exists Exercises (
	exerciseID VARCHAR(10) NOT NULL,
	target VARCHAR(150),
	instructions VARCHAR(500),
	type VARCHAR(50),
	rating DECIMAL(3,1),
	exerciseName VARCHAR(40),
	PRIMARY KEY (exerciseID)
);

INSERT INTO Exercises (exerciseID, target, instructions, type, rating, exerciseName)
VALUES ('0', 'lats', 'grab the bar, pull up', 'Upper Body', 8.5, 'Pull Up');

create table if not exists UserExercises (
	exerciseID VARCHAR(10),
	max DECIMAL(4,2),
	reaction DECIMAL(3,1),
	userID VARCHAR(10),
	ratedate DATETIME DEFAULT CURRENT_TIMESTAMP(),
    CONSTRAINT ex_ex_key FOREIGN KEY (exerciseID) REFERENCES Exercises (exerciseID),
    CONSTRAINT ex_us FOREIGN KEY (userID) REFERENCES Users (userID)
);

INSERT INTO UserExercises (exerciseID, max, reaction, userID)
VALUES ('0', 1, 1.2, '700');

create table if not exists ProgramDetails (
	programID VARCHAR(10) NOT NULL ,
	exerciseID VARCHAR(10) NOT NULL ,
	numDay INT,
	pattern VARCHAR(150),
	CONSTRAINT program_k FOREIGN KEY (programID) REFERENCES Programs (programID) ON DELETE CASCADE,
	CONSTRAINT excersise_k FOREIGN KEY (exerciseID) REFERENCES Exercises (exerciseID) ON DELETE CASCADE
);

INSERT INTO ProgramDetails (programID, exerciseID, numDay, pattern)
VALUES ('007700', '0', 2, 'do this, then that');

create table if not exists UserPrograms (
	userID VARCHAR(10) NOT NULL,
	programID VARCHAR(10) NOT NULL,
	CONSTRAINT UP_Users_k FOREIGN KEY (userID) REFERENCES Users (userID),
	CONSTRAINT OP_programs_programs FOREIGN KEY (programID) REFERENCES Programs (programID)
);

INSERT INTO UserPrograms (userID, programID)
VALUES ('700', '007700');

create table if not exists Eat (
	userID VARCHAR(10) NOT NULL,
	dietID VARCHAR(10) NOT NULL,
CONSTRAINT eat_user_key FOREIGN KEY (userID) REFERENCES Users (userID) ON DELETE CASCADE,
CONSTRAINT eat_diet_key FOREIGN KEY (dietID) REFERENCES Diet (dietID)
);

INSERT INTO Eat (userID, dietID) VALUES ('700', '99090');
