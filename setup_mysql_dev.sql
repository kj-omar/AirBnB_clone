-- Script that prepares MySQL server for project

-- Creating project database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create new user on local MySQL server
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting new users privileges on system db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Granting new user privilegeson new db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Refreshing
FLUSH PRIVILEGES;
