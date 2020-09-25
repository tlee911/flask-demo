DROP DATABASE IF EXISTS demo;

CREATE DATABASE demo;
USE demo;

CREATE TABLE results (
  `id` int not null AUTO_INCREMENT,
  `input` varchar(255) not null,
  `result` int not null,
  `created` datetime not null default CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
)