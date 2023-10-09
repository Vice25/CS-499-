
DROP DATABASE IF EXISTS `QuantigrationUpdates`;
CREATE DATABASE `QuantigrationUpdates`;
USE `QuantigrationUpdates`;

CREATE TABLE `Customers` (
  `CustomerID` int,
  `FirstName` varchar(25),
  `LastName` varchar (25),
  `Street` varchar(50),
  `City` varchar(50),
  `State`varchar(25),
  `ZipCode`varchar(10),
  `Telephone`varchar(15),
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO CUSTOMERS VALUES (1,'Victor','Landi','1 Main Street','Jacksonville','NC',28540,'910-555-1212'),
 (2,'John Q','Public','25 Star Lane','New York','NY',10001,'212-555-1234'),
 (3,'Mary','Smith','33 Greenway Court','Patterson','NJ',07634,'201-999-0987'),
 (4,'Nosmo','King','Jackie Vernon Lane','Los Angeles','CA',90210,'304-987-1222'),
 (5,'Beverly','Fiction','Pseudo Street','Palm Court','Fl',33445,'561-333-5454');


CREATE TABLE `Orders` (
  `OrderID`int,
  `CustomerID`int,
  `SKU`varchar(20),
  `Description`varchar(50),
  PRIMARY KEY (OrderID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `Orders` VALUES (1,01,9909,Oil Pan);
INSERT INTO `Orders` VALUES (2,02,9908,Oil Filter);
INSERT INTO `Orders` VALUES (3,03,9907,Gas Filter);
INSERT INTO `Orders` VALUES (4,04,9906,Intake Valve);
INSERT INTO `Orders` VALUES (5,05,9905,Pressure Meter);


CREATE TABLE RMA (
  RMAID int,
  OrderID int,
  Step varchar(50),
  Status varchar(15),
  Reason varchar(15),
   PRIMARY KEY (RMAID),
   FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO RMA VALUES (1,1,'Credit Customer Order','Complete','Defective'),
 (2,2,'Awaiting Paperwork','Pending','Wrong Part'),
 (3,3,'Requested Paperwork','Pending','Defective'),
 (4,4,'Credit Customer Order','Complete','Wrong Part'),
 (5,5,'Awaiting Paperwork','Pending','Defective');


