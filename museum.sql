-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 05, 2021 at 05:36 PM
-- Server version: 10.4.21-MariaDB-log
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `museum`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `AccountId` int(4) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `Password` varchar(10000) NOT NULL,
  `RoleId` int(4) DEFAULT NULL,
  `isActivated` tinyint(4) DEFAULT NULL,
  `confirmedAt` datetime DEFAULT NULL,
  `GoogleId` varchar(50) DEFAULT NULL,
  `CreateAt` date DEFAULT NULL,
  `UpdateAt` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accountfavoriteartifact`
--

CREATE TABLE `accountfavoriteartifact` (
  `AccountId` int(4) NOT NULL,
  `ArtifactId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accountfavoriteevent`
--

CREATE TABLE `accountfavoriteevent` (
  `AccountId` int(4) NOT NULL,
  `EventId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounttest`
--

CREATE TABLE `accounttest` (
  `AccountId` int(4) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Password` varchar(10000) NOT NULL,
  `RoleId` int(4) DEFAULT NULL,
  `isActivated` tinyint(4) NOT NULL,
  `confirmedAt` datetime DEFAULT NULL,
  `GoogleId` varchar(50) DEFAULT NULL,
  `CreateAt` datetime DEFAULT NULL,
  `UpdateAt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `agegroup`
--

CREATE TABLE `agegroup` (
  `    GroupId` int(4) NOT NULL,
  `    Description` varchar(500) NOT NULL,
  `    Price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `artifact`
--

