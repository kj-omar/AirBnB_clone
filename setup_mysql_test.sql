-- Script that prepares MySQL server for project

-- Creating project database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create new user on local MySQL server
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting new users privileges on system db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Granting new user privilegeson new db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';

-- Refreshing
FLUSH PRIVILEGES;
