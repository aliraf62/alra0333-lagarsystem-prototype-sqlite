
"""
This is the main entry point for the Lagra™ Prototype CLI.
It calls modules for database initialization, user registration, user login, data storage, and data retrieval.
"""
import sys
import getpass
import sqlite3
from db_init import init_db
from user_register import register_user
from user_login import login_user
from data_store import store_data
from data_retrieve import retrieve_data
from messages import messages as m
import time

# Main menu function
def main_menu():
    print("\n"  +  m["10"][lang])
    print("1. " +  m["11"][lang])
    print("2. " +  m["12"][lang])
    print("3. " +  m["13"][lang])
    choice = input(m["choose"][lang])
    return choice

# User menu function
def user_menu(username):
    print("\n" +  m["20"][lang] + f"{username}")
    print("1. "+  m["21"][lang])
    print("2. "+  m["22"][lang])
    print("3. "+  m["23"][lang])
    choice = input(m["choose"][lang])
    return choice

# Main CLI interface function
def cli_interface():
    logged_in = False
    username = None
    #print(lang)
    # Initialize database
    conn, result = init_db(lang)
    c = conn.cursor()
    if conn:
        print(m["db_start"][lang])
    else:
        print(result)
        return
    
    while True:
        if not logged_in:
            choice = main_menu()
            if choice == '1':  # Register user
                username = input(m["user"][lang])
                password = getpass.getpass(m["pwd"][lang])
                #try:
                success, message = register_user(conn, c, username, password,lang)
                print(message)
                #except TypeError:
                #    print('User already exists.')

            elif choice == '2': # Login
                username = input(m["user"][lang])
                password = getpass.getpass(m["pwd"][lang])
                logged_in, message = login_user(c, username, password,lang)
                print(message)
            elif choice == '3': # Exit
                print(m["exit"][lang])
                break
            else:
                print(m["invalid"][lang])
        else:
            choice = user_menu(username)
            if choice == '1': # Store data
                data = input(m["item"][lang])
                success, message = store_data(conn, c, username, data,lang)
                print(message)
            elif choice == '2': # Retrieve data
                success, data = retrieve_data(c, username,lang)
                if success:
                    print(m["retrieve"][lang])
                    for item in data:
                        print(f"- {item[0]}")
                else:
                    print(data)
            elif choice == '3': # log out
                print(m["logout"][lang])
                logged_in = False
            else:
                print(m["invalid"][lang])

def main(args):
#    cli_interface()
    global lang 
    lang= 0 if "en" in args else 1
    cli_interface()
if __name__ == "__main__":
    main(sys.argv[1:])
#    cli_interface()
