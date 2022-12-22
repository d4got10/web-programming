import constants
from app import app
from flask import render_template


@app.route('/', methods=['GET'])
def index():
    html = render_template(
        'index.html',
        program_list=constants.programs,
        subject_list=constants.subjects,
        contest_list=constants.contests,
        len=len
    )
    return html
