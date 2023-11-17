#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])

# Create a cursor
cursor = db.cursor()

# creating a query
cursor.execute("SELECT * FROM states");

#Fetch and and print result

results = cursor.fetchall()

for row in results:
    print(row)
