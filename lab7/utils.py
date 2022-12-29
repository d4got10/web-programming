import sqlite3
def get_db_connection():
    return sqlite3.connect('C:\\Users\\rusbe\\Desktop\\University-Projects\\web-programming\\lab7\\library.sqlite')