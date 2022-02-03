-- SQL script that creates a table "unique_id" in database "hbtn_0d_2"
-- id INT UNIQUE with default value 1
-- name VARCHAR(256)

CREATE TABLE IF NOT EXISTS `unique_id` (
  `id` INT UNIQUE DEFAULT 1,
  `name` VARCHAR(256)
);
