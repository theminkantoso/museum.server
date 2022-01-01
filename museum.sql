-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 01, 2022 lúc 04:44 PM
-- Phiên bản máy phục vụ: 10.4.17-MariaDB
-- Phiên bản PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `museum`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `account`
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
-- Cấu trúc bảng cho bảng `accountfavoriteartifact`
--

CREATE TABLE `accountfavoriteartifact` (
  `AccountId` int(4) NOT NULL,
  `ArtifactId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `accountfavoriteevent`
--

CREATE TABLE `accountfavoriteevent` (
  `AccountId` int(4) NOT NULL,
  `EventId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `agegroup`
--

CREATE TABLE `agegroup` (
  `GroupId` int(4) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `Price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `artifact`
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
-- Cấu trúc bảng cho bảng `artifacttype`
--

CREATE TABLE `artifacttype` (
  `ArtifactTypeId` int(4) NOT NULL,
  `Name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `artifacttypemapping`
--

CREATE TABLE `artifacttypemapping` (
  `ArtifactId` int(4) NOT NULL,
  `ArtifactTypeId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `entryticket`
--

CREATE TABLE `entryticket` (
  `TicketId` int(4) NOT NULL,
  `OrderId` int(4) NOT NULL,
  `NumberPerson` int(2) NOT NULL,
  `TicketType` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `image`
--

CREATE TABLE `image` (
  `ImageId` int(4) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Content` varchar(100) DEFAULT NULL,
  `Url` blob DEFAULT NULL,
  `Path` varchar(100) DEFAULT NULL,
  `MimeType` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `museumevent`
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
-- Cấu trúc bảng cho bảng `notification`
--

CREATE TABLE `notification` (
  `NotificationId` int(4) NOT NULL,
  `AccountId` int(4) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Content` varchar(200) NOT NULL,
  `Time` datetime NOT NULL,
  `Unread` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `orders`
--

CREATE TABLE `orders` (
  `OrderId` int(4) NOT NULL,
  `OrderDate` date NOT NULL,
  `TotalPrice` int(30) NOT NULL,
  `CreatedAt` date NOT NULL,
  `AccountId` int(4) NOT NULL,
  `QRCode` varchar(100) DEFAULT NULL,
  `used` tinyint(4) DEFAULT NULL,
  `type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `orderssouvenirdetail`
--

CREATE TABLE `orderssouvenirdetail` (
  `OrderId` int(4) NOT NULL,
  `SouvenirId` int(4) NOT NULL,
  `Quantity` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `rattings`
--

CREATE TABLE `rattings` (
  `RattingId` int(4) NOT NULL,
  `Star` float NOT NULL,
  `Description` varchar(500) DEFAULT NULL,
  `AccountId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `revoked_tokens`
--

CREATE TABLE `revoked_tokens` (
  `id` int(11) NOT NULL,
  `jti` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `souvenir`
--

CREATE TABLE `souvenir` (
  `SouvenirId` int(4) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Description` varchar(500) NOT NULL,
  `Price` int(3) NOT NULL,
  `Discount` decimal(2,2) DEFAULT NULL,
  `ImageId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`AccountId`);

--
-- Chỉ mục cho bảng `accountfavoriteartifact`
--
ALTER TABLE `accountfavoriteartifact`
  ADD PRIMARY KEY (`ArtifactId`,`AccountId`) USING BTREE,
  ADD KEY `fk_AccountFavoriteArtifact_Account` (`AccountId`),
  ADD KEY `fk_AccountFavoriteArtifact_Artifact` (`ArtifactId`);

--
-- Chỉ mục cho bảng `accountfavoriteevent`
--
ALTER TABLE `accountfavoriteevent`
  ADD PRIMARY KEY (`AccountId`,`EventId`),
  ADD KEY `fk_AccountFavoriteEvent_Account` (`AccountId`),
  ADD KEY `fk_AccountFavoriteEvent_MuseumEvent` (`EventId`);

--
-- Chỉ mục cho bảng `agegroup`
--
ALTER TABLE `agegroup`
  ADD PRIMARY KEY (`GroupId`);

--
-- Chỉ mục cho bảng `artifact`
--
ALTER TABLE `artifact`
  ADD PRIMARY KEY (`ArtifactId`),
  ADD KEY `fk_artifact_image` (`ImageId`);

--
-- Chỉ mục cho bảng `artifacttype`
--
ALTER TABLE `artifacttype`
  ADD PRIMARY KEY (`ArtifactTypeId`);

--
-- Chỉ mục cho bảng `artifacttypemapping`
--
ALTER TABLE `artifacttypemapping`
  ADD PRIMARY KEY (`ArtifactId`,`ArtifactTypeId`),
  ADD UNIQUE KEY `fk_artifacttypemapping_artifact` (`ArtifactId`),
  ADD KEY `fk_ArtifactTypeMapping_ArtifactType` (`ArtifactTypeId`);

--
-- Chỉ mục cho bảng `entryticket`
--
ALTER TABLE `entryticket`
  ADD PRIMARY KEY (`TicketId`),
  ADD KEY `fk_entryticket_AgeGroup` (`TicketType`),
  ADD KEY `fk_entryticket_Orders` (`OrderId`);

--
-- Chỉ mục cho bảng `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`ImageId`);

--
-- Chỉ mục cho bảng `museumevent`
--
ALTER TABLE `museumevent`
  ADD PRIMARY KEY (`EventId`),
  ADD KEY `fk_museumevent_image` (`Poster`);

--
-- Chỉ mục cho bảng `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`NotificationId`),
  ADD KEY `fk_notification_account` (`AccountId`);

--
-- Chỉ mục cho bảng `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderId`),
  ADD KEY `fk_orders_account` (`AccountId`);

--
-- Chỉ mục cho bảng `orderssouvenirdetail`
--
ALTER TABLE `orderssouvenirdetail`
  ADD PRIMARY KEY (`OrderId`,`SouvenirId`),
  ADD KEY `fk_OrdersSouvenirDetail_Orders` (`OrderId`),
  ADD KEY `fk_orderssouvenirdetail_souvenir` (`SouvenirId`);

--
-- Chỉ mục cho bảng `rattings`
--
ALTER TABLE `rattings`
  ADD PRIMARY KEY (`RattingId`),
  ADD KEY `fk_rattings_account` (`AccountId`);

--
-- Chỉ mục cho bảng `revoked_tokens`
--
ALTER TABLE `revoked_tokens`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `souvenir`
--
ALTER TABLE `souvenir`
  ADD PRIMARY KEY (`SouvenirId`),
  ADD KEY `fk_sou` (`ImageId`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `account`
--
ALTER TABLE `account`
  MODIFY `AccountId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `agegroup`
--
ALTER TABLE `agegroup`
  MODIFY `GroupId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `artifact`
--
ALTER TABLE `artifact`
  MODIFY `ArtifactId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `artifacttype`
--
ALTER TABLE `artifacttype`
  MODIFY `ArtifactTypeId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `entryticket`
--
ALTER TABLE `entryticket`
  MODIFY `TicketId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `image`
--
ALTER TABLE `image`
  MODIFY `ImageId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `museumevent`
--
ALTER TABLE `museumevent`
  MODIFY `EventId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `notification`
--
ALTER TABLE `notification`
  MODIFY `NotificationId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `orders`
--
ALTER TABLE `orders`
  MODIFY `OrderId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `rattings`
--
ALTER TABLE `rattings`
  MODIFY `RattingId` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `revoked_tokens`
--
ALTER TABLE `revoked_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `souvenir`
--
ALTER TABLE `souvenir`
  MODIFY `SouvenirId` int(4) NOT NULL AUTO_INCREMENT;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `accountfavoriteartifact`
--
ALTER TABLE `accountfavoriteartifact`
  ADD CONSTRAINT `fk_AccountFavoriteArtifact_Account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`),
  ADD CONSTRAINT `fk_AccountFavoriteArtifact_Artifact` FOREIGN KEY (`ArtifactId`) REFERENCES `artifact` (`ArtifactId`);

--
-- Các ràng buộc cho bảng `accountfavoriteevent`
--
ALTER TABLE `accountfavoriteevent`
  ADD CONSTRAINT `fk_AccountFavoriteEvent_Account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`),
  ADD CONSTRAINT `fk_AccountFavoriteEvent_MuseumEvent` FOREIGN KEY (`EventId`) REFERENCES `museumevent` (`EventId`);

--
-- Các ràng buộc cho bảng `artifact`
--
ALTER TABLE `artifact`
  ADD CONSTRAINT `fk_artifact_image` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);

--
-- Các ràng buộc cho bảng `artifacttypemapping`
--
ALTER TABLE `artifacttypemapping`
  ADD CONSTRAINT `fk_ArtifactTypeMapping_ArtifactType` FOREIGN KEY (`ArtifactTypeId`) REFERENCES `artifacttype` (`ArtifactTypeId`),
  ADD CONSTRAINT `fk_artifacttypemapping_artifact` FOREIGN KEY (`ArtifactId`) REFERENCES `artifact` (`ArtifactId`);

--
-- Các ràng buộc cho bảng `entryticket`
--
ALTER TABLE `entryticket`
  ADD CONSTRAINT `fk_entryticket_AgeGroup` FOREIGN KEY (`TicketType`) REFERENCES `agegroup` (`GroupId`),
  ADD CONSTRAINT `fk_entryticket_Orders` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`OrderId`);

--
-- Các ràng buộc cho bảng `museumevent`
--
ALTER TABLE `museumevent`
  ADD CONSTRAINT `fk_museumevent_image` FOREIGN KEY (`Poster`) REFERENCES `image` (`ImageId`);

--
-- Các ràng buộc cho bảng `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `fk_notification_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Các ràng buộc cho bảng `orderssouvenirdetail`
--
ALTER TABLE `orderssouvenirdetail`
  ADD CONSTRAINT `fk_OrdersSouvenirDetail_Orders` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`OrderId`),
  ADD CONSTRAINT `fk_orderssouvenirdetail_souvenir` FOREIGN KEY (`SouvenirId`) REFERENCES `souvenir` (`SouvenirId`);

--
-- Các ràng buộc cho bảng `rattings`
--
ALTER TABLE `rattings`
  ADD CONSTRAINT `fk_rattings_account` FOREIGN KEY (`AccountId`) REFERENCES `account` (`AccountId`);

--
-- Các ràng buộc cho bảng `souvenir`
--
ALTER TABLE `souvenir`
  ADD CONSTRAINT `fk_sou` FOREIGN KEY (`ImageId`) REFERENCES `image` (`ImageId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
