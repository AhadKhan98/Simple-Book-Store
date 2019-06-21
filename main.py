"""
Simple Book Store: A program that stores book information in a database and allows data retrieval, modification and addition.
The books are stored in the format: Title, Author, Year, ISBN and are stored in a SQLite database.

Features:
View all records
Search an entry
Add an entry
Update an entry
Delete an entry

@author: Ahad Zai

"""

import frontend
import backend

def main():
    backend.connect()
    frontend.create_ui()

if __name__=="__main__":
    main()
