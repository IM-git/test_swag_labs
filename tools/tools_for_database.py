import sqlite3
from sqlite3 import Error
import os

LOGIN_PASSWORD = [('standard_user', 'secret_sauce'),
                  ('locked_out_user', 'secret_sauce'),
                  ('problem_user', 'secret_sauce'),
                  ('performance_glitch_user', 'secret_sauce')]


class ToolsDatabase:

    @staticmethod
    def create_db():
        """Will create database - login_password.db"""
        connection = sqlite3.connect('login_password.db')
        db_session = connection.cursor()
        db_session.execute('''CREATE TABLE users(
                            _id INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT,
                            password TEXT)''')

        db_session.connection.commit()

    @staticmethod
    def insert_into_db():
        """Here is existing one important moment: was created 3 row
        but created for inserting in (LOGIN_PASSWORD) two values.
         For creating a third value need enter a 'NULL',
         see the example below."""
        connection = sqlite3.connect('login_password.db')
        db_session = connection.cursor()
        db_session.executemany('INSERT INTO users VALUES (NULL, ?, ?)', LOGIN_PASSWORD)

        db_session.connection.commit()

    @staticmethod
    def read_db():
        """Getting all values from the 'users' table."""
        connection = sqlite3.connect('login_password.db')
        db_session = connection.cursor()
        values = db_session.execute('SELECT * FROM users')
        #   Prints all values to the console
        print(values.fetchall())

        db_session.connection.commit()

    @staticmethod
    def delete_table():
        """Delete table in login_password.db database,
        but the database will remain(empty)."""
        connection = sqlite3.connect('login_password.db')
        db_session = connection.cursor()
        db_session.execute('DROP TABLE if exists users')

        db_session.connection.commit()

    @staticmethod
    def delete_db():
        """Delete login_password.db database."""
        os.remove('login_password.db')


