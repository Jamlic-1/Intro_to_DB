#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your MySQL password
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as err:
        # mysql.connector specific errors (connection/authentication/SQL errors)
        print(f"MySQL Error: {err}")
    except Exception as exc:
        # Any other unexpected errors
        print(f"Error: {exc}")
    finally:
        # Close cursor if it was created
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                print(f" Error: {Exception}")
        # Close connection if it was created and is connected
        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except Exception:
                print(f" Error: {Exception}")

if __name__ == "__main__":
    create_database()
