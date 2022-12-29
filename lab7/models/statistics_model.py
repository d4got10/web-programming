import pandas
import sqlite3
import pandas as pd


def books_from_most_popular_genre(conn, dateStart, dateEnd):
    return pd.read_sql(f'''
        SELECT title AS 'Название', genre_name AS 'Жанр' FROM book
        JOIN 
        (SELECT genre_id FROM book_reader
        JOIN book USING(book_id)
        WHERE borrow_date>='{dateStart}' and borrow_date<='{dateEnd}'
        GROUP BY genre_id
        ORDER BY COUNT(*) DESC LIMIT 1) 
        USING (genre_id)
        JOIN genre USING (genre_id);
    ''', conn)