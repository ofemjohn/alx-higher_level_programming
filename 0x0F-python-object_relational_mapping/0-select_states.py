#!/usr/bin/python3


import MySQLdb
from sys import argv

''' a script that lists all states from the database'''
if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDERED BY id ASC")
    d_b = cursor.fetchall()
    for i in d_b:
        print(i)
    cursor.close()
    d_b.close()
