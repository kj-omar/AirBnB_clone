-- Prepares a MySQL server for the AirBnB_clone_v2
-- Database: hbnb_dev_db
-- New user: hbnb_dev

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the new user
GRANT ALL PRIVILEGES ON  `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the new user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to ensure that all changes take effect
FLUSH PRIVILEGES;