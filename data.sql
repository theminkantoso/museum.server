-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 29, 2021 at 05:22 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

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

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`AccountId`, `email`, `Password`, `RoleId`, `isActivated`, `confirmedAt`, `GoogleId`, `CreateAt`, `UpdateAt`) VALUES
(1, 'trangco19621962@gmail.com', 'sha256$iUtOAp2l3Fot4W6j$e865a998d8ab5d9b98db60448d64b33892e4790863c80bfa42c0de4c80886595', NULL, 1, '2021-12-28 19:28:18', NULL, NULL, NULL);

--
-- Dumping data for table `agegroup`
--

INSERT INTO `agegroup` (`GroupId`, `Description`, `Price`) VALUES
(1, 'children', 50000),
(2, 'adult', 80000),
(3, 'elderly', 65000);

--
-- Dumping data for table `entryticket`
--

INSERT INTO `entryticket` (`TicketId`, `OrderId`, `NumberPerson`, `TicketType`) VALUES
(1, 4, 2, 1),
(2, 4, 2, 2),
(3, 4, 3, 3),
(4, 5, 2, 1),
(5, 5, 2, 2),
(6, 5, 3, 3),
(7, 6, 2, 1),
(8, 6, 2, 2),
(9, 6, 3, 3),
(10, 7, 2, 1),
(11, 7, 2, 2),
(12, 7, 3, 3),
(13, 8, 2, 1),
(14, 8, 2, 2),
(15, 8, 3, 3),
(16, 9, 2, 1),
(17, 9, 2, 2),
(18, 9, 3, 3),
(19, 10, 2, 1),
(20, 10, 2, 2),
(21, 10, 3, 3),
(22, 11, 2, 1),
(23, 11, 2, 2),
(24, 11, 3, 3),
(25, 12, 2, 1),
(26, 12, 2, 2),
(27, 12, 3, 3),
(28, 13, 2, 1),
(29, 13, 2, 2),
(30, 13, 3, 3),
(31, 14, 2, 1),
(32, 14, 2, 2),
(33, 14, 3, 3),
(34, 15, 2, 1),
(35, 15, 2, 2),
(36, 15, 3, 3),
(37, 16, 2, 1),
(38, 16, 2, 2),
(39, 16, 3, 3),
(40, 17, 2, 1),
(41, 17, 2, 2),
(42, 17, 3, 3),
(43, 18, 2, 1),
(44, 18, 2, 2),
(45, 18, 3, 3),
(46, 19, 2, 1),
(47, 19, 2, 2),
(48, 19, 3, 3),
(49, 20, 2, 1),
(50, 20, 2, 2),
(51, 20, 3, 3),
(52, 21, 2, 1),
(53, 21, 2, 2),
(54, 21, 3, 3),
(55, 22, 2, 1),
(56, 22, 2, 2),
(57, 22, 3, 3),
(58, 23, 2, 1),
(59, 23, 2, 2),
(60, 23, 3, 3),
(61, 1, 2, 1),
(62, 1, 2, 2),
(63, 1, 3, 3),
(64, 24, 2, 1),
(65, 24, 2, 2),
(66, 24, 3, 3);

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`OrderId`, `OrderDate`, `TotalPrice`, `CreatedAt`, `AccountId`, `QRCode`, `used`) VALUES
(1, '2021-12-29', 145000, '2021-12-29', 0, '74o55u395EaXq7R8d1KW', 1),
(24, '2021-12-12', 145000, '2021-12-29', 1, 'uULR4603p7831pxh8te9', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
