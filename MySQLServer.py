#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Attempt to connect to MySQL server (update credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        # If connection failed, mysql.connector.connect would raise an exception
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        # Confirm creation (or existence) to the user
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # mysql.connector-specific errors (connection/authentication/SQL errors)
        print(f"Error: {err}")

    except Exception as exc:
        # Any other unexpected errors
        print(f"Error: {exc}")

    finally:
        # Safely close cursor and connection if they were opened
        try:
            if cursor is not None:
                cursor.close()
        except Exception:
            pass

        try:
            if connection is not None and connection.is_connected():
                connection.close()
        except Exception:
            pass

if __name__ == "__main__":
    create_database()
