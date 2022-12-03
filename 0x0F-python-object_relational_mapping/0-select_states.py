#!/usr/bin/python3


import MySQLdb
import sys

''' a script that lists all states from the database'''
if __name__ == "__main__":
    data_base = MySQLdb.connect(
            host="localhost", port=3306, username=argv[1],
            password=argv[2], database_name=argv[3])
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states ORDERED BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
