import pandas as pd


def get_table_names(conn):
    return pd.read_sql('''SELECT 
    name
FROM 
    sqlite_schema
WHERE 
    type ='table' AND 
    name NOT LIKE 'sqlite_%';''', conn)


def get_table(name, conn):
    return pd.read_sql(f"SELECT * FROM {name}", conn)


def get_publisher(conn):
    return pd.read_sql("SELECT * FROM publisher", conn)


def get_genre(conn):
    return pd.read_sql("SELECT * FROM genre", conn)