from flask import Blueprint, redirect, render_template, request, make_response
from datetime import datetime
lab4 = Blueprint('lab4', __name__)


@lab3.route('/lab3/')
def laba3():
    name = request.cookies.get('name', 'Анонимус') 
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age', ' ')
    return render_template('lab3/lab3.html', name=name, name_color=name_color,  age=age)


