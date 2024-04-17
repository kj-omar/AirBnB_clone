-- setup test database, and corresponding user(s)
-- create the test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges for hbnb_test_db db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant only SELECT privileges on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
