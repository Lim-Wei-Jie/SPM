-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 12, 2020 at 02:17 AM
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

--
-- Database: `order`
--
CREATE DATABASE IF NOT EXISTS `course` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `course`;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `Course_ID` varchar(20) NOT NULL,
  `Course_Name` varchar(50)  NOT NULL,
  `Course_Desc` varchar(255)  NOT NULL,
  `Course_Status` varchar(15)  NOT NULL,
  `Course_Type` varchar(10)  NOT NULL,
  `Course_Category` varchar(50)  NOT NULL
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order`
--

INSERT INTO `course` (`Course_ID`, `Course_Name`, `Course_Desc`, `Course_Status`, `Course_Type`,`Course_Category`) VALUES
("1A2B", 'python', 'functions', 'virtual', 'IT','Informatics');

-- --------------------------------------------------------

--
-- Table structure for table `order_item`
--


--
-- Dumping data for table `order_item`
--


--
-- Constraints for dumped tables
--

--
-- Constraints for table `order_item`
--


COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
