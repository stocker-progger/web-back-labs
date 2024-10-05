from flask import Blueprint, url_for, redirect, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/')
def laba():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/a')
def a1():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = ['лилия', 'ландыш', 'ромашка', 'гвоздика']


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return f'''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Информация о цветке</title>
                <link rel="stylesheet" href="/static/lab1/lab1.css">
            </head>
            <body>
                <h1>Информация о цветке</h1>
                <h2>Цветок: {flower_list[flower_id]} - отличный выбор!</h2>
                <p>Идентификатор: {flower_id}</p>
                <a href="/lab2/all_flowers">Посмотреть все цветы</a><br>
                <a href="/lab2/add_flower/">Добавить новый цветок</a>
            </body>
        </html>
        '''


@lab2.route('/lab2/add_flower/')
def no_flower():
    return f'''
    <!DOCTYPE html>
        <html>
            <head>
                <title>Ошибка!</title>
                <link rel="stylesheet" href="/static/lab1/lab1.css">
            </head>
            <body>
                <p>вы не задали имя цветка!</p>
                <a href="/lab2/all_flowers">Посмотреть все цветы</a><br>
                <a href="/lab2/add_flower/">Добавить новый цветок</a>
            </body>
        </html>
        ''', 400



@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name) 
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Добавление цветка</title>
            <link rel="stylesheet" href="/static/lab1/lab1.css">
        </head>
        <body>
            <h1>Добавлен новый цветок</h1>
            <p> Название нового цветка: {name}</p>
            <p> Всего цветов: {len(flower_list)}</p>
            <p> Полный список: {flower_list}</p>
            <a href="/lab2/all_flowers">Посмотреть все цветы</a><br>
            <a href="/lab2/add_flower/">Добавить новый цветок</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/all_flowers/')
def all_flowers():
    all_flowers = ""
    for i in flower_list:
        all_flowers += f"<li>{i}</li>"

    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Список всех цветов</title>
            <link rel="stylesheet" href="/static/lab1/lab1.css">
        </head>
        <body>
            <h1>Все цветы</h1>
            <p>Количество цветов: {len(flower_list)}</p>
            <ul>
                {all_flowers}
            </ul>
            <a href="/lab2/add_flower/">Добавить новый цветок</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        del flower_list[flower_id]
        return redirect(url_for('lab2.all_flowers')) 


@lab2.route('/lab2/delete_flowers')
def del_flowers():
    flower_list.clear()
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Список цветов очищен</title>
            <link rel="stylesheet" href="/static/lab1/lab1.css">
        </head>
        <body>
            <h1>Список цветов был очищен</h1>
            <p>Все цветы удалены.</p>
            <a href="/lab2/all_flowers">Посмотреть список цветов</a>
        </body>
    </html>
    '''


@lab2.route('/lab2/example')
def example():

    name, lab_num, group, course = 'Данил Трохин', 2, 'ФБИ-21', 3
    fruits = [
        {'name': 'яблок', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('lab2/example.html',
                           name=name, lab_num=lab_num, group=group,
                           course=course, fruits=fruits)


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase=phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calculate(a, b):
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Калькулятор</title>
        </head>
        <body>
            <h1>Расчёт с параметрами:</h1>
            <p>{a} + {b} = {a + b}</p>
            <p>{a} - {b} = {a - b}</p>
            <p>{a} * {b} = {a * b}</p>
            <p>{a} / {b} = {(a / b) if b != 0 else 'Деление на ноль'}</p>
            <p>{a}<sup>{b}</sup> = {a ** b}</p>
        </body>
    </html>
    '''


@lab2.route('/lab2/calc/')
def calc():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>/')
def calc_one(a):
    return redirect(f'/lab2/calc/{a}/1')


books = [
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 470},
    {"author": "Лев Толстой", "title": "Анна Каренина", "genre": "Роман", "pages": 864},
    {"author": "Борис Пастернак", "title": "Доктор Живаго", "genre": "Роман", "pages": 704},
    {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Поэма", "pages": 240},
    {"author": "Фёдор Достоевский", "title": "Идиот", "genre": "Роман", "pages": 640},
    {"author": "Иван Гончаров", "title": "Обломов", "genre": "Роман", "pages": 560},
    {"author": "Николай Гоголь", "title": "Мёртвые души", "genre": "Роман", "pages": 352},
    {"author": "Антон Чехов", "title": "Чайка", "genre": "Пьеса", "pages": 120}
]


@lab2.route('/lab2/books')
def show_books():
    return render_template('lab2/books.html', books=books)


places = [
    {"name": "Собор Александра Невского", "description": "Был построен аж в 1899 году!", "image":"sobor.jfif"},
    {"name": "Театр оперы и балета", "description": "Самый большой театр России!", "image": "novat.jfif"},
    {"name": "Новосибирский зоопарк имени Р. А. Шило", "description": "Один из крупнейших зоопарков России, содержащий больше 11 тыс. животных.", "image": "zoo.jfif"},
    {"name": "Музей железнодорожной техники", "description": "Железная дорога и поезда сыграли немалую роль в развитии Новосибирска, поэтому заслужили собственный музей.", "image": "gd.jfif"},
    {"name": "Театр «Глобус»", "description": "Просто красивое место.", "image": "globus.jfif"}
]


@lab2.route('/lab2/places')
def show_places():
    return render_template('lab2/places.html', places=places)
