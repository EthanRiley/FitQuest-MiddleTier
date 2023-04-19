DROP SCHEMA IF EXISTS `fitquest`;
CREATE SCHEMA IF NOT EXISTS `fitquest` DEFAULT CHARACTER SET latin1 ;
USE `fitquest`;

create table if not exists Trainers (
	trainerID VARCHAR(10) NOT NULL,
	rate DECIMAL(6, 2) NOT NULL,
	startdate DATETIME DEFAULT CURRENT_TIMESTAMP(),
	specialty VARCHAR(20),
	TrainerName varchar(50),
    PRIMARY KEY (trainerID)
);

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


create table if not exists Foods (
	foodID VARCHAR(10),
	foodName VARCHAR(200),
	NumServings DECIMAL(6, 2),
	unit VARCHAR(50),
	carbs DECIMAL(6, 2),
	protien DECIMAL(6, 2),
	fat DECIMAL(6, 2),
	PRIMARY KEY (foodID)
);

create table if not exists Diet (
	totalcarbs DECIMAL(8, 2),
	totalprotien DECIMAL(8, 2),
	totalfat DECIMAL(8, 2),
	dietID VARCHAR(10) NOT NULL ,
	dietname VARCHAR(200),
	userID VARCHAR(10) NOT NULL,
	PRIMARY KEY (dietID),
	CONSTRAINT d_key
		FOREIGN KEY (userID)
			REFERENCES Users (userID)
	on DELETE cascade
);


create table if not exists DietFoods (
	foodID VARCHAR(10),
	dietID VARCHAR(10),
	foodName VARCHAR(200),
	logdate DATETIME DEFAULT CURRENT_TIMESTAMP(),
	mealNum VARCHAR(10) NOT NULL ,
	servings decimal(6, 2),
	carbs DECIMAL(6, 2),
	protien DECIMAL(6, 2),
	fat DECIMAL(6, 2),
	CONSTRAINT food_k
        FOREIGN KEY (foodID)
            REFERENCES Foods (foodID),
    CONSTRAINT diet_k
        FOREIGN KEY (dietID)
            REFERENCES Diet (dietID)
);





create table if not exists Weight (
	userID VARCHAR(10),
	weight INT,
	date DATETIME DEFAULT CURRENT_TIMESTAMP(),
	CONSTRAINT weight_k FOREIGN KEY (userID) REFERENCES Users (userID)
);

create table if not exists Equipment (
	machineid VARCHAR(10) NOT NULL,
	datepurchased DATETIME DEFAULT CURRENT_TIMESTAMP(),
	machinestatus VARCHAR(500),
	machineName VARCHAR(99),
	PRIMARY KEY (machineid)
);


create table if not exists Staff (
	startdate DATETIME DEFAULT CURRENT_TIMESTAMP(),
	employeeID VARCHAR(10) NOT NULL,
	biweeklyhours DECIMAL(5, 2) DEFAULT 0.00,
	hourlyRate DECIMAL(5, 2),
	Ename VARCHAR(40),
	supID VARCHAR(10) NOT NULL,
	PRIMARY KEY (employeeID)
);

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

create table if not exists UserRequests (
	machineid VARCHAR(10) NOT NULL ,
	userID VARCHAR(10) NOT NULL,
	CONSTRAINT req_k FOREIGN KEY (userID) REFERENCES Users (userID)
	    ON DELETE CASCADE,
	CONSTRAINT equipment_key FOREIGN KEY (machineID) REFERENCES Equipment (machineID)
                                      ON DELETE CASCADE
);

create table if not exists Programs (
	programID VARCHAR(10),
	numdays VARCHAR(10),
	ProgramDescription VARCHAR(200),
	PRIMARY KEY (programID)
);

create table if not exists Exercises (
	exerciseID VARCHAR(10) NOT NULL,
	target VARCHAR(150),
	instructions VARCHAR(500),
	type VARCHAR(50),
	rating DECIMAL(3,1),
	exerciseName VARCHAR(40),
	PRIMARY KEY (exerciseID)
);

create table if not exists UserExercises (
	exerciseID VARCHAR(10),
	max INT,
	reaction varchar(500),
	userID VARCHAR(10),
	ratedate DATETIME DEFAULT CURRENT_TIMESTAMP(),
    CONSTRAINT ex_ex_key FOREIGN KEY (exerciseID) REFERENCES Exercises (exerciseID),
    CONSTRAINT ex_us FOREIGN KEY (userID) REFERENCES Users (userID)
);

create table if not exists ProgramDetails (
	programID VARCHAR(10) NOT NULL ,
	exerciseID VARCHAR(10) NOT NULL ,
	numDay INT,
	pattern VARCHAR(150),
	CONSTRAINT program_k FOREIGN KEY (programID) REFERENCES Programs (programID) ON DELETE CASCADE,
	CONSTRAINT excersise_k FOREIGN KEY (exerciseID) REFERENCES Exercises (exerciseID) ON DELETE CASCADE
);

create table if not exists UserPrograms (
	userID VARCHAR(10) NOT NULL,
	programID VARCHAR(10) NOT NULL,
	CONSTRAINT UP_Users_k FOREIGN KEY (userID) REFERENCES Users (userID),
	CONSTRAINT OP_programs_programs FOREIGN KEY (programID) REFERENCES Programs (programID)
);



