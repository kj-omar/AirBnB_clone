# Connect to the MySQL server as root (adjust the credentials if needed)
db_connection = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='your_root_password'
)

# Create a cursor object to execute queries
cursor_obj = db_connection.cursor()

# Create the database if it doesn't exist
cursor_obj.execute("CREATE DATABASE IF NOT EXISTS hbnb_test_db")

# Create the user if it doesn't exist and set the password
cursor_obj.execute("CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'")

# Grant all privileges on hbnb_test_db to hbnb_test
cursor_obj.execute("GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'")

# Grant SELECT privilege on performance_schema to hbnb_test
cursor_obj.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'")

# Flush privileges to apply the changes
cursor_obj.execute("FLUSH PRIVILEGES")

# Close the cursor and database connection
cursor_obj.close()
db_connection.close()
