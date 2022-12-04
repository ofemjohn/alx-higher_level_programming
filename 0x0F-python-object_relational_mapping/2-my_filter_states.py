#!/usr/bin/python3

import MySQLdb
import sys


''' script that takes in argument and display all values
in the state table
'''
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINRY'{}' ORDERED BY id ASC"
            .format(sys.argv[4]))
    fetch = cur.fetchall()
    for i in fetch:
        print(i)
    cur.close()
    db.close()
