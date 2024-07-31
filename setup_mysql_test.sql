-- script that prepares a MySQL server for the project as test environment
-- Create a database for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a user for the project
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on the project database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
-- Flush privileges
FLUSH PRIVILEGES;
