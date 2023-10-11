# Lagra™ Prototype

## Description

Lagra™ Prototype is a simple CLI-based Python application that allows users to securely register, log in, store, and retrieve data. The system uses SQLite for data storage and is designed with modularity in mind, making it easy to expand and maintain.

## Features

- User Registration
- User Login
- Data Storage
- Data Retrieval

## Installation

1. Clone the repository or download the ZIP file and extract it.
2. Navigate to the project folder in your terminal.
3. Run the application using Python 3.x:

    ```bash
    python main.py
    ```

## Usage

Run `main.py` to start the application. You will be presented with a main menu:

1. Register: To create a new user account.
2. Login: To log in using an existing account.
3. Exit: To exit the application.

After logging in, you will be presented with a user menu to store or retrieve data.

## Dependencies

- Python 3.x
- SQLite

## Project Structure

The project is divided into multiple Python files, each responsible for a specific functionality:

- `db_init.py`: Initializes the database and tables.
- `user_register.py`: Handles user registration.
- `user_login.py`: Manages user login.
- `data_store.py`: Manages data storage.
- `data_retrieve.py`: Handles data retrieval.
- `main.py`: The main entry point of the application.

## Call Graph

Please refer to `call_graph.dot` for the call graph of the system.

## License

This project is under the MIT License. See the LICENSE.md file for details.
