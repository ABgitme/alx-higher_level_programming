#!/usr/bin/python3
"""
1-filter_states.py

This script lists all cities with ascending id from the database hbtn_0e_4_usa.

Usage:
    ./1-filter_states.py username password database

Arguments:
    username: MySQL username for database authentication.
    password: MySQL password for database authentication.
    database: Name of the MySQL database to connect to.

This script connects to a MySQL server running on localhost at port 3306,
executes a SQL query on state name searched and matched,
sorts the results by state ID in ascending order,
and then prints the fetched rows.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments provided
    # if len(sys.argv) != 4:
    #    sys.exit(1)

    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Execute SQL query to match state name ans sort by id ascending
    query = "SELECT cities.id, cities.name, states.name\
    FROM cities JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetch all the rows and print them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
