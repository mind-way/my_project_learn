-- MySQL 08.29  Distrib 8.0.17 for Win64 (x64)
--
-- Host: localhost    Database:news
-- ----------------------------------------------
-- server version    8.0.17

create database if not exists news;
use news;

/*
    News information database, used to store the title, description,
    URL address of the main news downloaded from various news websites,
    and account-related information for mail and wechat sending.
    total of six tables,user,email,wechat,kejixun,kuaikeji.
*/

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*SET character_set_client = utf8*/
CREATE TABLE `user` (
	`user_id` int(11) NOT NULL AUTO_INCREMENT,
	`user_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
	`user_psd` longtext NOT NULL,
	`sex` varchar(2) DEFAULT NULL,
	`age` int(5) DEFAULT NULL,
	`hobby` varchar(255),
	PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `email`
--

DROP TABLE IF EXISTS `email`;
/*SET character_set_client = utf8*/
CREATE TABLE `email` (
	`email_id` int(11) NOT NULL AUTO_INCREMENT,
	`email_host` varchar(32) NOT NULL,
	`email_port` int(5) NOT NULL,
	`login_email` varchar(32) NOT NULL,
	`login_psd` varchar(32),
	`send_email` varchar(32),
	`send_info` varchar(255),
	PRIMARY KEY (`email_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `wechat`
--

DROP TABLE IF EXISTS `wechat`;
/*SET character_set_client = utf8*/
CREATE TABLE `wechat` (
	`wechat_id` int(11) NOT NULL AUTO_INCREMENT,
	`login_user` varchar(32) NOT NULL,
	`send_user` varchar(32) NOT NULL,
	`send_room` varchar(32) NOT NULL,
	`send_info` varchar(255) NOT NULL,
	PRIMARY KEY (`wechat_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `kuaikj`
--

DROP TABLE IF EXISTS `kuaikeji`;
/*SET character_set_client = utf8*/
CREATE TABLE `kuaikeji` (
	`kuaikj_id` int(11) NOT NULL AUTO_INCREMENT,
	`today` varchar(16),
	`title` varchar(128),
	`brief` varchar(255),
	`news_url` varchar(128),
	`from_url` varchar(128),
	`send_time` datetime DEFAULT NULL,
	PRIMARY KEY (`kuaikj_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `kejixun`
--

DROP TABLE IF EXISTS `kejixun`;
/*SET character_set_client = utf8*/
CREATE TABLE `kejixun` (
	`kejx_id` int(11) NOT NULL AUTO_INCREMENT,
	`today` varchar(16),
	`title` varchar(128),
	`brief` varchar(255),
	`news_url` varchar(128),
	`from_url` varchar(128),
	`send_time` datetime DEFAULT NULL,
	PRIMARY KEY (`kejx_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
