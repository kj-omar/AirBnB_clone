-- create a database and user and grant them previliges
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
Create USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.*
TO 'hbnb_dev'@'localhost';
