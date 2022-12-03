#!/usr/bin/python3


import MySQLdb
from sys import argv

''' a script that lists all states from the database'''
if __name__ == "__main__":
    con = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDERED BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
