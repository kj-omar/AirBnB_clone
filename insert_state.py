#!/usr/bin/python3
""""""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="HBNB_MYSQL_USER",
        passwd="HBNB_MYSQL_PWD",
        db="HBNB_MYSQL_DB",
        charset="utf8"
    )

    curr = conn.cursor()
    curr.execute(f"""INSERT INTO states (name) VALUES ('California')""")
    conn.commit()
    curr.close()
    conn.close()
