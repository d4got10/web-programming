from jinja2 import FileSystemLoader, Environment
import sqlite3
from library_model import *

selected_authors = [1, 2, 3, 4]
selected_genres = [1, 2]
selected_publishers = [1, 2, 3, 4, 5, 6]

conn = sqlite3.connect("library.sqlite")

df_authors = get_authors(conn)['author_name']
df_genres = get_genres(conn)['genre_name']
df_publishers = get_publishers(conn)['publisher_name']
df = get_book_with_arguments(conn, tuple(selected_genres), tuple(selected_authors), tuple(selected_publishers))

conn.close()

f_template = open("templates/reader_book_templ.html", 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()
template = Environment(loader=FileSystemLoader('templates/')).from_string(html)

result_html = template.render(
    authors=df_authors,
    genres=df_genres,
    publishers=df_publishers,
    selected_authors=selected_authors,
    selected_genres=selected_genres,
    selected_publishers=selected_publishers,
    books=df,
    len=len
)
f = open('reader_book.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
