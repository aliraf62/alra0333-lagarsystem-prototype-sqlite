
"""
This is the main entry point for the Lagra™ Prototype CLI.
It calls modules for database initialization, user registration, user login, data storage, and data retrieval.
"""

import getpass
import sqlite3
from db_init import init_db
from user_register import register_user
from user_login import login_user
from data_store import store_data
from data_retrieve import retrieve_data

# Main menu function
def main_menu():
    print("\nWelcome to Lagra™ Prototype")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

# User menu function
def user_menu(username):
    print(f"\nWelcome, {username}")
    print("1. Store Data")
    print("2. Retrieve Data")
    print("3. Logout")
    choice = input("Enter your choice: ")
    return choice

# Main CLI interface function
def cli_interface():
    logged_in = False
    username = None
    
    # Initialize database
    conn, result = init_db()
    c = conn.cursor()
    if conn:
        print("Database initialized.")
    else:
        print(result)
        return
    
    while True:
        if not logged_in:
            choice = main_menu()
            if choice == '1':  # Register user
                username = input("Enter username: ")
                password = getpass.getpass("Enter password: ")
                success, message = register_user(conn, c, username, password)
                print(message)
            elif choice == '2': # Login
                username = input("Enter username: ")
                password = getpass.getpass("Enter password: ")
                logged_in, message = login_user(c, username, password)
                print(message)
            elif choice == '3': # Exit
                print("Thank you for using Lagra™ Prototype. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            choice = user_menu(username)
            if choice == '1': # Store data
                data = input("Enter the data you want to store: ")
                success, message = store_data(conn, c, username, data)
                print(message)
            elif choice == '2': # Retrieve data
                success, data = retrieve_data(c, username)
                if success:
                    print("Your stored data:")
                    for item in data:
                        print(f"- {item[0]}")
                else:
                    print(data)
            elif choice == '3': # log out
                print("Logged out successfully.")
                logged_in = False
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli_interface()
