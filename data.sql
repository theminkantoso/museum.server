-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 04, 2022 lúc 06:07 PM
-- Phiên bản máy phục vụ: 10.4.17-MariaDB
-- Phiên bản PHP: 7.4.15

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

--
-- Đang đổ dữ liệu cho bảng `account`
--

INSERT INTO `account` (`AccountId`, `email`, `Password`, `RoleId`, `isActivated`, `confirmedAt`, `GoogleId`, `CreateAt`, `UpdateAt`) VALUES
(1, 'trangco19621962@gmail.com', 'sha256$iUtOAp2l3Fot4W6j$e865a998d8ab5d9b98db60448d64b33892e4790863c80bfa42c0de4c80886595', 1, 1, '2021-12-28 19:28:18', NULL, NULL, NULL);

--
-- Đang đổ dữ liệu cho bảng `agegroup`
--

INSERT INTO `agegroup` (`GroupId`, `Description`, `Price`) VALUES
(1, 'children', 50000),
(2, 'adult', 80000),
(3, 'elderly', 65000);

--
-- Đang đổ dữ liệu cho bảng `artifact`
--

INSERT INTO `artifact` (`ArtifactId`, `Name`, `Description`, `Level`, `ImageId`) VALUES
(1, 'Đường cách mệnh', 'Đường cách mệnh là tác phẩm ghi lại những bài giảng của Nguyễn Ái Quốc cho các lớp đào tạo cán bộ tại Quảng Châu do Bộ tuyên truyền của Hội Liên hiệp các dân tộc bị áp bức ở Á Đông phát hành vào đầu năm 1927. Cuốn sách này đánh dấu cho sự truyền bá Chủ nghĩa Marx – Lenin vào Việt Nam những năm 20 của thế kỷ XX.', 0, 1),
(2, 'Trống đồng Cảnh Thịnh', 'Trống đồng Cảnh Thịnh được đúc theo kỹ thuật khuôn sáp, nặng 32 kg, cao 37,4 cm, đường kính khoảng 49 cm. Mặt trống cong vồng hình chỏm cầu, tâm mặt trống đúc nổihình vòng tròn kép. Thân trống hình trụ, phình nhẹ ở giữa, và được chia thành ba phần tương đối đều nhau, ngăn cách bằng hai đường gờ nổi hình sống trâu. Tương ứng với mỗi phần là một băng hoa văn trang trí. Ngoài các đồ án phụ trang trí đường diềm như băng hoa chanh, nhũ đinh, hồi văn chữ T và văn như ý, đề tài trang trí chủ đạo trên trống xuất hiện ở hai băng: băng trên cùng đúc nổi đề tài Tứ linh (Long, Lân, Quy, Phượng) mang ý nghĩa biểu trưng cho đất nước thái bình thịnh trị, xã hội an lạc, mưa thuận gió hòa, mùa màng tốt tươi, con người được no đủ, sống lâu.', 0, 2),
(3, 'Cây đèn hình người quỳ', 'Cây đèn hình người quỳ bằng đồng, thuộc văn hóa Đông Sơn, được thể hiện theo hình tượng một người đàn ông mình trần đóng khố tư thế đang quỳ, hai tay nâng đĩa đèn. Tượng có khuôn mặt bầu, mắt mở to, miệng hơi mỉm cười, quanh môi có ria mép. Đầu tượng được gắn vương miện, tóc để chỏm.', 0, 3),
(4, 'Mộ thuyền Việt Khê', 'Mộ thuyền Việt Khê, thuộc văn hóa Đông Sơn, là loại quan tài bằng thân cây khoét rỗng, có kích thước lớn nhất trong số những mộ thuyền đã phát hiện ở Việt Nam. Bên trong mộ chứa 109 đồ tùy táng gồm chủ yếu là đồ đồng, bao gồm các loại hình vũ khí, nhạc khí, công cụ lao động và đồ dùng sinh hoạt.', 0, 4),
(5, 'Chuông Vân Bản', 'Chuông chùa Vân Bản, thời Trần là chiếc chuông cổ nhất, đồng thời có kích thước lớn nhất, uy nghi nhất của nền văn minh Đại Việt.', 0, 5),
(6, 'Ấn vàng Sắc mênhj chi bảo', 'Ấn vàng Sắc mệnh chi bảo là biểu trưng quyền lực của triều đình nhà Nguyễn, dùng để đóng trên các loại sắc phong của vương triều. Mỗi hình dấu của ấn trên văn bản được coi là một văn bản hoàn chỉnh và trung thực nhất. ', 0, 6),
(7, 'Bản thảo Lời kêu gọi toàn quốc kháng chiến', 'Lời kêu gọi toàn quốc kháng chiến, do Hồ Chí Minh soạn thảo, là lời phát động cuộc kháng chiến chống Pháp vào cuối năm 1946, sau khi những nỗ lực đàm phán hòa bình giữa Việt Nam Dân chủ Cộng hòa với Pháp, vào giữa năm 1946, để công nhận một nước Việt Nam độc lập, không thành công. Lời kêu gọi này được phát ra vào sáng ngày 20 tháng 12 năm 1946. Đêm hôm trước - ngày 19 tháng 12, khi chiến sự bùng nổ - là ngày được gọi là Toàn quốc kháng chiến.', 0, 7),
(8, 'Bia Võ Cạnh', 'Bia Võ Cạnh là tấm bia cổ nhất được tìm thấy của Vương quốc Chăm Pa, đồng thời cùng là tấm bia cổ nhất ở Việt Nam và một trong những tấm bia cổ nhất Đông Nam Á. Tấm bia được Thủ tướng Chính phủ công nhận là bảo vật quốc gia trong đợt thứ hai năm 2013. Bia Võ Cạnh được phát hiện bên cạnh nền móng một công trình bằng gạch ở giữa hai làng Phú Văn (hoặc Phố Văn) và Phú Vinh, thuộc Tổng Xương Hà, Vĩnh Xương, Khánh Hòa (ngày nay là làng Võ Cạnh, xã Vĩnh Trung, Nha Trang, Khánh Hòa)', 0, 8);

