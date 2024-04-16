-- Create a new Mysql database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user 'hbnb_dev'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges for user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privilege for user 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;