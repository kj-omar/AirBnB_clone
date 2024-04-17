-- setup necessary dev database, and corresponding users automatially
-- create the dev database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create dev user, and their password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- dev user has all privileges for hbnb_dev db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- dev user has only SELECT privileges on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