--
-- Đang đổ dữ liệu cho bảng `entryticket`
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
-- Đang đổ dữ liệu cho bảng `image`
--

INSERT INTO `image` (`ImageId`, `Name`, `Content`, `Url`, `Path`, `MimeType`) VALUES
(1, 'uong_cach_menh.jpg', 'Đường cách mệnh', 'uong_cach_menh.jpg', 'statics/images/uong_cach_menh.jpg', 'image/jpeg'),
(2, 'trong_ong_canh_thinh.jpg', 'Trống đồng Cảnh Thịnh', 'trong_ong_canh_thinh.jpg', 'statics/images/trong_ong_canh_thinh.jpg', 'image/jpeg'),
(3, 'cay_en_hinh_nguoi_quy.jpg', 'Cây đèn hình người quỳ', 'cay_en_hinh_nguoi_quy.jpg', 'statics/images/cay_en_hinh_nguoi_quy.jpg', 'image/jpeg'),
(4, 'Mo_Thuyen_Viet_Khe.jpg', 'Mộ thuyền Việt Khê', 'Mo_Thuyen_Viet_Khe.jpg', 'statics/images/Mo_Thuyen_Viet_Khe.jpg', 'image/jpeg'),
(5, 'Chuong_Van_Ban.jpg', 'Chuông Vân Bản', 'Chuong_Van_Ban.jpg', 'statics/images/Chuong_Van_Ban.jpg', 'image/jpeg'),
(6, 'An_vang_sac_menh_chi_bao.jpg', 'Ấn vàng Sắc mệnh chi bảo', 'An_vang_sac_menh_chi_bao.jpg', 'statics/images/An_vang_sac_menh_chi_bao.jpg', 'image/jpeg'),
(7, 'Loi_keu_goi_toan_quoc_khang_chien.jpg', 'Bản thào Lời kêu gọi toàn quốc kháng chiến', 'Loi_keu_goi_toan_quoc_khang_chien.jpg', 'statics/images/Loi_keu_goi_toan_quoc_khang_chien.jpg', 'image/jpeg'),
(8, 'bia_Vo_Canh.jpg', 'Bia Võ Cạnh', 'bia_Vo_Canh.jpg', 'statics/images/bia_Vo_Canh.jpg', 'image/jpeg'),
(9, 'am_cuoi_chuot.jpeg', 'Đám cưới chuột', 'am_cuoi_chuot.jpeg', 'statics/images/am_cuoi_chuot.jpeg', 'image/jpeg'),
(10, 'tranh_chu_An.jpg', 'Tranh chữ An', 'tranh_chu_An.jpg', 'statics/images/tranh_chu_An.jpg', 'image/jpeg'),
(11, 'vong_tay.jpg', 'Vòng tay chỉ đỏ', 'vong_tay.jpg', 'statics/images/vong_tay.jpg', 'image/jpeg'),
(12, 'sao_truc.jpg', 'Sáo trúc', 'sao_truc.jpg', 'statics/images/sao_truc.jpg', 'image/jpeg'),
(13, 'tranh_go.jpg', '', 'tranh_go.jpg', 'statics/images/tranh_go.jpg', 'image/jpeg'),
(14, 'but_long_viet_thu_phap.jpg', '', 'but_long_viet_thu_phap.jpg', 'statics/images/but_long_viet_thu_phap.jpg', 'image/jpeg'),
(15, 'non_la.jpg', '', 'non_la.jpg', 'statics/images/non_la.jpg', 'image/jpeg'),
(16, 'Tranh_cat.jpg', '', 'Tranh_cat.jpg', 'statics/images/Tranh_cat.jpg', 'image/jpeg'),
(17, 'su_kien_ky_uc_di_san.jpg', '', 'su_kien_ky_uc_di_san.jpg', 'statics/images/su_kien_ky_uc_di_san.jpg', 'image/jpeg'),
(18, 'Ho_Chi_Minh.jpg', '', 'Ho_Chi_Minh.jpg', 'statics/images/Ho_Chi_Minh.jpg', 'image/jpeg');

