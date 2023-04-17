import sqlite3
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
        cursor.execute(pass_change,(new_pass,self.user_id))
        connection.commit()



class Manager(User):
    def __init__(self,user_id,first,last,phone,email,password):
        super().__init__(user_id,first,last,phone,email,password)
        self.is_manager = 1
    
    def view_users(self):
        view_query = '''SELECT * FROM Users'''
        results = cursor.execute(view_query,).fetchall()
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Phone':<20}{'Email':<20}{'Password':<20}{'is_manager':<20}{'is_active'}")
        print(f"{'---------':<20}{'----------':<20}{'---------':<20}{'-----':<20}{'-----':<20}{'--------':<20}{'----------':<20}{'---------'}")
        for row in results:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}{row[5]:<20}{row[6]:<20}{row[7]}")

    def search_user(self):
        search_query = '''SELECT * FROM Users WHERE first LIKE ?'''
        search = input('Search by first name: ')
        search = f'%{search}%'
        rows = cursor.execute(search_query,(search,)).fetchall()
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}{'Phone':<20}{'Email':<20}{'Password':<20}{'is_manager':<20}{'is_active'}")
        print(f"{'---------':<20}{'----------':<20}{'---------':<20}{'-----':<20}{'-----':<20}{'--------':<20}{'----------':<20}{'---------'}")
        for row in rows:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}{row[5]:<20}{row[6]:<20}{row[7]}")

    def report_of_users(self):
        all_users_query = '''SELECT FROM Competencies'''
        results = cursor.execute(all_users_query,).fetchall()
        print(f"\n{'User ID':<20}{'First Name':<20}{'Last Name':<20}")
        print(f"{'---------':<20}{'----------':<20}{'---------':<20}")
        for row in results:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}")

    def report_of_user(self):
        query = '''SELECT'''

    def view_list_of_assessments_for_a_given_user(self):
        pass

    def add_user(self):
        create_query = '''INSERT INTO Users (first, last, email, phone, password, is_manager)
        VALUES(?,?,?,?,?,?) '''
        first = input('Enter first name ')
        last = input('Enter last name ')
        email = input('Enter email ')
        phone = input('Enter phone ')
        password = input('Enter password ')
        is_manager = input('Is this user a manager? (1=Manager, 0=User) ')
        cursor.execute(create_query,(first,last,email,phone,password,is_manager,)).fetchall()
        connection.commit()
    
    def add_new_competency(self):
        pass

    def add_new_assessment(self):
        pass

    def add_assessment_result(self):
        pass

    def get_all_assessments(self):
        view_query = '''SELECT * FROM Assessments'''
        data = cursor.execute(view_query).fetchall()
        for line in data:
            print(line)


# user1 = Manager(1, 'sdfkljasd', 'a;sldkfjasld', 's;adlfsd', 'sdkflaskd', 'sd;lfasdke')
# user1.change_password()



