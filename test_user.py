import sqlite3
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()
def create_person():
    create_query = '''INSERT INTO Users (first, last, email, phone, password, is_manager)
    VALUES(?,?,?,?,?,?) '''
    first = input('Enter first name ')
    last = input('Enter last name ')
    email = input('Enter email ')
    phone = input('Enter phone ')
    password = input('Enter password ')
    is_manager = input('is manager ')
    cursor.execute(create_query,(first,last,email,phone,password,is_manager,)).fetchall()
    connection.commit()

create_person()