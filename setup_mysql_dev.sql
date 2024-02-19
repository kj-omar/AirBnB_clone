-- creates a database and a new user for the dev env
-- and grants specified privileges for said user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'Dev@8981';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
