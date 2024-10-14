from flask import Blueprint, url_for, request, redirect, render_template
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def laba4():
    return render_template('/lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])  # Добавляем метод POST
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    try:
        x1 = int(x1)
        x2 = int(x2)
        if x2 == 0:
            return render_template('lab4/div.html', error='На ноль делить нельзя!')
        
        result = x1 / x2
    except ValueError:
        return render_template('lab4/div.html', error='Введите целые числа!')

    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)