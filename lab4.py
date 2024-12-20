from flask import Blueprint, url_for, request, redirect, render_template, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def laba4():
    return render_template('/lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])  
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
        
    result = x1 / x2

    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


# Суммирование
@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1:
        x1 = 0
    
    if not x2:
        x2 = 0
    
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2

    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

# Умножение
@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if not x1:
        x1 = 1
    
    if not x2:
        x2 = 1

    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2

    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)

# Вычитание
@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2

    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)

# Возведение в степень
@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')

@lab4.route('/lab4/pow', methods=['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if not x1 or not x2:
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', error='Оба значения не могут быть равны нулю!')
    result = x1 ** x2

    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)

tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut' and tree_count > 0:
        tree_count -= 1
    elif operation == 'plant' and tree_count < 10:
        tree_count += 1

    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Johnson', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Smith', 'gender': 'male'},
    {'login': 'sofa', 'password': '222', 'name': 'Sofia Petrova', 'gender': 'female'},
    {'login': 'momo', 'password': '333', 'name': 'Monica Garcia', 'gender': 'female'}
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            user = next(u for u in users if u['login'] == session['login'])
            return render_template('lab4/login.html', authorized=authorized, user=user)
        return render_template('lab4/login.html', authorized=False)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        return render_template('lab4/login.html', error='Не введён логин', login=login, authorized=False)

    if not password:
        return render_template('lab4/login.html', error='Не введён пароль', login=login, authorized=False)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')

    error = 'Неверные логин и/или парольь'
    return render_template('lab4/login.html', error=error, login=login, authorized=False)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')

    temperature = int(request.form.get('temperature'))

    if not temperature:
        return render_template('lab4/fridge.html', error='Ошибка: не задана температура')

    if temperature < -12:
        return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком низкое значение')
    elif temperature > -1:
        return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком высокое значение')
    elif -12 <= temperature <= -9:
        return render_template('lab4/fridge.html', temperature=temperature, snowflakes=3)
    elif -8 <= temperature <= -5:
        return render_template('lab4/fridge.html', temperature=temperature, snowflakes=2)
    elif -4 <= temperature <= -1:
        return render_template('lab4/fridge.html', temperature=temperature, snowflakes=1)

    return render_template('lab4/fridge.html')


# Цены на зерно
grain_prices = {
    'Ячмень': 12345,  
    'Овёс': 8522,     
    'Пшеница': 8722,    
    'Рожь': 14111      
}

@lab4.route('/lab4/grain-order', methods=['GET', 'POST'])
def grain_order():
    if request.method == 'GET':
        return render_template('lab4/grain_order.html')

    grain_type = request.form.get('grain')
    weight = float(request.form.get('weight'))

    if not weight:
        return render_template('lab4/grain_order.html', error='Ошибка: не указан вес заказа.')

    if weight <= 0:
        return render_template('lab4/grain_order.html', error='Ошибка: вес должен быть больше 0.')

    if weight > 500:
        return render_template('lab4/grain_order.html', error='Ошибка: такого объёма сейчас нет в наличии.')

    price_per_ton = grain_prices.get(grain_type)
    if price_per_ton is None:
        return render_template('lab4/grain_order.html', error='Ошибка: не выбран тип зерна.')

    total_cost = weight * price_per_ton

    # Применяем скидку
    if weight > 50:
        discount = total_cost * 0.10
        total_cost -= discount
        discount_message = f"Применена скидка за большой объём: {discount} руб."
    else:
        discount_message = ""

    return render_template('lab4/grain_order.html', grain=grain_type, weight=weight, total_cost=total_cost, discount_message=discount_message)