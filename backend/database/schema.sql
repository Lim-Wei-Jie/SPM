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
    `Skill_Name` varchar(20)  NOT NULL,
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
    `Role_ID` int NOT NULL,
    
    PRIMARY KEY (`Reg_ID`),
    FOREIGN KEY (`Role_ID`) REFERENCES  role(`Role_ID`)
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Skill_Assignment`(
`Course_ID` varchar(20) NOT NULL,
`Skill_ID` varchar(20) NOT NULL,

PRIMARY KEY (`Course_ID`,`Skill_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Role_assignment`(
`Role_ID` varchar(20) NOT NULL,
`Skill_ID` varchar(20) NOT NULL,

PRIMARY KEY (`Role_ID`,`Skill_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO sys(System_Role,System_Role_Desc) VALUES
 (1,'Admin')
,(2,'User')
,(3,'Manager')
,(4,'Trainer');

INSERT INTO course(Course_ID,Course_Name,Course_Desc,Course_Status,Course_Type,Course_Category) VALUES
 ('COR001','Systems Thinking and Design','This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,','Active','Internal','Core')
,('COR002','Lean Six Sigma Green Belt Certification','Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics','Active','Internal','Core')
,('COR004','Service Excellence','The programme provides the learner with the key foundations of what builds customer confidence in the service industr','Pending','Internal','Core')
,('COR006','Manage Change','Identify risks associated with change and develop risk mitigation plans.','Retired','External','Core')
,('FIN001','Data Collection and Analysis','Data is meaningless unless insights and analysis can be drawn to provide useful information for business decision-making. It is imperative that data quality, integrity and security','Active','External','Finance')
,('FIN002','Risk and Compliance Reporting','Regulatory reporting is a requirement for businesses from highly regulated sectors to demonstrate compliance with the necessary regulatory provisions.','Active','External','Finance')
,('FIN003','Business Continuity Planning','Business continuity planning is essential in any business to minimise loss when faced with potential threats and disruptions.','Retired','External','Finance')
,('HRD001','Leading and Shaping a Culture in Learning','This training programme, delivered by the National Centre of Excellence (Workplace Learning), aims to equip participants with the skills and knowledge of the National workplace learning certification framework,','Active','External','HR')
,('MGT001','People Management','enable learners to manage team performance and development through effective communication, conflict resolution and negotiation skills.','Active','Internal','Management')
,('MGT002','Workplace Conflict Management for Professionals','This course will address the gaps to build consensus and utilise knowledge of conflict management techniques to diffuse tensions and achieve resolutions effectively in the best interests of the organisation.','Active','External','Management')
,('MGT003','Enhance Team Performance Through Coaching','The course aims to upskill real estate team leaders in the area of service coaching for performance.','Pending','Internal','Management')
,('MGT004','Personal Effectiveness for Leaders','Learners will be able to acquire the skills and knowledge to undertake self-assessment in relation to one�s performance and leadership style','Active','External','Management')
,('MGT007','Supervisory Management Skills','Supervisors lead teams, manage tasks, solve problems, report up and down the hierarchy, and much more.','Retired','External','Management')
,('SAL001','Risk Management for Smart Business','Apply risk management concepts to digital business','Retired','Internal','Sales')
,('SAL002','CoC in Smart Living Solutions','Participants will acquire the knowledge and skills in setting up a smart living solution','Pending','External','Sales')
,('SAL003','Optimising Your Brand For The Digital Spaces','Digital has fundamentally shifted communication between brands and their consumers from a one-way broadcast to a two-way dialogue. In a hastened bid to transform their businesses to be digital market-ready,','Active','External','Sales')
,('SAL004','Stakeholder Management','Develop a stakeholder engagement plan and negotiate with stakeholders to arrive at mutually-beneficial arrangements.','Active','Internal','Sales')
,('tch001','Print Server Setup','Setting up print server in enterprise environment','Retired','Internal','Technical')
,('tch002','Canon MFC Setup','Setting up Canon ImageRUNNER series of products','Retired','Internal','Technical')
,('tch003','Canon MFC Mainteance and Troubleshooting','Troubleshoot and fixing L2,3 issues of Canon ImageRUNNER series of products','Active','Internal','Technical')
,('tch004','Introduction to Open Platform Communications','This course provides the participants with a good in-depth understanding of the SS IEC 62541 standard','Pending','Internal','Technical')
,('tch005','An Introduction to Sustainability','The course provides learners with the multi-faceted basic knowledge of sustainability.','Active','External','Technical')
,('tch006','Machine Learning DevOps Engineer�','The Machine Learning DevOps Engineer Nanodegree program focuses on the software engineering fundamentals needed to successfully streamline the deployment of data and machine-learning models','Pending','Internal','Technical')
,('tch008','Technology Intelligence and Strategy','Participants will be able to gain knowledge and skills on: - establishing technology strategy with technology intelligence framework and tools','Active','External','Technical')
,('tch009','Smart Sensing Technology','This course introduces sensors and sensing systems. The 5G infrastructure enables the many fast-growing IoT applications equipped with sensors','Pending','External','Technical')
,('tch012','Internet of Things','The Internet of Things (IoT) is integrating our digital and physical world, opening up new and exciting opportunities to deploy, automate, optimize and secure diverse use cases and applications.','Active','Internal','Technical')
,('tch013','Managing Cybersecurity and Risks','Digital security is the core of our daily lives considering that our dependence on the digital world','Active','Internal','Technical')
,('tch014','Certified Information Privacy Professional','The Certified Information Privacy Professional/ Asia (CIPP/A) is the first publicly available privacy certification','Active','External','Technical')
,('tch015','Network Security','Understanding of the fundamental knowledge of network security including cryptography, authentication and key distribution. The security techniques at various layers of computer networks are examined.','Active','External','Technical')
,('tch018','Professional Project Management','solid foundation in the project management processes from initiating a project, through planning, execution, control,','Active','Internal','Technical')
,('tch019','Innovation and Change Management�','the organization that constantly reinvents itself to be relevant has a better chance of making progress','Active','External','Technical');

