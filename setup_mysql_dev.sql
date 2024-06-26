-- The script that prepares a MySQL server for the project as development environment
-- Create a database for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a user for the project
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on the project database to the project user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
-- Flush privileges
FLUSH PRIVILEGES;

