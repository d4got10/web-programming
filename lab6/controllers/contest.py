import constants
from app import app
from flask import render_template, request


@app.route('/contest/<contest>')
def contest(contest):
    html = render_template(
        'contest.html',
        contest=contest,
        discription=constants.contest_dict[contest]
    )
    return html
