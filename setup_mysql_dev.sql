-- Creates a MySQL server with:
--   Database: hbnb_dev_db
--   User: hbnb_dev
--   Password: hbnb_dev_pwd
--   Host: localhost
-- Grants all privileges for the user hbnb_dev on the database hbnb_dev_db.
-- Grants SELECT privilege for the user hbnb_dev on the performance_schema database.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
   ON `hbnb_dev_db`.*
   TO 'hbnb_dev'@'localhost'
   IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT
   ON `performance_schema`.*
   TO 'hbnb_dev'@'localhost'
   IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
