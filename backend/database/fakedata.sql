CREATE DATABASE IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
 
use lms;

CREATE TABLE IF NOT EXISTS `staff` (
	`Staff_ID` int NOT NULL,
    `Staff_FName` varchar(50)  NOT NULL,
    `Staff_LName` varchar(50)  NOT NULL,
    `Dept` varchar(50)  NOT NULL,
    `Email` varchar(50)  NOT NULL,	

    PRIMARY KEY (`Staff_ID`)
        
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `role` (
	`Role_ID` int NOT NULL,
    `Role_Name` varchar(20)  NOT NULL,
    
    PRIMARY KEY (`Role_ID`)
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