CREATE TABLE `artifact` (
  `ArtifactId` int(4) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Description` varchar(1000) NOT NULL,
  `Level` int(1) NOT NULL,
  `ImageId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `artifacttype`
--

CREATE TABLE `artifacttype` (
  `ArtifactTypeId` int(4) NOT NULL,
  `Name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `artifacttypemapping`
--

CREATE TABLE `artifacttypemapping` (
  `ArtifactId` int(4) NOT NULL,
  `ArtifactTypeId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `entryticket`
--

CREATE TABLE `entryticket` (
  `TicketId` int(4) NOT NULL,
  `OrderId` int(4) NOT NULL,
  `TimeFrameId` int(4) NOT NULL,
  `NumberPerson` int(2) NOT NULL,
  `TicketType` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `ImageId` int(4) NOT NULL,
  `Name` varchar(22) NOT NULL,
  `Content` varchar(100) DEFAULT NULL,
  `Url` blob DEFAULT NULL,
  `Path` varchar(100) DEFAULT NULL,
  `MimeType` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `museumevent`
--

CREATE TABLE `museumevent` (
  `EventId` int(4) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Description` varchar(300) NOT NULL,
  `OpenTime` time NOT NULL,
  `CloseTime` time NOT NULL,
  `EventDate` date NOT NULL,
  `Poster` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `NotificationId` int(4) NOT NULL,
  `AccountId` int(4) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Content` varchar(200) NOT NULL,
  `Time` date NOT NULL,
  `Unread` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `OrderId` int(4) NOT NULL,
  `OrderDate` date NOT NULL,
  `TotalPrice` int(30) NOT NULL,
  `CreatedAt` date NOT NULL,
  `AccountId` int(4) NOT NULL,
  `QRCode` varchar(100) DEFAULT NULL,
  `used` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orderssouvenirdetail`
--

CREATE TABLE `orderssouvenirdetail` (
  `OrderId` int(4) NOT NULL,
  `SouvenirId` int(4) NOT NULL,
  `Quantity` int(2) NOT NULL,
  `PriceEach` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rattings`
--

CREATE TABLE `rattings` (
  `RattingId` int(4) NOT NULL,
  `Star` float NOT NULL,
  `Description` varchar(500) DEFAULT NULL,
  `AccountId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `revoked_tokens`
--

CREATE TABLE `revoked_tokens` (
  `id` int(11) NOT NULL,
  `jti` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `souvenir`
--

CREATE TABLE `souvenir` (
  `SouvenirId` int(4) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Description` varchar(500) NOT NULL,
  `Price` int(3) NOT NULL,
  `Discount` decimal(2,2) DEFAULT NULL,
  `ImageId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `timeframe`
--

CREATE TABLE `timeframe` (
  `    TimeFrameId` int(4) NOT NULL,
  `    Description` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`AccountId`);

--
-- Indexes for table `accountfavoriteartifact`
--
ALTER TABLE `accountfavoriteartifact`
  ADD PRIMARY KEY (`ArtifactId`,`AccountId`) USING BTREE,
  ADD KEY `fk_AccountFavoriteArtifact_Account` (`AccountId`),
  ADD KEY `fk_AccountFavoriteArtifact_Artifact` (`ArtifactId`);

--
-- Indexes for table `accountfavoriteevent`
--
ALTER TABLE `accountfavoriteevent`
  ADD PRIMARY KEY (`AccountId`,`EventId`),
  ADD KEY `fk_AccountFavoriteEvent_Account` (`AccountId`),
  ADD KEY `fk_AccountFavoriteEvent_MuseumEvent` (`EventId`);

--
-- Indexes for table `accounttest`
--
ALTER TABLE `accounttest`
  ADD PRIMARY KEY (`AccountId`);

--
-- Indexes for table `agegroup`
--
ALTER TABLE `agegroup`
  ADD PRIMARY KEY (`    GroupId`);

--
-- Indexes for table `artifact`
--
ALTER TABLE `artifact`
  ADD PRIMARY KEY (`ArtifactId`),
  ADD KEY `fk_artifact_image` (`ImageId`);

--
-- Indexes for table `artifacttype`
--
ALTER TABLE `artifacttype`
  ADD PRIMARY KEY (`ArtifactTypeId`);

--
-- Indexes for table `artifacttypemapping`
--
ALTER TABLE `artifacttypemapping`
  ADD PRIMARY KEY (`ArtifactId`,`ArtifactTypeId`),
  ADD UNIQUE KEY `fk_artifacttypemapping_artifact` (`ArtifactId`),
  ADD KEY `fk_ArtifactTypeMapping_ArtifactType` (`ArtifactTypeId`);

--
-- Indexes for table `entryticket`
--
ALTER TABLE `entryticket`
  ADD PRIMARY KEY (`TicketId`),
  ADD KEY `fk_entryticket_TimeFrame` (`TimeFrameId`),
  ADD KEY `fk_entryticket_AgeGroup` (`TicketType`),
  ADD KEY `fk_entryticket_Orders` (`OrderId`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`ImageId`);

--
-- Indexes for table `museumevent`
--
ALTER TABLE `museumevent`
  ADD PRIMARY KEY (`EventId`),
  ADD KEY `fk_museumevent_image` (`Poster`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`NotificationId`),
  ADD KEY `fk_notification_account` (`AccountId`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderId`),
  ADD KEY `fk_orders_account` (`AccountId`);

--
-- Indexes for table `orderssouvenirdetail`
--
ALTER TABLE `orderssouvenirdetail`
  ADD PRIMARY KEY (`OrderId`,`SouvenirId`),
  ADD KEY `fk_OrdersSouvenirDetail_Orders` (`OrderId`),
  ADD KEY `fk_orderssouvenirdetail_souvenir` (`SouvenirId`);

--
-- Indexes for table `rattings`
--
ALTER TABLE `rattings`
  ADD PRIMARY KEY (`RattingId`),
  ADD KEY `fk_rattings_account` (`AccountId`);

--
-- Indexes for table `revoked_tokens`
--
ALTER TABLE `revoked_tokens`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `souvenir`
--
ALTER TABLE `souvenir`
  ADD PRIMARY KEY (`SouvenirId`),
  ADD KEY `fk_sou` (`ImageId`);

--
-- Indexes for table `timeframe`
--
ALTER TABLE `timeframe`
  ADD PRIMARY KEY (`    TimeFrameId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `AccountId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounttest`
--
ALTER TABLE `accounttest`
  MODIFY `AccountId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `agegroup`
--
ALTER TABLE `agegroup`
  MODIFY `    GroupId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `artifact`
--
ALTER TABLE `artifact`
  MODIFY `ArtifactId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `artifacttype`
--
ALTER TABLE `artifacttype`
  MODIFY `ArtifactTypeId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `entryticket`
--
ALTER TABLE `entryticket`
  MODIFY `TicketId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `image`
--
ALTER TABLE `image`
  MODIFY `ImageId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `museumevent`
--
ALTER TABLE `museumevent`
  MODIFY `EventId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `NotificationId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `OrderId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rattings`
--
ALTER TABLE `rattings`
  MODIFY `RattingId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `revoked_tokens`
--
ALTER TABLE `revoked_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `souvenir`
--
ALTER TABLE `souvenir`
  MODIFY `SouvenirId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `timeframe`
--
ALTER TABLE `timeframe`
  MODIFY `    TimeFrameId` int(4) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accountfavoriteartifact`
--
ALTER TABLE `accountfavoriteartifact`
  ADD CONSTRAINT `fk_AccountFavoriteArtifact_Account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`),
  ADD CONSTRAINT `fk_AccountFavoriteArtifact_Artifact` FOREIGN KEY (`ArtifactId`) REFERENCES `artifact` (`ArtifactId`);

--
-- Constraints for table `accountfavoriteevent`
--
ALTER TABLE `accountfavoriteevent`
  ADD CONSTRAINT `fk_AccountFavoriteEvent_Account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`),
  ADD CONSTRAINT `fk_AccountFavoriteEvent_MuseumEvent` FOREIGN KEY (`EventId`) REFERENCES `museumevent` (`EventId`);

--
-- Constraints for table `artifact`
--
ALTER TABLE `artifact`
  ADD CONSTRAINT `fk_artifact_image` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);

--
-- Constraints for table `artifacttypemapping`
--
ALTER TABLE `artifacttypemapping`
  ADD CONSTRAINT `fk_ArtifactTypeMapping_ArtifactType` FOREIGN KEY (`ArtifactTypeId`) REFERENCES `artifacttype` (`ArtifactTypeId`),
  ADD CONSTRAINT `fk_artifacttypemapping_artifact` FOREIGN KEY (`ArtifactId`) REFERENCES `artifact` (`ArtifactId`);

--
-- Constraints for table `entryticket`
--
ALTER TABLE `entryticket`
  ADD CONSTRAINT `fk_entryticket_AgeGroup` FOREIGN KEY (`TicketType`) REFERENCES `agegroup` (`    GroupId`),
  ADD CONSTRAINT `fk_entryticket_Orders` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`OrderId`),
  ADD CONSTRAINT `fk_entryticket_TimeFrame` FOREIGN KEY (`TimeFrameId`) REFERENCES `timeframe` (`    TimeFrameId`);

--
-- Constraints for table `museumevent`
--
ALTER TABLE `museumevent`
  ADD CONSTRAINT `fk_museumevent_image` FOREIGN KEY (`Poster`) REFERENCES `image` (`ImageId`);

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `fk_notification_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `fk_orders_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Constraints for table `orderssouvenirdetail`
--
ALTER TABLE `orderssouvenirdetail`
  ADD CONSTRAINT `fk_OrdersSouvenirDetail_Orders` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`OrderId`),
  ADD CONSTRAINT `fk_orderssouvenirdetail_souvenir` FOREIGN KEY (`SouvenirId`) REFERENCES `souvenir` (`SouvenirId`);

--
-- Constraints for table `rattings`
--
ALTER TABLE `rattings`
  ADD CONSTRAINT `fk_rattings_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Constraints for table `souvenir`
--
ALTER TABLE `souvenir`
  ADD CONSTRAINT `fk_sou` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
