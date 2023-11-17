#!/usr/bin/python3

"""
Module: database_operations
Description:This module provide functions for interacting with a MySQL database
"""

import MySQLdb
import sys


def fetchdata():
    """
    Function: fetchdata
    Description: Fetches and prints all data from the 'states' table in
                 the specified MySQL database.
    Usage:
    - Requires three command-line arguments: MySQL username, password,
      and database name.
    - The function connects to the MySQL server on localhost at port 3306.
    - It executes a SELECT query to retrieve all data from the 'states' table.
    - The fetched results are printed to the console.

    Example:
    ```bash
    python script.py your_username your_password hbtn_0e_0_usa
    ```

    Args:
    - No arguments are passed directly to the function;
      it retrieves arguments from sys.argv.

    Returns:
    - None

    Raises:
    - None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    statename = sys.argv[4]

    # Create a cursor
    cursor = db.cursor()

    # Create a query that selects states
    # that start only with capital letter name
    cursor.execute("""SELECT * FROM states WHERE name
                   LIKE BINARY '{}' ORDER BY states.id""".format(statename))

    # Fetch and print result
    results = cursor.fetchall()
    for row in results:
        print(row)

    # closing the cursor
    cursor.close()
    # Close the database connection
    db.close()


if __name__ == "__main__":
    # Execute the fetchdata function when the script is run
    fetchdata()
