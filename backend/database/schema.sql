-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE DATABASE IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use lms;


DROP Table IF EXISTS `lms`;


CREATE TABLE IF NOT EXISTS `sys` (
	`System_Role` int NOT NULL,
	`System_Role_Desc` varchar(255) NOT NULL,
    
    
    PRIMARY KEY (`System_Role`)
	    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `staff` (
	`Staff_ID` varchar(20) NOT NULL,
    `Staff_FName` varchar(50)  NOT NULL,
    `Staff_LName` varchar(50)  NOT NULL,
    `Dept` varchar(50)  NOT NULL,
    `Email` varchar(50)  NOT NULL,
	`System_Role` int NOT NULL, 
	

    PRIMARY KEY (`Staff_ID`)    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE IF NOT EXISTS `course` (
	`Course_ID` varchar(20) NOT NULL,
    `Course_Name` varchar(50)  NOT NULL,
    `Course_Desc` varchar(255)  NOT NULL,
    `Course_Status` varchar(15)  NOT NULL,
    `Course_Type` varchar(10)  NOT NULL,
    `Course_Category` varchar(50)  NOT NULL,
    
    
    
    PRIMARY KEY (`Course_ID`)
        
)ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE IF NOT EXISTS `skill` (
	`Skill_ID` int NOT NULL,
    `Skill_name` varchar(20)  NOT NULL,
    `Skill_Desc` varchar(20)  NULL,
    
    
    -- extra
    `Date_Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (`Skill_ID`)    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE IF NOT EXISTS `role` (
	`Role_ID` int NOT NULL,
    `Role_Name` varchar(20)  NOT NULL,
    
	-- extra
    `Role_Desc` varchar(20)  NOT NULL,
    `Date_Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (`Role_ID`)
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `registration` (
	`Reg_ID` int(20) NOT NULL,
    `Course_ID` varchar(20)  NOT NULL,
    `Staff_ID` varchar(20)  NOT NULL,
	`Reg_Status` varchar(20) NOT NULL,
    `Completion_Status` varchar(20) NOT NULL,
    
    
    PRIMARY KEY (`Reg_ID`),
    FOREIGN KEY (`Course_ID`) REFERENCES course(`Course_ID`) ,
	FOREIGN KEY (`Staff_ID`) REFERENCES staff(`Staff_ID`) 
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `skill_assignment`(
`skill_assignment_id` int(11) NOT NULL,
`course_ID` varchar(20) NOT NULL,
`skill_ID` varchar(20) NOT NULL,

PRIMARY KEY (`skill_assignment_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `role_assignment`(
`role_assignment_id` int(11) NOT NULL,
`role_ID` varchar(20) NOT NULL,
`skill_ID` varchar(20) NOT NULL,

PRIMARY KEY (`role_assignment_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `sys` (`System_Role`, `System_Role_Desc` ) VALUES
('1', 'System Admin which can have greater access functions'),
('2', 'User which has limited functionality to only edit personalized learning journey');

INSERT INTO `staff` (`Staff_ID`, `Staff_FName`,`Staff_LName`,`Dept`,`Email`,`System_Role` ) VALUES
(123456 , 'Jordan', 'Ng', 'HR', 'jordanng@gmail.com', '1'),
(974182, 'Ryan', 'Wong', 'Staff', 'ryanwong@yahoo.com', '2'); 

INSERT INTO `course` (`Course_ID`, `Course_Name`,`Course_Desc`,`Course_Status`,`Course_Type`,`Course_Category` ) VALUES
(123456 , 'Mechanical Engineering', 'ME', 'Retired', 'External', 'Engineering'),
(974182, 'Computer Science', 'CE', 'Active', 'Internal', 'IT'); 

INSERT INTO `skill` (`Skill_ID`, `Skill_name`,`Skill_Desc`,`Date_Created` ) VALUES
(1234567 , 'Mechanical Engineering Skill', 'MES Desc', 'Jan-21-2022'),
(9741827, 'Computer Science Skill', 'CES Desc', 'Aug-21-2022'); 

INSERT INTO `role` (`Role_ID`, `Role_Name`,`Role_Desc`,`Date_Created` ) VALUES
(123456 , 'Mechanical Engineering Role', 'MER Desc', 'Jan-21-2022'),
(974182, 'Computer Science Role', 'CER Desc', 'Aug-21-2022'); 


INSERT INTO `registration` (`Reg_ID`, `Course_ID`,`Staff_ID`,`Reg_Status`,`Completion_Status` ) VALUES
(12345655 , 123456, 123456, 'Waitlist', 'Incomplete'),
(97418255, 974182, 974182, 'Registered', 'Incomplete'); 