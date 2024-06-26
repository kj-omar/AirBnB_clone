-- A script to create a database --


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user in localhost and set password --
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- set privileges for the user --
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- set SELECT privileges for user hbnb_dev on performance_schema --
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
