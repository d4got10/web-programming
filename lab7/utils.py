import sqlite3


def get_db_connection():
    return sqlite3.connect('C:\\Users\\rusbe\\Desktop\\University\\123456\\web-programming\\lab7\\library.sqlite')


def convert_date(date):
    dates=date.split('.')
    if(len(dates)>3):
        return dates[2]+'-'+dates[1]+'-'+dates[0]
    else:
        return date