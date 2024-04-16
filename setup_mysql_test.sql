-- a script that prepares a MySQL server for the project.

-- Creates a Database if it does not exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a user if it does not exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges to user hbnb_test on hbnb_test_db database.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privileges to user hbnb_test on performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
