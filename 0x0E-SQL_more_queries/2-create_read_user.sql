-- SQL script that creates a new database "hbtn_0d_2" and new user "user_0d_2"
-- user has only SELECT priviledges on database "hbtn_0d_2"
-- user has password "user_0d_2_pwd"

CREATE DATABSE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