--
-- Đang đổ dữ liệu cho bảng `museumevent`
--

INSERT INTO `museumevent` (`EventId`, `Name`, `Description`, `OpenTime`, `CloseTime`, `EventDate`, `Poster`) VALUES
(1, 'Ký ức di sản', 'Sự kiện ký ức di sản sẽ diễn ra tới đây ', '08:00:00', '17:30:00', '2022-01-10', 17),
(2, 'Sự kiện Nguyễn Tất Thành - Hồ Chí Minh đi tìm đường cứu nước.Ý nghĩa lịch sử và giá trị thời đại', 'Kỷ niệm 111 năm Ngày Chủ tịch Hồ Chí Minh đi tìm đường cứu nước (5-6-1911/5-6-2022),tổ chức Hội thảo khoa học với chủ đề: “Sự kiện Nguyễn Tất Thành - Hồ Chí Minh đi tìm đường cứu nước. Ý nghĩa lịch sử và giá trị thời đại\"', '08:00:00', '17:30:00', '2022-06-05', 18);

--
-- Đang đổ dữ liệu cho bảng `orders`
--

INSERT INTO `orders` (`OrderId`, `OrderDate`, `TotalPrice`, `CreatedAt`, `AccountId`, `QRCode`, `used`, `type`) VALUES
(1, '2021-12-29', 145000, '2021-12-29', 0, '74o55u395EaXq7R8d1KW', 1, 0),
(24, '2021-12-12', 145000, '2021-12-29', 1, 'uULR4603p7831pxh8te9', 0, 0);

--
-- Đang đổ dữ liệu cho bảng `souvenir`
--

INSERT INTO `souvenir` (`SouvenirId`, `Name`, `Description`, `Price`, `Discount`, `ImageId`) VALUES
(1, 'Tranh đám cưới chuột', 'Bức tranh đám cưới chuột nổi tiếng được thực hiển bởi những nghệ nhân Đông Hồ. Theo các nghệ nhân làng tranh Đông Hồ thì bức tranh này có từ khoảng từ 500 năm trước. Bức tranh gồm có 12 con chuột và 1 con mèo. Ngoài chủ đạo là chuột và mèo, thì bức tranh còn có những loài vật khác như 1 con chim, 1 con cá và 1 con ngựa.', 50, NULL, 9),
(2, 'Tranh chữ An', 'Tranh chữ Đồng chữ An mang lại sự hạnh phúc, an khang, thịnh vượng', 200, NULL, 10),
(3, 'Vòng tay chỉ đỏ', 'Vòng tay chỉ đỏ mang lại may mắn, tài lộc', 15, NULL, 11),
(4, 'Sáo trúc', 'Sáo là nhạc cụ thổi hơi có từ thời kỳ cổ đại, rất nhiều nước trên thế giới sử dụng sáo với nhiều hình dáng và cấu tạo có thể khác nhau.', 50, NULL, 12),
(5, 'Tranh cát', 'Nghệ thuật tranh cát', 50, NULL, 16),
(6, 'Bút lông viết thư pháp', 'Bút lông viết thư pháp đẹp', 20, NULL, 14),
(7, 'Nón lá', 'Món đồ lưu niệm đậm chất văn hoá Việt Nam', 50, NULL, 15),
(8, 'Tranh gỗ treo trường', 'Tranh gỗ đẹp, ý nghĩa, mang lại phongc cách riêng cho ngôi nhà của bạn', 200, NULL, 13);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
