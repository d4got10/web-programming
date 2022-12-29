import pandas

from app import app
from flask import render_template, request, session
from utils import get_db_connection, convert_date
from models.book import return_book
from models.statistics_model import books_from_most_popular_genre

@app.route('/statistics', methods=['get'])
def statistics():
    conn = get_db_connection()
    borrowers_list = pandas.DataFrame
    books_list = pandas.DataFrame
    most_popular_book_df = pandas.DataFrame

    if request.values.get('submitGetPopularBook'):
        startDate=request.values.get('dateStart')
        endDate=request.values.get('dateEnd')
        startDate=convert_date(startDate)
        endDate=convert_date(endDate)
        books_list=books_from_most_popular_genre(conn, startDate, endDate)
        print(books_list)

    return render_template('statistics.html',
       most_popular_book_df=books_list,
       borrowers_list=borrowers_list,
       len=len)