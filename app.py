from flask import Flask, url_for, redirect, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.errorhandler(404)
def not_found(err):
    path_to_pic = url_for("static", filename="i.webp")
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Страница не найдена</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Ой, страница не найдена!</h1>
                <p>К сожалению, запрашиваемая вами страница не существует. Пожалуйста, проверьте URL или вернитесь на главную.</p>
                <img src="''' + path_to_pic + '''"><br>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 404


@app.route('/')
@app.route('/index')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
        <main> 
             <div class ="menu">
                <ol>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                    <li><a href="/lab2">Вторая лабораторная</a></li>
                </ol>
            </div>
        </main>
        <footer>Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024</footer>
    </body>
    </html>
    '''


@app.route('/lab1')
def lab1():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Лабораторная работа 1</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Лабораторная работа 1</header>
        <main> 
            <p>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </p> <br>
            <a href="/">Возврат на главную страницу</a> <br>

            <h2>Список роутов</h2>
            <ul>
                <li><a href="/">Главная страница</a></li>
                <li><a href="/lab1/author">Автор</a></li>
                <li><a href="/lab1/oak">Дуб</a></li>
                <li><a href="/lab1/counter">Счетчик</a></li>
                <li><a href="/lab1/customlg">Заголовки</a></li>
                <li><a href="/lab1/error500">Ошибка500</a></li>
                <li><a href="/lab1/web">Сервер</a></li>
                <li><a href="/lab1/resource">Статус дуба</a></li>
            </ul>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    '''


@app.errorhandler(500)
def internal_error(err):
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Ошибка на сервере</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <body>
            <div>
                <h1>Произошла ошибка на сервере</h1>
                <p>К сожалению, при обработке вашего запроса возникла ошибка. Учите матиматику...</p>
                <a href="/">Вернуться на главную</a>
            </div>
        </body>
    </html>
    ''', 500


@app.route('/lab2/a')
def a1():
    return 'без слэша'


@app.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = ['лилия', 'ландыш', 'ромашка', 'гвоздика']


@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        return f'''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Информация о цветке</title>
                <link rel="stylesheet" href="/static/lab1.css">
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


@app.route('/lab2/add_flower/')
def no_flower():
    return "вы не задали имя цветка!", 400


@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Добавление цветка</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <body>
            <h1>Добавлен новый цветок</h1>
            <p> Название нового цветка: {name}</p>
            <p> Всего цветов: {len(flower_list)}</p>
            <p> Полный список: {flower_list}</p>
        </body>
    </html>
    '''


@app.route('/lab2/all_flowers/')
def all_flowers():
    all_flowers = ""
    for i in flower_list:
        all_flowers += f"<li>{i}</li>"

    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Список всех цветов</title>
            <link rel="stylesheet" href="/static/lab1.css">
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


@app.route('/lab2/all_flowers_extra')
def all_flowers_extra():
    return render_template('flowers.html', flowers=flower_list)


@app.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        del flower_list[flower_id]
        return redirect(url_for('all_flowers'))


@app.route('/lab2/delete_flowers')
def del_flowers():
    flower_list.clear()
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Список цветов очищен</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <body>
            <h1>Список цветов был очищен</h1>
            <p>Все цветы удалены.</p>
            <a href="/lab2/all_flowers">Посмотреть список цветов</a>
        </body>
    </html>
    '''


@app.route('/lab2/example')
def example():

    name, lab_num, group, course = 'Данил Трохин', 2, 'ФБИ-21', 3
    fruits = [
        {'name': 'яблок', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('example.html',
                           name=name, lab_num=lab_num, group=group,
                           course=course, fruits=fruits)


@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)


@app.route('/lab2/calc/<int:a>/<int:b>')
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


@app.route('/lab2/calc/')
def calc():
    return redirect('/lab2/calc/1/1')


@app.route('/lab2/calc/<int:a>/')
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


@app.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)


places = [
    {"name": "Собор Александра Невского", "description": "Был построен аж в 1899 году!", "image":"собор.jfif"},
    {"name": "Театр оперы и балета", "description": "Самый большой театр России!", "image": "новат.jfif"},
    {"name": "Новосибирский зоопарк имени Р. А. Шило", "description": "Один из крупнейших зоопарков России, содержащий больше 11 тыс. животных.", "image": "зоо.jfif"},
    {"name": "Музей железнодорожной техники", "description": "Железная дорога и поезда сыграли немалую роль в развитии Новосибирска, поэтому заслужили собственный музей.", "image": "жд.jfif"},
    {"name": "Театр «Глобус»", "description": "Просто красивое место.", "image": "глобус.jfif"}
]


@app.route('/lab2/places')
def show_places():
    return render_template('places.html', places=places)


