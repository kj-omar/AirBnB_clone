import unittest
import MySQLdb

class TestMySQLServerPreparationForProject(unittest.TestCase):
    def setUp(self):
        """ Connect to MySQL server"""
        self.connection = MySQLdb.connect(host='localhost', user='root', passwd='password')
        self.cursor = self.connection.cursor()

      """Ensure database and user don't already exist"""
        self.cursor.execute("DROP DATABASE IF EXISTS hbnb_test_db")
        self.cursor.execute("DROP USER IF EXISTS 'hbnb_test'@'localhost'")
        self.connection.commit()

    def test_mysql_setup_script_for_project(self):
        
        """Check if the database and user were created with correct privileges"""
        self.cursor.execute("SHOW DATABASES LIKE 'hbnb_test_db'")
        db_exists = self.cursor.fetchone()
        self.assertIsNotNone(db_exists)

        self.cursor.execute("SELECT User FROM mysql.user WHERE User='hbnb_test' AND Host='localhost'")
        user_exists = self.cursor.fetchone()
        self.assertIsNotNone(user_exists)

        self.cursor.execute("SHOW GRANTS FOR 'hbnb_test'@'localhost'")
        user_grants = self.cursor.fetchall()
        self.assertIn("GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'", user_grants)
        self.assertIn("GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'", user_grants)
        self.assertIn("GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'", user_grants)

    def tearDown(self):
       """Clean up"""
        self.cursor.execute("DROP DATABASE IF EXISTS hbnb_test_db")
        self.cursor.execute("DROP USER IF EXISTS 'hbnb_test'@'localhost'")
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    unittest.main()

