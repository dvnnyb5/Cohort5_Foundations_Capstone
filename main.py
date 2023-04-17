
import sqlite3
from user import User, Manager
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def user_menu():
    return input("""
    ******MENU******
    [1] VIEW ASSESSMENT DATA
    [2] EDIT NAME
    [3] EDIT PASSWORD
    [4] LOG OUT
        """)
def admin_menu():
    return input("""
    ******MENU******
    [1] VIEW ALL USERS
    [2] SEARCH FOR USER
    [3] VIEW USER REPORTS/COMPETENCY LEVELS
    [4] VIEW INDIVIDUAL COMPETENCY LEVEL
    [5] VIEW LIST OF ASSESSMENTS
    [6] ADD
    [7] EDIT
    [8] DELETE
    [9] LOG OUT
        """)
    
user = None

# login
while not user:
    email = input("Email: ")
    password = input("Password: ")
    query = '''SELECT * FROM Users WHERE email = ?'''
    potential_user = cursor.execute(query,(email,)).fetchall()[0]
    if password == potential_user[5]:
        user = potential_user
        print("\n\nlogin successful\n\n")
    else:
        print("\nTry Again\nincorrect password\n\n")

instantiated_user = None
if user[6] == 1:
    instantiated_user = Manager(user[0], user[1], user[2], user[3], user[4], user[5])
    pass
else:
    instantiated_user = User(user[0], user[1], user[2], user[3], user[4], user[5])
    pass

# Admin engine
while instantiated_user.is_manager == 1:
    selection = admin_menu()
    if selection == '1':
        instantiated_user.view_users()
    elif selection == '2':
        instantiated_user.search_user()
    elif selection == '5':
        instantiated_user.get_all_assessments()
    else:
        break

# user engine
while instantiated_user.is_manager != 1:
    selection = user_menu()
    if selection == '1':
        instantiated_user.view_data()
    elif selection == '2':
        instantiated_user.change_name()
    elif selection == '3':
        instantiated_user.change_password()
    else:
        break


new_user = Manager(user[0], user[1], user[2], user[3], user[4])