INSERT INTO skill(Skill_ID,Skill_name,Skill_Desc,Date_Created) VALUES
 (1,'Facebook','Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.','2/2/2022')
,(2,'UB04','Phasellus in felis. Donec semper sapien a libero. Nam dui.','11/19/2021')
,(3,'TMA','In congue. Etiam justo. Etiam pretium iaculis justo.','2/13/2022')
,(4,'Black Box Testing','Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.
Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.','10/7/2022')
,(5,'SGBD','Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.
Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.','8/21/2022')
,(6,'Business Journalism','Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.
Fusce consequat. Nulla nisl. Nunc nisl.','3/3/2022')
,(7,'Nortel DMS','Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.
In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.
Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.','4/17/2022')
,(8,'Social Media Marketing','Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.','8/1/2022')
,(9,'Psychotherapy','Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.','7/17/2022')
,(10,'Robotics','Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.','12/18/2021')
,(11,'Medicine','Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.
Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.','1/5/2022')
,(12,'IAM','Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.
Phasellus in felis. Donec semper sapien a libero. Nam dui.
Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.','1/1/2022')
,(13,'TFM','Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.
Fusce consequat. Nulla nisl. Nunc nisl.','3/20/2022')
,(14,'Luxury Homes','Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.
In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.','12/28/2021')
,(15,'HDV','Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.
In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.','10/28/2021')
,(16,'PTCRB','In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.','5/29/2022')
,(17,'DVB-S2','Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.','7/20/2022')
,(18,'Quantitative Research','Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.
Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.
Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.','8/27/2022')
,(19,'Film','Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.
Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.','10/25/2021')
,(20,'Microsoft Dynamics AX','Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.
Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.','9/24/2022')
,(21,'GSI','Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.
Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.','3/19/2022')
,(22,'Xero','Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.','7/14/2022')
,(23,'OGC','Phasellus in felis. Donec semper sapien a libero. Nam dui.','7/31/2022')
,(24,'Thermodynamics','Phasellus in felis. Donec semper sapien a libero. Nam dui.
Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.','11/4/2021')
,(25,'Evidence','Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.
Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.','7/16/2022')
,(26,'Xserve','Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.
Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.
Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.','11/11/2021')
,(27,'RMX','Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.
Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.
Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.','2/9/2022')
,(28,'Nokia Qt','Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.','1/27/2022')
,(29,'Young Adults','Fusce consequat. Nulla nisl. Nunc nisl.','8/18/2022')
,(30,'Xytech','Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.
Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.','4/12/2022')
,(31,'Project Estimation','Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.
Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.
Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.','12/30/2021')
,(32,'Guided Imagery','Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.','10/21/2021')
,(33,'Corporate FP&amp;A','Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.','1/22/2022')
,(34,'SQL Server Management Studio','Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.
Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.','10/20/2021')
,(35,'Temporary Placement','Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.
Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.
Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.','12/4/2021')
,(36,'MVS','Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.
Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.','3/20/2022')
,(37,'PTCRB','Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.','2/18/2022')
,(38,'Bridge','Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.
In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.','5/11/2022')
,(39,'RBI','Phasellus in felis. Donec semper sapien a libero. Nam dui.','1/22/2022')
,(40,'Green Belt','Fusce consequat. Nulla nisl. Nunc nisl.
Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.
In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.','5/13/2022')
,(41,'Vaccines','Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.','9/13/2022')
,(42,'3D Visualization','Phasellus in felis. Donec semper sapien a libero. Nam dui.','12/7/2021')
,(43,'Behavioral Health','Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.
Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.
Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.','1/10/2022')
,(44,'Public Safety','Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.','4/18/2022')
,(45,'Income Tax','Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.
Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.
Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.','2/3/2022')
,(46,'Outcomes Research','In hc habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.
Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.','7/25/2022')
,(47,'Horticulture','Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.
Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.
Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.','1/21/2022')
,(48,'Oil Analysis','Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.
Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.
Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.','1/15/2022')
,(49,'Nagios','Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.','7/8/2022')
,(50,'FMCG','Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.
Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.','3/4/2022'); 

INSERT INTO role(Role_ID,Role_Name,Role_Desc,Date_Created) VALUES
 (1,'Biostatistician I','Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.
Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.
Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.','7/15/2022')
,(2,'Geologist II','Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.
In congue. Etiam justo. Etiam pretium iaculis justo.
In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.','7/2/2022')
,(3,'Speech Pathologist','Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.
Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.
In congue. Etiam justo. Etiam pretium iaculis justo.','6/3/2022')
,(4,'Office Assistant III','Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.
Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.
Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.','3/17/2022')
,(5,'Help Desk Operator','Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.
In congue. Etiam justo. Etiam pretium iaculis justo.','9/8/2022')
,(6,'Graphic Designer','Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.
Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.','11/29/2021')
,(7,'Senior Quality Engineer','Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.
Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.','3/1/2022')
,(8,'Desktop Support Technician','Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.
Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.','10/26/2021')
,(9,'Geological Engineer','Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.
Fusce consequat. Nulla nisl. Nunc nisl.','7/21/2022')
,(10,'Structural Analysis Engineer','Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.','1/31/2022')
,(11,'VP Quality Control','Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.
Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.','6/20/2022')
,(12,'Programmer Analyst II','Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.
Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.
In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.','11/11/2021')
,(13,'Project Manager','Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.
Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.','1/5/2022')
,(14,'Environmental Specialist','Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.
Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.','1/11/2022')
,(15,'Editor','Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.
Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.','3/6/2022')
,(16,'Health Coach II','Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.','4/18/2022')
,(17,'Pharmacist','Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.
Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.','12/15/2021')
,(18,'Graphic Designer','Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.
Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.','7/20/2022')
,(19,'Actuary','Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.
In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.','3/25/2022')
,(20,'Structural Engineer','Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.
Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.','1/7/2022')
,(21,'Assistant Manager','Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.','5/17/2022')
,(22,'VP Sales','Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.
Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.
Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.','12/4/2021')
,(23,'Food Chemist','Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.
Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.','11/25/2021')
,(24,'Budget/Accounting Analyst I','Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.
Sed ante. Vivamus tortor. Duis mattis egestas metus.','12/14/2021')
,(25,'Senior Editor','Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.','10/11/2022')
,(26,'Software Test Engineer II','Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.','3/8/2022')
,(27,'Programmer Analyst II','Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.','7/3/2022')
,(28,'Sales Representative','Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.
Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.
Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.','1/23/2022')
,(29,'Speech Pathologist','Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.
Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.','9/25/2022')
,(30,'Financial Analyst','Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.
Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.
Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.','7/22/2022')
,(31,'Mechanical Systems Engineer','Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.','10/16/2021')
,(32,'Analog Circuit Design manager','Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.','12/22/2021')
,(33,'Structural Analysis Engineer','Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.','9/23/2022')
,(34,'Staff Accountant II','Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.
Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.
Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.','3/22/2022')
,(35,'Mechanical Systems Engineer','Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.','10/30/2021')
,(36,'Analog Circuit Design manager','Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.
Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.','6/12/2022')
,(37,'Analyst Programmer','Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.
Nullam sit amet turpis elementum igula vehicula consequat. Morbi a ipsum. Integer a nibh.
In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.','2/7/2022')
,(38,'Dental Hygienist','Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.','9/28/2022')
,(39,'VP Sales','Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.','6/11/2022')
,(40,'Assistant Manager','Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.
Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.
Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.','12/7/2021')
,(41,'Staff Accountant III','Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.
Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.','7/7/2022')
,(42,'Health Coach I','Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.
Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.','6/29/2022')
,(43,'Assistant Media Planner','Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.','9/15/2022')
,(44,'Senior Editor','Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.','2/5/2022')
,(45,'Senior Sales Associate','In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.
Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.','10/14/2022')
,(46,'Senior Cost Accountant','Fusce consequat. Nulla nisl. Nunc nisl.','11/5/2021')
,(47,'Assistant Manager','Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.
Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.
In congue. Etiam justo. Etiam pretium iaculis justo.','9/24/2022')
,(48,'GIS Technical Architect','In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.
Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.
Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.','8/14/2022')
,(49,'Analog Circuit Design manager','Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.','11/3/2021')
,(50,'Sales Representative','Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.','8/21/2022');
 

INSERT INTO `Skill_Assignment` (`Course_ID`,`Skill_ID`) VALUES
('COR001', 42),
('FIN002', 18),
('tch006', 18),
('tch006', 15); 

INSERT INTO `Role_Assignment` (`Role_ID`,`Skill_ID`) VALUES
(2, 12),
(32, 14),
(46, 36); 

INSERT INTO registration(Reg_ID,Course_ID,Staff_ID,Reg_Status,Completion_Status,Role_ID) VALUES
 (1,'COR002',130001,'Registered','Completed',2)
,(245,'COR001',130001,'Registered','Completed',3)
,(2,'COR002',130002,'Registered','Completed',4)
,(200100,'COR003a',130002,'Registered','Completed',5)
,(200101,'COR004b',130002,'Registered','Completed',6)
,(3,'COR002',140001,'Registered','Completed',3)
,(111,'SAL004',140001,'Registered','Completed',3)
,(200,'MGT001',140001,'Registered','Completed',3)
,(246,'COR006',140001,'Waitlist',NULL,2);

INSERT INTO staff(Staff_ID,Staff_FName,Staff_LName,Dept,Email,System_Role) VALUES
 (130001,'John','Sim','Chariman','jack.sim@allinone.com.sg',1)
,(130002,'Jack','Sim','CEO','jack.sim@allinone.com.sg',1)
,(140001,'Derek','Tan','Sales','Derek.Tan@allinone.com.sg',3)
,(140002,'Susan','Goh','Sales','Susan.Goh@allinone.com.sg',2)
,(140003,'Janice','Chan','Sales','Janice.Chan@allinone.com.sg',2)
,(140004,'Mary','Teo','Sales','Mary.Teo@allinone.com.sg',2)
,(140008,'Jaclyn','Lee','Sales','Jaclyn.Lee@allinone.com.sg',2)
,(140015,'Oliva','Lim','Sales','Oliva.Lim@allinone.com.sg',2)
,(140025,'Emma','Heng','Sales','Emma.Heng@allinone.com.sg',2)
,(140036,'Charlotte','Wong','Sales','Charlotte.Wong@allinone.com.sg',2)
,(140078,'Amelia','Ong','Sales','Amelia.Ong@allinone.com.sg',2)
,(140102,'Eva','Yong','Sales','Eva.Yong@allinone.com.sg',2)
,(140103,'Sophia','Toh','Sales','Sophia.Toh@allinone.com.sg',2)
,(140108,'Liam','The','Sales','Liam.The@allinone.com.sg',2)
,(140115,'Noah','Ng','Sales','Noah.Ng@allinone.com.sg',2)
,(140525,'Oliver','Tan','Sales','Oliver.Tan@allinone.com.sg',2)
,(140736,'William','Fu','Sales','William.Fu@allinone.com.sg',2)
,(140878,'James','Tong','Sales','James.Tong@allinone.com.sg',2)
,(150008,'Eric','Loh','Ops','Eric.Loh@allinone.com.sg',3)
,(150065,'Noah','Goh','Ops','Noah.Goh@allinone.com.sg',4)
,(150075,'Liam','Tan','Ops','Liam.Tan@allinone.com.sg',4)
,(150076,'Oliver','Chan','Ops','Oliver.Chan@allinone.com.sg',4)
,(150085,'Michael','Ng','Ops','Michael.Ng@allinone.com.sg',4)
,(150095,'Alexander','The','Ops','Alexander.The@allinone.com.sg',4)
,(150096,'Ethan','Tan','Ops','Ethan.Tan@allinone.com.sg',4)
,(150115,'Jaclyn','Lee','Ops','Jaclyn.Lee@allinone.com.sg',4)
,(150118,'William','Teo','Ops','William.Teo@allinone.com.sg',4)
,(150125,'Mary','Teo','Ops','Mary.Teo@allinone.com.sg',4)
,(150126,'Oliva','Lim','Ops','Oliva.Lim@allinone.com.sg',2)
,(150138,'Daniel','Fu','Ops','Daniel.Fu@allinone.com.sg',4)
,(150142,'James','Lee','Ops','James.Lee@allinone.com.sg',4)
,(150143,'John','Lim','Ops','John.Lim@allinone.com.sg',4)
,(150148,'Jack','Heng','Ops','Jack.Heng@allinone.com.sg',4)
,(150155,'Derek','Wong','Ops','Derek.Wong@allinone.com.sg',4)
,(150162,'Jacob','Tong','Ops','Jacob.Tong@allinone.com.sg',4)
,(150163,'Logan','Loh','Ops','Logan.Loh@allinone.com.sg',4)
,(150165,'Oliver','Tan','Ops','Oliver.Tan@allinone.com.sg',2)
,(150166,'William','Fu','Ops','William.Fu@allinone.com.sg',2)
,(150168,'Jackson','Tan','Ops','Jackson.Tan@allinone.com.sg',4)
,(150175,'Aiden','Tan','Ops','Aiden.Tan@allinone.com.sg',4)
,(150192,'Emma','Heng','Ops','Emma.Heng@allinone.com.sg',2)
,(150193,'Charlotte','Wong','Ops','Charlotte.Wong@allinone.com.sg',2)
,(150198,'Amelia','Ong','Ops','Amelia.Ong@allinone.com.sg',2)
,(150205,'Eva','Yong','Ops','Eva.Yong@allinone.com.sg',2)
,(150208,'James','Tong','Ops','James.Tong@allinone.com.sg',2)
,(150215,'Michael','Lee','Ops','Michael.Lee@allinone.com.sg',2)
,(150216,'Ethan','Lim','Ops','Ethan.Lim@allinone.com.sg',2)
,(150232,'John','Loh','Ops','John.Loh@allinone.com.sg',2)
,(150233,'Jack','Tan','Ops','Jack.Tan@allinone.com.sg',2)
,(150238,'Derek','Tan','Ops','Derek.Tan@allinone.com.sg',2)
,(150245,'Benjamin','Tan','Ops','Benjamin.Tan@allinone.com.sg',2)
,(150258,'Daniel','Heng','Ops','Daniel.Heng@allinone.com.sg',2)
,(150265,'Jaclyn','Tong','Ops','Jaclyn.Tong@allinone.com.sg',2)
,(150275,'Mary','Fu','Ops','Mary.Fu@allinone.com.sg',2)
,(150276,'Oliva','Loh','Ops','Oliva.Loh@allinone.com.sg',2)
,(150282,'Jacob','Wong','Ops','Jacob.Wong@allinone.com.sg',2)
,(150283,'Logan','Ong','Ops','Logan.Ong@allinone.com.sg',2)
,(150288,'Jackson','Yong','Ops','Jackson.Yong@allinone.com.sg',2)
,(150295,'Aiden','Toh','Ops','Aiden.Toh@allinone.com.sg',2)
,(150318,'Emma','Tan','Ops','Emma.Tan@allinone.com.sg',2)
,(150342,'Charlotte','Tan','Ops','Charlotte.Tan@allinone.com.sg',2)
,(150343,'Amelia','Tan','Ops','Amelia.Tan@allinone.com.sg',2)
,(150345,'William','Heng','Ops','William.Heng@allinone.com.sg',2)
,(150348,'Eva','Goh','Ops','Eva.Goh@allinone.com.sg',2)
,(150355,'Sophia','Chan','Ops','Sophia.Chan@allinone.com.sg',2)
,(150356,'James','Wong','Ops','James.Wong@allinone.com.sg',2)
,(150398,'John','Ong','Ops','John.Ong@allinone.com.sg',2)
,(150422,'Jack','Yong','Ops','Jack.Yong@allinone.com.sg',2)
,(150423,'Derek','Toh','Ops','Derek.Toh@allinone.com.sg',2)
,(150428,'Benjamin','The','Ops','Benjamin.The@allinone.com.sg',2)
,(150435,'Lucas','Ng','Ops','Lucas.Ng@allinone.com.sg',2)
,(150445,'Ethan','Loh','Ops','Ethan.Loh@allinone.com.sg',2)
,(150446,'Daniel','Tan','Ops','Daniel.Tan@allinone.com.sg',2)
,(150488,'Jacob','Tan','Ops','Jacob.Tan@allinone.com.sg',2)
,(150512,'Logan','Tan','Ops','Logan.Tan@allinone.com.sg',2)
,(150513,'Jackson','Goh','Ops','Jackson.Goh@allinone.com.sg',2)
,(150518,'Aiden','Chan','Ops','Aiden.Chan@allinone.com.sg',2)
,(150525,'Samuel','Teo','Ops','Samuel.Teo@allinone.com.sg',2)
,(150555,'Jaclyn','Wong','Ops','Jaclyn.Wong@allinone.com.sg',2)
,(150565,'Benjamin','Ong','Ops','Benjamin.Ong@allinone.com.sg',4)
,(150566,'Oliva','Ong','Ops','Oliva.Ong@allinone.com.sg',2)
,(150585,'Samuel','Tan','Ops','Samuel.Tan@allinone.com.sg',4)
,(150608,'Emma','Yong','Ops','Emma.Yong@allinone.com.sg',2)
,(150615,'Sophia','Toh','Ops','Sophia.Toh@allinone.com.sg',2)
,(150632,'Charlotte','Toh','Ops','Charlotte.Toh@allinone.com.sg',2)
,(150633,'Amelia','The','Ops','Amelia.The@allinone.com.sg',2)
,(150638,'Eva','Ng','Ops','Eva.Ng@allinone.com.sg',2)
,(150645,'Sophia','Tan','Ops','Sophia.Tan@allinone.com.sg',2)
,(150655,'Lucas','Goh','Ops','Lucas.Goh@allinone.com.sg',2)
,(150695,'William','Tan','Ops','William.Tan@allinone.com.sg',2)
,(150705,'Samuel','The','Ops','Samuel.The@allinone.com.sg',2)
,(150765,'Liam','Teo','Ops','Liam.Teo@allinone.com.sg',2)
,(150776,'Lucas','Yong','Ops','Lucas.Yong@allinone.com.sg',4)
,(150796,'Susan','Goh','Ops','Susan.Goh@allinone.com.sg',4)
,(150826,'Liam','The','Ops','Liam.The@allinone.com.sg',2)
,(150845,'Henry','Tan','Ops','Henry.Tan@allinone.com.sg',2)
,(150866,'Henry','Chan','Ops','Henry.Chan@allinone.com.sg',2)
,(150916,'Susan','Ng','Ops','Susan.Ng@allinone.com.sg',2)
,(150918,'Henry','Toh','Ops','Henry.Toh@allinone.com.sg',4)
,(150935,'Susan','Lee','Ops','Susan.Lee@allinone.com.sg',2)
,(150938,'Janice','Chan','Ops','Janice.Chan@allinone.com.sg',4)
,(150968,'Noah','Ng','Ops','Noah.Ng@allinone.com.sg',2)
,(150976,'Noah','Lee','Ops','Noah.Lee@allinone.com.sg',2)
,(151008,'Alexander','Teo','Ops','Alexander.Teo@allinone.com.sg',2)
,(151055,'Liam','Fu','Ops','Liam.Fu@allinone.com.sg',2)
,(151056,'Alexander','Fu','Ops','Alexander.Fu@allinone.com.sg',2)
,(151058,'Janice','Tan','Ops','Janice.Tan@allinone.com.sg',2)
,(151118,'Oliver','Lim','Ops','Oliver.Lim@allinone.com.sg',2)
,(151146,'Janice','Lim','Ops','Janice.Lim@allinone.com.sg',2)
,(151198,'Michael','Tong','Ops','Michael.Tong@allinone.com.sg',2)
,(151266,'Noah','Tong','Ops','Noah.Tong@allinone.com.sg',2)
,(151288,'Mary','Heng','Ops','Mary.Heng@allinone.com.sg',2)
,(151408,'Oliver','Loh','Ops','Oliver.Loh@allinone.com.sg',2)
,(160008,'Sally','Loh','HR','Sally.Loh@allinone.com.sg',1)
,(160065,'John','Tan','HR','John.Tan@allinone.com.sg',1)
,(160075,'James','Tan','HR','James.Tan@allinone.com.sg',1)
,(160076,'Jack','Goh','HR','Jack.Goh@allinone.com.sg',1)
,(160118,'Derek','Chan','HR','Derek.Chan@allinone.com.sg',1)
,(160135,'Jaclyn','Ong','HR','Jaclyn.Ong@allinone.com.sg',2)
,(160142,'Benjamin','Teo','HR','Benjamin.Teo@allinone.com.sg',1)
,(160143,'Lucas','Lee','HR','Lucas.Lee@allinone.com.sg',1)
,(160145,'Mary','Wong','HR','Mary.Wong@allinone.com.sg',2)
,(160146,'Oliva','Yong','HR','Oliva.Yong@allinone.com.sg',2)
,(160148,'Henry','Lim','HR','Henry.Lim@allinone.com.sg',1)
,(160155,'Alexander','Heng','HR','Alexander.Heng@allinone.com.sg',1)
,(160188,'Emma','Toh','HR','Emma.Toh@allinone.com.sg',2)
,(160212,'Charlotte','The','HR','Charlotte.The@allinone.com.sg',2)
,(160213,'Amelia','Ng','HR','Amelia.Ng@allinone.com.sg',2)
,(160218,'Eva','Tan','HR','Eva.Tan@allinone.com.sg',2)
,(160225,'Sophia','Fu','HR','Sophia.Fu@allinone.com.sg',2)
,(160258,'Michael','Tong','HR','Michael.Tong@allinone.com.sg',2)
,(160282,'Ethan','Loh','HR','Ethan.Loh@allinone.com.sg',2)
,(170166,'David','Yap','Finance','David.Yap@allinone.com.sg',3)
,(170208,'Daniel','Tan','Finance','Daniel.Tan@allinone.com.sg',2)
,(170215,'Mary','Wong','Finance','Mary.Wong@allinone.com.sg',2)
,(170216,'Jaclyn','Ong','Finance','Jaclyn.Ong@allinone.com.sg',2)
,(170232,'Jacob','Tan','Finance','Jacob.Tan@allinone.com.sg',2)
,(170233,'Logan','Goh','Finance','Logan.Goh@allinone.com.sg',2)
,(170238,'Jackson','Chan','Finance','Jackson.Chan@allinone.com.sg',2)
,(170245,'Aiden','Teo','Finance','Aiden.Teo@allinone.com.sg',2)
,(170655,'Samuel','Lee','Finance','Samuel.Lee@allinone.com.sg',2)
,(170866,'Susan','Lim','Finance','Susan.Lim@allinone.com.sg',2)
,(171008,'Janice','Heng','Finance','Janice.Heng@allinone.com.sg',2);