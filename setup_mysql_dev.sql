-- Drop the user if it exists
DROP USER IF EXISTS 'hbnb_dev'@'localhost';

-- Create the user
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant SHOW DATABASES privilege to the user
GRANT SHOW DATABASES ON *.* TO 'hbnb_dev'@'localhost';

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
SHOW GRANTS FOR 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hafssaelk';
SELECT user FROM mysql.user WHERE user = 'hbnb_dev' AND host = 'localhost';
