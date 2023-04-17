import sqlite3
import csv
from datetime import datetime

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


class Admin:
    def __init__(self, user_id, first, last, phone, email, password, is_manager):
        self.user_id = user_id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.password = password
        self.is_manager = is_manager

    def add_user(self):
        create_query = '''INSERT INTO Users (first, last, email, phone, password, is_manager)
        VALUES(?,?,?,?,?,?) '''
        first = input('Enter first name ')
        last = input('Enter last name ')
        email = input('Enter email ')
        phone = input('Enter phone ')
        password = input('Enter password ')
        is_manager = input('Is this user a manager? (True or False) ')
        cursor.execute(create_query,(first,last,email,phone,password,is_manager,)).fetchall()
        connection.commit()

    def add_competency(self):
        pass

    def add_assessment(self):
        pass

    def edit_user(self):
        pass

    def edit_competency(self):
        pass

    def edit_assessment(self):
        pass

    def edit_assessment_result(self):
        pass