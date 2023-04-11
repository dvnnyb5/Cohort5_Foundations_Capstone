import sqlite3
import csv
from datetime import datetime
from admin import Admin
from user import User
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()
with open('queries.sql') as my_queries:
    queries = my_queries.read()
cursor.executescript(queries)

def menu():
    input("""
    ******MENU******
        """)