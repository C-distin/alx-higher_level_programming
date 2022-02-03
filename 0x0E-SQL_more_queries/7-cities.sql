-- SQL script that creates a database "hbtn_0d_usa" and table "cities"
-- id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY
-- state_id INT NOT NULL FORIGN KEY REFERENCES states(id)
-- name VARCHAR(256) NOT NULL

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
  `id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `state_id` INT NOT NULL FORIEGN KEY REFERENCES hbtn_0d_usa.states(id),
  `name` VARCHAR(256) NOT NULL,
);
