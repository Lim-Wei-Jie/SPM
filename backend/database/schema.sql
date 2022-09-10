-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE DATABASE IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


DROP TABLE IF EXISTS `lms`;


CREATE TABLE IF NOT EXISTS `sys` (
	`System_Role` int NOT NULL,
	`System_Role_Desc` varchar(255) NOT NULL,
    
    
    PRIMARY KEY (`System_Role`)
	    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `staff` (
	`Staff_ID` int NOT NULL,
    `Staff_FName` varchar(50)  NOT NULL,
    `Staff_LName` varchar(50)  NOT NULL,
    `Dept` varchar(50)  NOT NULL,
    `Email` varchar(50)  NOT NULL,
	`System_Role` int NOT NULL, 
	

    PRIMARY KEY (`Staff_ID`),
	FOREIGN KEY (`System_Role`) REFERENCES  sys(`System_Role`) 
    
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
    `Skill_Desc` varchar(20)  NOT NULL,
    
    
    -- extra
    `Date_Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `Course_ID` varchar(20),
    PRIMARY KEY (`Skill_ID`),
    FOREIGN KEY (`Course_ID`) REFERENCES course(`Course_ID`) 
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE IF NOT EXISTS `role` (
	`Role_ID` int NOT NULL,
    `Role_Name` varchar(20)  NOT NULL,
    
	-- extra
    `Role_Desc` varchar(20)  NOT NULL,
    `Date_Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `Skill_ID` int NOT NULL,
    
    PRIMARY KEY (`Role_ID`),
    FOREIGN KEY (`Skill_ID`) REFERENCES skill(`Skill_ID`) 
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `registration` (
	`Reg_ID` int(20) NOT NULL,
    `Course_ID` varchar(20)  NOT NULL,
    `Staff_ID` int(20)  NOT NULL,
	`Reg_Status` varchar(20) NOT NULL,
    `Completion_Status` varchar(20) NOT NULL,
    
    
    PRIMARY KEY (`Reg_ID`),
    FOREIGN KEY (`Course_ID`) REFERENCES course(`Course_ID`) ,
	FOREIGN KEY (`Staff_ID`) REFERENCES staff(`Staff_ID`) 
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;





