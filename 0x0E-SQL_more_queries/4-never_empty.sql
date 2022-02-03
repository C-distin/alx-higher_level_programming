-- SQL script that creates a table "id_not_null" in database "hbtn_0d_2"
-- id INT with default value 1
-- name VARCHAR(256)

CREATE TABLE IF NOT EXISTS `id_not_null` (
  `id` INT DEFAULT 1,
  `name` VARCHAR(256)
);
