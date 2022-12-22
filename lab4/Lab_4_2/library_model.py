import pandas as pd


def get_authors(conn):
    return pd.read_sql("SELECT * FROM author;", conn)


def get_publishers(conn):
    return pd.read_sql("SELECT * FROM publisher;", conn)


def get_genres(conn):
    return pd.read_sql("SELECT * FROM genre;", conn)


def get_book_with_arguments(conn, genres, authors, publishers):
    return pd.read_sql(f'''SELECT * FROM book_author
                            JOIN book USING (book_id)
                            JOIN genre USING (genre_id)
                            JOIN publisher USING (publisher_id)
                            JOIN author USING (author_id)
                            WHERE author_id IN {authors} 
                            AND genre_id IN {genres}
                            AND publisher_id IN {publishers};''', conn)