-- A script to create a database --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user in localhost and set password --
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- set privileges for the user --
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- set SELECT privileges for user hbnb_test on performance_schema --
GRANT SELECT ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
