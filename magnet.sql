/*
Navicat MySQL Data Transfer

Source Server         : 搬瓦工
Source Server Version : 50548
Source Host           : 104.224.175.113:3306
Source Database       : magnet

Target Server Type    : MYSQL
Target Server Version : 50548
File Encoding         : 65001

Date: 2017-06-19 11:07:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for app_magnet
-- ----------------------------
DROP TABLE IF EXISTS `app_magnet`;
CREATE TABLE `app_magnet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mgTitle` varchar(255) NOT NULL,
  `mgSize` int(11) NOT NULL,
  `mgList` varchar(255) NOT NULL,
  `mgCreate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mgHot` int(11) NOT NULL,
  `mgLable` varchar(255) NOT NULL,
  `mgList_1` varchar(255) NOT NULL COMMENT '迅雷链接',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=80344 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for app_nodess
-- ----------------------------
DROP TABLE IF EXISTS `app_nodess`;
CREATE TABLE `app_nodess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(128) NOT NULL,
  `node_type` int(3) NOT NULL,
  `node_server` varchar(128) NOT NULL,
  `node_method` varchar(64) NOT NULL,
  `node_info` varchar(128) NOT NULL,
  `node_status` varchar(128) NOT NULL,
  `node_order` int(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for app_userbind
-- ----------------------------
DROP TABLE IF EXISTS `app_userbind`;
CREATE TABLE `app_userbind` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `openid` varchar(128) NOT NULL,
  `create` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `modify` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for app_usercode
-- ----------------------------
DROP TABLE IF EXISTS `app_usercode`;
CREATE TABLE `app_usercode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(128) NOT NULL,
  `code` varchar(128) NOT NULL,
  `create` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for magnet
-- ----------------------------
DROP TABLE IF EXISTS `magnet`;
CREATE TABLE `magnet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mgTitle` varchar(255) NOT NULL,
  `mgSize` int(11) NOT NULL,
  `mgList` varchar(255) NOT NULL,
  `mgCreate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mgHot` int(11) NOT NULL,
  `mgLable` varchar(255) NOT NULL,
  `mgList_1` varchar(255) NOT NULL COMMENT '迅雷链接',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=78215 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for node_ss
-- ----------------------------
DROP TABLE IF EXISTS `node_ss`;
CREATE TABLE `node_ss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(128) NOT NULL,
  `node_type` int(3) NOT NULL,
  `node_server` varchar(128) NOT NULL,
  `node_method` varchar(64) NOT NULL,
  `node_info` varchar(128) NOT NULL,
  `node_status` varchar(128) NOT NULL,
  `node_order` int(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_bind
-- ----------------------------
DROP TABLE IF EXISTS `user_bind`;
CREATE TABLE `user_bind` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `openid` varchar(128) NOT NULL,
  `create` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  `modify` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_code
-- ----------------------------
DROP TABLE IF EXISTS `user_code`;
CREATE TABLE `user_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(128) NOT NULL,
  `code` varchar(128) NOT NULL,
  `create` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
