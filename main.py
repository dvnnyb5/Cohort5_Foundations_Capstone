import os
import sqlite3
import bcrypt
import csv
from user import User, Manager
connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def user_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    return input("""
    ******MAIN MENU******

    [1] VIEW ASSESSMENT DATA
    [2] EDIT NAME
    [3] EDIT PASSWORD
    [4] LOG OUT
        """)
def admin_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    return input("""
    ******MAIN MENU******

    [1] VIEW ALL USERS
    [2] SEARCH FOR USER
    [3] VIEW USER REPORTS/COMPETENCY LEVELS
    [4] VIEW INDIVIDUAL COMPETENCY LEVEL
    [5] VIEW LIST OF ASSESSMENTS FOR SINGLE USER
    [6] ADD
    [7] EDIT
    [8] DELETE ASSESSMENT RESULT
    [9] EXPORT COMPETENCY REPORT
    [10] EXPORT COMPETENCY REPORT FOR SINGLE USER
    [11] IMPORT ASSESSMENT RESULT
    [12] LOG OUT
        """)
def add_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    return input("""
    ******ADD MENU******

    [1] ADD NEW USER
    [2] ADD NEW COMPETENCY
    [3] ADD ADD NEW ASSESSMENT TO COMPETENCY
    [4] ADD AN ASSESSMENT RESULT FOR A USER FOR AN ASSESSMENT
    [5] BACK TO MAIN MENU
        """)
def edit_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    return input("""
    ******EDIT MENU******

    [1] EDIT A USERS INFORMATION
    [2] EDIT A COMPETENCY
    [3] EDIT AN ASSESSMENT
    [4] BACK TO ORIGINAL MENU
        """)


    
user = None

# login
while not user:
    email = input("Email: ")
    password = input("Password: ")
    query = '''SELECT * FROM Users WHERE email = ?'''
    potential_user = cursor.execute(query,(email,)).fetchall()[0]
    if bcrypt.checkpw(password.encode(), potential_user[5]):
        user = potential_user
        print("\n\nlogin successful")
    else:
        print("\nTry Again\nIncorrect Username or Password!\n\n")

instantiated_user = None
if user[6] == 1:
    instantiated_user = Manager(user[0], user[1], user[2], user[3], user[4], user[5])
    pass
else:
    instantiated_user = User(user[0], user[1], user[2], user[3], user[4], user[5])
    pass

# Admin engine
while instantiated_user.is_manager == 1:
    try:
        selection = admin_menu()
        if selection == '1':
            instantiated_user.view_users()
        elif selection == '2':
            instantiated_user.search_user()
        elif selection == '3':
            instantiated_user.report_of_users()
        elif selection == '4':
            instantiated_user.report_of_single_user()
        elif selection == '5':
            instantiated_user.report_of_single_user()
        elif selection == '6':
            while True:
                selection2 = add_menu()
                if selection2 == '1':
                    instantiated_user.add_user()
                elif selection2 == '2':
                    instantiated_user.add_new_competency()
                elif selection2 == '3':
                    instantiated_user.add_new_assessment()
                elif selection2 == '4':
                    instantiated_user.add_assessment_result()
                elif selection2 == '5':
                    break
                else:
                    print("/nTry a valid selection!")
        elif selection == '7':
            while True:
                selection3 = edit_menu()
                if selection3 == '1':
                    instantiated_user.edit_user_info()
                elif selection3 == '2':
                    instantiated_user.edit_competency()
                elif selection3 == '3':
                    instantiated_user.edit_assessment()
                elif selection3 == '4':
                    break
                else:
                    print("\nTry a valid selection!")
        elif selection == '8':
            instantiated_user.delete_assessment_result()
        elif selection == '9':
            instantiated_user.write_report_csv()
        elif selection == '10':
            instantiated_user.write_one_report()
        elif selection == '11':
            instantiated_user.import_csv()
        elif selection == '12':
            break
        else:
            print('Try a valid selection')
    except Exception:
        with open('log.txt', 'a') as log:
            log.write(f"{Exception}\n")
        print('\nSystem Error try again!\n')

# user engine
while instantiated_user.is_manager != 1:
    try:
        selection = user_menu()
        if selection == '1':
            instantiated_user.view_data()
        elif selection == '2':
            instantiated_user.change_name()
        elif selection == '3':
            instantiated_user.change_password()
        else:
            break
    except Exception:
        with open('log.txt', 'a') as log:
            log.write(f"{Exception}\n")
        print('\nSystem Error try again!\n')