CREATE TABLE `Constituency` (
  `id` int(11) AUTO_INCREMENT,
  `city` varchar(50),
  `mp` varchar(50),
  PRIMARY KEY (`id`)
);

CREATE TABLE `Station` (
  `id` int(11),
  `location` varchar(50),
  `Constituency_ID` int(11),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`Constituency_ID`) REFERENCES `Constituency`(`id`)
);

CREATE TABLE `Reading` (
  `ID` int(11) AUTO_INCREMENT,
  `Date_Time` datetime,
  `Site_ID` int(11),
  `NOx` float,
  `NO2` float,
  `NO` float,
  `PM10` float,
  `O3` float,
  `Temperature` float,
  `ObjectId` int(11),
  `ObjectId2` int(11),
  `NVPM10` float,
  `VPM10` float,
  `NVPM2_5` float,
  `PM2_5` float,
  `VPM2_5` float,
  `CO` float,
  `RH` float,
  `Pressure` float,
  `SO2` float,
  PRIMARY KEY (`ID`),
  FOREIGN KEY (`Site_ID`) REFERENCES `Station`(`id`)
);


