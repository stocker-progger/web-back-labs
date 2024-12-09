from flask import Blueprint, render_template, session, request

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def lab7():
    return render_template('lab7/index.html', login=session.get('login'))
