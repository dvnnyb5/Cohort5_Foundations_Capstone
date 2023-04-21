import sqlite3
import bcrypt
import hashlib
import csv
from datetime import datetime
connection = sqlite3.connect("capstone.db")
cursor = connection.cursor()

class User:
    def __init__(self,user_id,first, last, phone, email, password):
        self.user_id = user_id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.password = password
        self.is_manager = 0

    def view_data(self):
        view_query = '''SELECT * FROM Assessments WHERE user_id = ?'''
        data = cursor.execute(view_query,(self.user_id,)).fetchall()
        for line in data:
            print(line)

    def change_name(self):
        name_change = '''UPDATE Users SET first = ?, last = ? WHERE user_id = ?'''
        first = input('Enter new first name ')
        last = input('Enter new last name ')
        cursor.execute(name_change,(first,last,self.user_id))
        connection.commit()

    def change_password(self):
        pass_change = '''UPDATE Users SET password = ? WHERE user_id = ?'''
        new_pass = input('Enter new password ')
        password = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt())
        cursor.execute(pass_change,(password,self.user_id))
        connection.commit()



class Manager(User):
    def __init__(self,user_id,first,last,phone,email,password):
        super().__init__(user_id,first,last,phone,email,password)
        self.is_manager = 1
    
    def view_users(self):
        view_query = '''SELECT * FROM Users'''
        results = cursor.execute(view_query,).fetchall()
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Phone':<20}{'Email':<20}{'is_manager':<20}{'is_active'}")
        print(f"{'---------':<20}{'----------':<20}{'---------':<20}{'-----':<20}{'-----':<20}{'----------':<20}{'---------'}")
        for row in results:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}{row[6]:<20}{row[7]}")

    def search_user(self):
        search_query = '''SELECT * FROM Users WHERE first LIKE ?'''
        search = input('Search by first name: ')
        search = f'%{search}%'
        rows = cursor.execute(search_query,(search,)).fetchall()
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Phone':<20}{'Email':<20}{'is_manager':<20}{'is_active'}")
        print(f"{'---------':<20}{'----------':<20}{'---------':<20}{'-----':<20}{'-----':<20}{'----------':<20}{'---------'}")
        for row in rows:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}{row[6]:<20}{row[7]}")

    def view_competencies(self):
        view_query = '''SELECT * FROM Competencies'''
        data = cursor.execute(view_query,).fetchall()
        print(f"\n{'Competency ID':<20}{'Competency Name':<20}{'Date Created':<20}")
        print(f"{'--------------':<20}{'----------------':<20}{'-------------':<20}")
        for line in data:
            print(f"{line[0]:<20}{line[1]:<20}{line[2]:<20}")

    def report_of_users(self):
        all_users_query = '''
            SELECT U.user_id, U.first, U.last, C.competency_name, COALESCE(A.result, NULL) AS result
            FROM Users U
            LEFT OUTER JOIN (
                SELECT user_id, result, competency_id
                FROM Assessments
                WHERE competency_id = ?
            ) A ON U.user_id = A.user_id
            LEFT OUTER JOIN Competencies C ON C.competency_id = A.competency_id
            WHERE U.user_id NOT IN (SELECT user_id FROM Assessments)
            OR A.user_id IS NOT NULL
        '''
        print("\n\n")
        self.view_competencies()
        print("\n\n")
        search = input('Competency id: ')
        results = cursor.execute(all_users_query,(search,)).fetchall()
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Subject':<20}{'Score'}")
        print(f"{'-------':<20}{'----------':<20}{'---------':<20}{'-------':<20}{'-----'}")
        for row in results:
            if row[3] == None:
                print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{'NONE':<20}{'NONE':<20}")
            else:
                print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}")
    
    def report_of_single_user(self):
        query = '''SELECT U.user_id, U.first, U.last, C.competency_name, A.result FROM Users U JOIN Assessments A ON A.user_id=U.user_id JOIN Competencies C ON C.competency_id=A.competency_id WHERE U.user_id = ?'''
        user_id = input('Enter user id ')
        results = cursor.execute(query,(user_id,))
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Subject':<20}{'Score'}")
        print(f"{'-------':<20}{'----------':<20}{'---------':<20}{'-------':<20}{'-----'}")
        for row in results:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}")

    def add_user(self):
        create_query = '''INSERT INTO Users (first, last, email, phone, password, is_manager)
        VALUES(?,?,?,?,?,?) '''
        first = input('Enter first name ')
        last = input('Enter last name ')
        email = input('Enter email ')
        phone = input('Enter phone ')
        password = input('Enter password ')
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        is_manager = input('Is this user a manager? (1=Manager, 0=User) ')
        cursor.execute(create_query,(first,last,email,phone,hashed_password,is_manager,)).fetchall()
        connection.commit()
    
    def add_new_competency(self):
        query = '''INSERT INTO Competencies (competency_name, date_created)
        VALUES(?,?)'''
        name = input('Enter new competency name ')
        date_created = datetime.now()
        cursor.execute(query,(name,date_created))
        connection.commit()
        print(f'{name} has been added!')

    def add_new_assessment(self):
        query = '''INSERT INTO Assessments (user_id, competency_id)
        VALUES(?,?)'''
        user_id = input('Enter user_id ')
        competency_id = input('Enter competency_id ')
        cursor.execute(query,(user_id, competency_id))
        connection.commit()

    def add_assessment_result(self):
        query = '''UPDATE Assessments SET result = ? WHERE assessment_id = ?'''
        assessment_id = input('Enter assessment_id ')
        result = input('Enter result ')
        cursor.execute(query,(result, assessment_id))
        connection.commit()
        print('Result recorded!')

    def edit_user_info(self):
        query = '''
        UPDATE Users 
        SET first = ?, last = ?, phone = ?, email = ?, password = ?, is_manager = ?, active = ?
        WHERE user_id = ?'''
        user_id = input("Enter user ID of the user you'd like to edit ")
        first = input('Enter new first name ')
        last = input('Enter new last name ')
        phone = input('Enter new phone number ')
        email = input('Enter new email ')
        password = input('Enter new password ')
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        is_manager = int(input('Enter 1 if manager or 0 if user '))
        active = int(input('Enter 1 if active or 0 if not active '))
        cursor.execute(query,(first,last,phone,email,hashed_password,is_manager,active,user_id))
        connection.commit()
        print('\n\n')
        print(f'{first} {last} has been updated!')

    def edit_competency(self):
        query = '''
        UPDATE Competencies
        SET competency_name = ?
        WHERE competency_name LIKE ?
        '''
        update_competency = input("Enter competency you'd like to update ")
        new_comp_name = input('What would you like to call the competency?(name) ')
        search = f'%{update_competency}%'
        cursor.execute(query,(new_comp_name,search))
        connection.commit()
        print('\n\n')
        print(f'{new_comp_name} has been updated!')

    def edit_assessment(self):
        query = '''
        UPDATE Assessments
        SET user_id = ?,
        competency_id = ?,
        result = ?
        WHERE assessment_id = ?
        '''
        assessment_id = int(input("Enter an assessment ID to update an assessment "))
        new_user_id = int(input("Enter new user ID "))
        new_comp_id = int(input("Enter new competency ID "))
        new_result = int(input("Enter new result "))
        cursor.execute(query,(new_user_id,new_comp_id,new_result,assessment_id))
        connection.commit()
        print('\n\n')
        print(f'assessment_id {assessment_id} has been updated!')
    
    def delete_assessment_result(self):
        query = '''
        UPDATE Assessments
        SET result = NULL
        WHERE assessment_id = ?
        '''
        assessment_id = int(input("Enter assessment ID to remove result "))
        cursor.execute(query,(assessment_id,))
        connection.commit()

    def import_csv(self):
        with open('test.csv', 'r')as file:
            next(file)
            reader = csv.reader(file)
            data = [row for row in reader]

        query = '''INSERT INTO Assessments (user_id, competency_id, result)
        VALUES (?,?,?)'''
        for row in data:
            cursor.execute(query, row)
        connection.commit()
        print('Results have been imported! ')
        
    
    def write_one_report(self):
        user_id = input('Enter a user ID ')
        query = '''
        SELECT u.first, u.last, c.competency_name, a.result
        FROM Users u
        LEFT JOIN Assessments a ON u.user_id = a.user_id
        LEFT JOIN Competencies c ON a.competency_id = c.competency_id
        WHERE u.user_id = ?;
        '''
        data = cursor.execute(query,(user_id))
        with open('single_new.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['first', 'last', 'subject', 'score'])
            writer.writerows(data)
        print('Data has been exported!')

    def write_report_csv(self):
        query = '''
        SELECT u.first, u.last, c.competency_name, a.result
        FROM Users u
        LEFT JOIN Assessments a ON u.user_id = a.user_id
        LEFT JOIN Competencies c ON a.competency_id = c.competency_id;
        '''
        data = cursor.execute(query)
        with open('new.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['first', 'last', 'subject', 'score'])
            writer.writerows(data)
        print('Data has been exported!')

