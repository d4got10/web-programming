import pandas as pd

def get_publisher(conn):
    return pd.read_sql("SELECT * FROM publisher", conn)


def get_author(conn):
    return pd.read_sql("SELECT * FROM author", conn)


def get_genre(conn):
    return pd.read_sql("SELECT * FROM genre", conn)

def cardQuerry(conn, publishers, genres, authors):
    if len(publishers) == 1:
        publishers = f'({publishers[0]})'
    if len(genres) == 1:
        genres = f'({genres[0]})'
    if len(authors) == 1:
        authors = f'({authors[0]})'
    return pd.read_sql(f'''
    SELECT 
    id,
    Название,
    GROUP_CONCAT(DISTINCT Авторы) as 'Авторы',
    Жанр,
    Издательство,
    Год_издания,
    Количество
    FROM
    (
        SELECT
        	title AS 'Название',
        	genre_name AS 'Жанр',
        	publisher_name AS 'Издательство',
            year_publication AS 'Год_издания',
            available_numbers AS 'Количество',
            book_id as id
        FROM book
        JOIN genre USING(genre_id)
        JOIN publisher USING(publisher_id)
        JOIN book_author USING(book_id)
        WHERE (genre_id IN {genres} OR {len(genres)==0})
            AND (publisher_id IN {publishers} OR {len(publishers)==0})
            AND (author_id IN {authors} OR {len(authors)==0}) 
    ) as q1
    INNER JOIN 
    (
        SELECT book_id, author_name as 'Авторы'
        FROM book_author
        JOIN author USING (author_id)
    ) AS q2 
    ON id = book_id
    GROUP BY id
    ''', conn)

def borrow_book(conn, book_id, user_id):
    cur = conn.cursor()
    cur.executescript(
    f'''
        UPDATE book
        SET available_numbers = available_numbers - 1
        WHERE book_id = {book_id} and available_numbers>0;
    
        INSERT INTO book_reader (book_id, reader_id, borrow_date, return_date)
        VALUES ({book_id}, {user_id}, DATE(), null);
    ''')
    conn.commit()