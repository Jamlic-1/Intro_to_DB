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
            password="your_password"  # replace with actual password or use env vars
        )

        # If connection wasn't established, mysql.connector.connect will raise Error
        cursor = connection.cursor()
        # Create database if it does not exist (so script won't fail if it already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # mysql.connector specific errors (connection/authentication/SQL errors)
        print(f"Error: {err}")

    except Exception as e:
        # Any other unexpected errors
        print(f"Error: {e}")

    finally:
        # Safely close cursor if it was created
        try:
            if cursor is not None:
                cursor.close()
        except Exception:
            pass

        # Safely close connection if it was created and is connected
        try:
            if connection is not None and connection.is_connected():
                connection.close()
        except Exception:
            pass

if __name__ == "__main__":
    create_database()
