from flask import Blueprint, render_template
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def laba3():
    return render_template('lab3.html')