import constants
from app import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    name = ""
    gender = ""
    program_id = 0
    subject_id = []
    subjects_select = []
    contest_id = []
    contest_select = []
    name = request.values.get('username')
    gender = request.values.get('gender')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    contest_id = request.values.getlist('contest[]')

    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    contests_select = [constants.contests[int(i)] for i in contest_id]
    html = render_template(
        'hello.html',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        program_list=constants.programs,
        len=len,
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        contests_select=contests_select,
        contest_list=constants.contests
    )
    return html
