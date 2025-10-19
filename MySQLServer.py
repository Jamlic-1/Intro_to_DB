#!/usr/bin/env python3
"""
Python script to create the alx_book_store database in MySQL
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    """
    Create the alx_book_store database in MySQL
    """
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this to your MySQL username
            password=''   # Change this to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_database()
