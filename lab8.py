from flask import Blueprint, render_template, jsonify, session, request

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def laba8():
    return render_template('lab8/lab8.html', login=session.get('login'))

