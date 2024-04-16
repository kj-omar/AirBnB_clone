-- a script that prepares a MySQL server for the project.

-- Creates a Database if it does not exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a user if it does not exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges to user hbnb_dev on hbnb_dev_db database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grants SELECT privileges to user hbnb_dev on performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
