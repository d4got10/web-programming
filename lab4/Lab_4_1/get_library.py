from jinja2 import FileSystemLoader, Environment
import sqlite3
from library_model import *

conn = sqlite3.connect("library.sqlite")

df = get_table_names(conn)
table_names = df['name']
tables = [get_table(name, conn) for name in table_names]
conn.close()

f_template = open("templates/library_templ.html", 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()
template = Environment(loader=FileSystemLoader('templates/')).from_string(html)

result_html = template.render(
    table_names=table_names,
    tables=tables,
    len=len
)
f = open('library.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
