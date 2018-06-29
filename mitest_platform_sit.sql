/*
Navicat MySQL Data Transfer

Source Server         : ALIUAT_mmqb
Source Server Version : 50716
Source Host           : 192.168.10.2:3306
Source Database       : mitest_platform_sit

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2018-06-29 17:20:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('b1610174bbc7');

-- ----------------------------
-- Table structure for env_info
-- ----------------------------
DROP TABLE IF EXISTS `env_info`;
CREATE TABLE `env_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `env_name` varchar(50) NOT NULL,
  `base_host` varchar(50) DEFAULT NULL,
  `dubbo_zookeeper` varchar(50) DEFAULT NULL,
  `mq_key` varchar(100) DEFAULT NULL,
  `db_connect` varchar(200) DEFAULT NULL,
  `remote_host` varchar(50) DEFAULT NULL,
  `disconf_host` varchar(50) DEFAULT NULL,
  `redis_connect` varchar(200) DEFAULT NULL,
  `simple_desc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `env_name` (`env_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of env_info
-- ----------------------------
INSERT INTO `env_info` VALUES ('1', '2018-06-25 14:54:08', null, 'mock', 'http://99.48.58.241', null, null, null, null, null, null, '测试mock用');

-- ----------------------------
-- Table structure for module_info
-- ----------------------------
DROP TABLE IF EXISTS `module_info`;
CREATE TABLE `module_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `module_name` varchar(80) NOT NULL,
  `test_user` varchar(50) DEFAULT NULL,
  `simple_desc` varchar(100) DEFAULT NULL,
  `system_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `system_id` (`system_id`),
  CONSTRAINT `module_info_ibfk_1` FOREIGN KEY (`system_id`) REFERENCES `system_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of module_info
-- ----------------------------
INSERT INTO `module_info` VALUES ('4', null, null, '申请', null, null, '1');

-- ----------------------------
-- Table structure for project_info
-- ----------------------------
DROP TABLE IF EXISTS `project_info`;
CREATE TABLE `project_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `project_name` varchar(50) NOT NULL,
  `simple_desc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_name` (`project_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of project_info
-- ----------------------------
INSERT INTO `project_info` VALUES ('3', '2018-06-21 16:37:30', '2018-06-21 16:45:40', '雅俏丽', '666');
INSERT INTO `project_info` VALUES ('4', '2018-06-25 16:16:34', null, '宝生', null);

-- ----------------------------
-- Table structure for system_info
-- ----------------------------
DROP TABLE IF EXISTS `system_info`;
CREATE TABLE `system_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `system_name` varchar(50) NOT NULL,
  `test_user` varchar(50) DEFAULT NULL,
  `dev_user` varchar(50) DEFAULT NULL,
  `publish_app` varchar(50) DEFAULT NULL,
  `simple_desc` varchar(100) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `system_info_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_info
-- ----------------------------
INSERT INTO `system_info` VALUES ('1', null, '2018-06-25 18:13:06', 'wallet_system2', null, null, null, null, null);
INSERT INTO `system_info` VALUES ('3', '2018-06-25 11:05:03', null, 'wallet_system1', null, null, null, '123321', '4');
INSERT INTO `system_info` VALUES ('4', '2018-06-25 11:41:14', null, 'wallet_system2', null, null, null, '123321', '4');
INSERT INTO `system_info` VALUES ('5', '2018-06-25 15:52:43', '2018-06-25 18:13:53', 'wallet_system3', null, null, null, null, '3');
INSERT INTO `system_info` VALUES ('6', '2018-06-25 15:58:03', null, 'wallet_system4', 'hanxueyao', 'hanxueyao', 'wallet', null, '3');

-- ----------------------------
-- Table structure for test_report
-- ----------------------------
DROP TABLE IF EXISTS `test_report`;
CREATE TABLE `test_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `start_at` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `run_type` int(11) DEFAULT NULL,
  `report` longtext NOT NULL,
  `system_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `system_id` (`system_id`),
  CONSTRAINT `test_report_ibfk_1` FOREIGN KEY (`system_id`) REFERENCES `system_info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test_report
-- ----------------------------

-- ----------------------------
-- Table structure for testcase_info
-- ----------------------------
DROP TABLE IF EXISTS `testcase_info`;
CREATE TABLE `testcase_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `testcase_name` varchar(100) NOT NULL,
  `type` int(11) NOT NULL,
  `include` varchar(400) DEFAULT NULL,
  `request` text NOT NULL,
  `testsuite_id` int(11) DEFAULT NULL,
  `module_id` int(11) DEFAULT NULL,
  `system_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `module_id` (`module_id`),
  KEY `testsuite_id` (`testsuite_id`),
  KEY `system_id` (`system_id`),
  CONSTRAINT `testcase_info_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module_info` (`id`),
  CONSTRAINT `testcase_info_ibfk_2` FOREIGN KEY (`testsuite_id`) REFERENCES `testsuite_info` (`id`),
  CONSTRAINT `testcase_info_ibfk_3` FOREIGN KEY (`system_id`) REFERENCES `system_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testcase_info
-- ----------------------------
INSERT INTO `testcase_info` VALUES ('1', '2018-06-25 14:52:36', null, 'myMock', '1', null, '{\"name\":\"myMock\",\"config\":{\"request\":{\"base_url\":\"http://99.48.58.31\",\"headers\":{\"Content-Type\":\"application/json;charset=UTF-8\"}},\"variables\":[{\"pageSize\":1},{\"currentPage\":1}],\"parameters\":[],\"name\":\"testset description\"},\"testcases\":[{\"request\":{\"json\":{},\"url\":\"mock/config/queryProject\",\"headers\":{\"Content-Type\":\"application/json\"},\"method\":\"POST\"},\"extract\":[{\"op\":\"content.desc.ups.0\"}],\"validate\":[{\"eq\":[\"status_code\",200]},{\"eq\":[\"headers.Content-Type\",\"application/json\"]},{\"eq\":[\"content.code\",\"000\"]}],\"variables\":[],\"name\":\"queryProject\"},{\"request\":{\"json\":{\"pageSize\":\"$pageSize\",\"interfaceName\":\"demo_post_json\",\"currentPage\":\"$currentPage\",\"projectName\":\"ups\",\"op\":\"$op\"},\"url\":\"http://99.48.58.241/mock/config/queryMock\",\"headers\":{},\"method\":\"POST\"},\"extract\":[{\"tableData\":\"content.tableData\"}],\"validate\":[{\"eq\":[\"status_code\",200]},{\"eq\":[\"headers.Content-Type\",\"application/json\"]},{\"eq\":[\"content.code\",\"000\"]}],\"variables\":[],\"name\":\"queryMock\"}]}', '1', '4', '1');
INSERT INTO `testcase_info` VALUES ('2', '2018-06-25 17:23:46', null, 'myMock2', '1', null, '{\"name\":\"myMock\",\"config\":{\"request\":{\"base_url\":\"http://99.48.58.241\",\"headers\":{\"Content-Type\":\"application/json;charset=UTF-8\"}},\"variables\":[{\"pageSize\":1},{\"currentPage\":1}],\"parameters\":[],\"name\":\"testset description\"},\"testcases\":[{\"request\":{\"json\":{},\"url\":\"mock/config/queryProject\",\"headers\":{\"Content-Type\":\"application/json\"},\"method\":\"POST\"},\"extract\":[{\"op\":\"content.desc.ups.0\"}],\"validate\":[{\"eq\":[\"status_code\",200]},{\"eq\":[\"headers.Content-Type\",\"application/json\"]},{\"eq\":[\"content.desc\",{\"bds\":[],\"capital\":[\"businessapi/ops/file/upload/2/xydadcce31a92e8b1c5\",\"mm/credit/getUnderWrittingStatus\",\"mm/credit/getUnderWrittingStatus/2/xydadcce31a92e8b1c5\",\"mm/credit/queryAccountInfo\",\"mm/credit/queryAccountInfo/2/xydadcce31a92e8b1c5\",\"mm/credit/saveUserInfo/2/xydadcce31a92e8b1c5\",\"mm/credit/withdrawDeposit/2\"],\"ups\":[\"demo_get\",\"demo_post\",\"demo_post_form\",\"demo_post_json\"]}]}],\"variables\":[],\"name\":\"queryProject\"},{\"request\":{\"json\":{\"pageSize\":\"$pageSize\",\"interfaceName\":\"demo_post_json\",\"currentPage\":\"$currentPage\",\"projectName\":\"ups\",\"op\":\"$op\"},\"url\":\"http://99.48.58.241/mock/config/queryMock\",\"headers\":{},\"method\":\"POST\"},\"extract\":[{\"tableData\":\"content.tableData\"}],\"validate\":[{\"eq\":[\"status_code\",200]},{\"eq\":[\"headers.Content-Type\",\"application/json\"]},{\"eq\":[\"content.code\",\"000\"]}],\"variables\":[],\"name\":\"queryMock\"}]}', '1', '4', '1');
INSERT INTO `testcase_info` VALUES ('3', '2018-06-26 11:23:37', null, '333', '1', null, '{\"name\":\"myMock\",\"config\":{\"request\":{\"base_url\":\"http://99.48.58.241\",\"headers\":{\"Content-Type\":\"application/json;charset=UTF-8\"}},\"variables\":[{\"pageSize\":1},{\"currentPage\":1}],\"parameters\":[],\"name\":\"testset description\"},\"testcases\":[{\"request\":{\"json\":{},\"url\":\"mock/config/queryProject\",\"headers\":{\"Content-Type\":\"application/json\"},\"method\":\"POST\"},\"extract\":[{\"op\":\"content.desc.ups.0\"}],\"validate\":[{\"eq\":[\"status_code\",200]},{\"eq\":[\"headers.Content-Type\",\"application/json\"]},{\"eq\":[\"content.desc\",{\"capital\":[\"businessapi/ops/file/upload/2/xydadcce31a92e8b1c5\",\"mm/credit/getUnderWrittingStatus\",\"mm/credit/getUnderWrittingStatus/2/xydadcce31a92e8b1c5\",\"mm/credit/queryAccountInfo\",\"mm/credit/queryAccountInfo/2/xydadcce31a92e8b1c5\",\"mm/credit/saveUserInfo/2/xydadcce31a92e8b1c5\",\"mm/credit/withdrawDeposit/2\"],\"ups\":[\"demo_get\",\"demo_post\",\"demo_post_form\",\"demo_post_json\"]}]}],\"variables\":[],\"name\":\"queryProject\"},{\"request\":{\"json\":{\"pageSize\":\"$pageSize\",\"interfaceName\":\"demo_post_json\",\"currentPage\":\"$currentPage\",\"projectName\":\"ups\",\"op\":\"$op\"},\"url\":\"http://99.48.58.241/mock/config/queryMock\",\"headers\":{},\"method\":\"POST\"},\"extract\":[{\"tableData\":\"content.tableData\"}],\"validate\":[{\"eq\":[\"status_code\",200]},{\"eq\":[\"headers.Content-Type\",\"application/json\"]},{\"eq\":[\"content.code\",\"000\"]}],\"variables\":[],\"name\":\"queryMock\"}]}', '1', '4', '1');
INSERT INTO `testcase_info` VALUES ('4', '2018-06-26 17:44:46', null, '用例名称A', '1', null, '{\"name\": \"用例名称A\", \"testcases\": [{\"validate\": [{\"eq\": [\"content.code\", \"000\"]}], \"variables\": [{\"pageSize\": 2}, {\"interfaceName\": \"demo_post_json\"}], \"request\": {\"url\": \"/mock/config/queryMock\", \"headers\": {\"Content-Type\": \"application/json\", \"oops\": \"oops\"}, \"json\": {\"pageSize\": \"${pageSize}\", \"interfaceName\": \"${demo_post_json}\", \"projectName\": \"ups\", \"currentPage\": 1}, \"method\": \"POST\"}, \"extract\": [{\"tableData\": \"content.tableData\"}], \"name\": \"这是一个测试步骤名称\"}], \"config\": {\"request\": {\"headers\": {\"Content-Type\": \"application/json;charset=UTF-8\"}, \"base_url\": \"\"}}}', '1', '4', '1');
INSERT INTO `testcase_info` VALUES ('8', '2018-06-26 17:50:50', null, '用例名称A', '1', null, '{\"config\": {\"request\": {\"base_url\": \"\", \"headers\": {\"Content-Type\": \"application/json;charset=UTF-8\"}}}, \"testcases\": [{\"validate\": [{\"eq\": [\"content.code\", \"000\"]}], \"name\": \"这是一个测试步骤名称\", \"extract\": [{\"tableData\": \"content.tableData\"}], \"variables\": [{\"pageSize\": 2}, {\"interfaceName\": \"demo_post_json\"}], \"request\": {\"url\": \"/mock/config/queryMock\", \"json\": {\"pageSize\": \"$pageSize\", \"projectName\": \"ups\", \"interfaceName\": \"$interfaceName\", \"currentPage\": 1}, \"headers\": {\"oops\": \"oops\", \"Content-Type\": \"application/json\"}, \"method\": \"POST\"}}], \"name\": \"用例名称A\"}', '1', '4', '1');
INSERT INTO `testcase_info` VALUES ('9', '2018-06-26 18:05:16', null, '用例名称A', '1', null, '{\"name\": \"用例名称A\", \"config\": {\"request\": {\"headers\": {\"Content-Type\": \"application/json;charset=UTF-8\"}, \"base_url\": \"\"}}, \"testcases\": [{\"variables\": [{\"pageSize\": 2}, {\"interfaceName\": \"demo_post_json\"}], \"name\": \"步骤-1\", \"request\": {\"url\": \"/mock/config/queryMock\", \"json\": {\"pageSize\": \"$pageSize\", \"currentPage\": 1, \"projectName\": \"ups\", \"interfaceName\": \"$interfaceName\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\", \"oops\": \"oops\"}}, \"extract\": [{\"tableData\": \"content.tableData\"}], \"validate\": [{\"eq\": [\"content.code\", \"000\"]}]}]}', '1', '4', '1');
INSERT INTO `testcase_info` VALUES ('10', '2018-06-29 15:41:44', null, '用例名称B', '1', null, '{\"name\": \"用例名称A\", \"config\": {\"request\": {\"headers\": {\"Content-Type\": \"application/json;charset=UTF-8\"}, \"base_url\": \"\"}}, \"testcases\": [{\"variables\": [{\"pageSize\": 2}, {\"interfaceName\": \"demo_post_json\"}], \"name\": \"步骤-1\", \"request\": {\"url\": \"/mock/config/queryMock\", \"json\": {\"pageSize\": \"$pageSize\", \"currentPage\": 1, \"projectName\": \"ups\", \"interfaceName\": \"$interfaceName\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\", \"oops\": \"oops\"}}, \"extract\": [{\"tableData\": \"content.tableData\"}], \"validate\": [{\"eq\": [\"content.code\", \"000\"]},{\"eq\": [\"content.db_result\", \"000\"]}],\"setup_hooks\": [\"${sleep_N_secs(3)}\"], \"teardown_hooks\": [\"${teardown_db_select($response, text111)}\"]}]}', '1', '4', '1');

-- ----------------------------
-- Table structure for testsuite_info
-- ----------------------------
DROP TABLE IF EXISTS `testsuite_info`;
CREATE TABLE `testsuite_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `testsuite_name` varchar(80) NOT NULL,
  `simple_desc` varchar(100) DEFAULT NULL,
  `module_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `module_id` (`module_id`),
  CONSTRAINT `testsuite_info_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `module_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testsuite_info
-- ----------------------------
INSERT INTO `testsuite_info` VALUES ('1', '2018-06-26 14:14:59', null, '测试集1', '1123', '4');
