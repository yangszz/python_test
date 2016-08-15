
USE `test`;

/*Table structure for table `t_meishi` */

DROP TABLE IF EXISTS `t_meishi`;

CREATE TABLE `t_meishi` (
  `id` int(20) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `cailiao` varchar(255) DEFAULT NULL,
  `homeJpjUrl` varchar(255) DEFAULT NULL,
  `sourceUrl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sourceUrl` (`sourceUrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `t_meishi_child` */

DROP TABLE IF EXISTS `t_meishi_child`;

CREATE TABLE `t_meishi_child` (
  `id` int(20) NOT NULL,
  `main_id` int(20) DEFAULT NULL,
  `step` int(2) DEFAULT NULL,
  `step_desc` varchar(255) DEFAULT NULL,
  `jpgUrl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

