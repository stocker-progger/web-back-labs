from flask import Blueprint, render_template

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def laba9():
    return render_template('lab9/lab9.html')
