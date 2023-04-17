import sqlite3
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()
with open('queries.sql') as my_queries:
    queries = my_queries.read()
cursor.executescript(queries)