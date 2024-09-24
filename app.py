from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

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

@app.route('/lab1/400')
def bad_request():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ошибка</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Запрос некорректен!</h1>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 400


@app.route('/lab1/401')
def unauthorized():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ошибка</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Необходима авторизация!</h1>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 401

@app.route('/lab1/402')
def payment_required():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ошибка</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Требуется оплата!</h1>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 402

@app.route('/lab1/403')
def forbidden():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ошибка</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Доступ запрещен!</h1>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 403

@app.route('/lab1/405')
def method_not_allowed():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ошибка</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Метод запроса недопустим!</h1>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 405

@app.route('/lab1/418')
def im_a_teapot():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ошибка</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <header>Ошибки тоже могут быть красивыми..</header>
        <main>
            <div>
                <h1>Запрос не может быть выполнен, так как сервер является чайником!</h1>
                <a href="/">Вернуться на главную</a>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
    </body>
    </html>
    ''', 418

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


@app.route("/lab1/web")
def web():
    return """<!DOCTYPE html>
        <html>
           <body>
               <h1>web-сервер на flask<h1>
           </body>
        </html>""", 200, {
            "X-Server": "sample",
            'Content-Type': 'text/html; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    name = "Трохин Данил Витальевич"
    group = "ФБИ-21"
    faculty = "ФБ"
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Страница автора</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
        <body>
            <p>Студент: """ + name + """<p>
            <p>Студент: """ + group + """<p>
            <p>Студент: """ + faculty + """<p>
            <a href="/lab1/web">web</a>
        </body>
    </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title>Oak Tree</title>
        <link rel="stylesheet" href="/static/lab1.css">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!DOCTYPE html>
<html>
    <body>
        Сколько раз вы сюда заходили:''' + str(count) + '''<br>
        <a href="/lab1/decounter">Очистить</a> <br>
    </body>
</html>
'''
@app.route('/lab1/decounter')
def decounter():
    global count
    count = 0
    return redirect("/lab1/counter")

@app.route('/lab1/info')
def info():
    return redirect("/lab1/author")

@app.route('/lab1/error500')
def trigger_error():
    return 1 / 0

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


@app.route('/lab1/customlg')
def custom_route():
    path_to_img = url_for('static', filename='oak.jpg') 
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <link rel="stylesheet" href="/static/lab1.css">
</head>
<body>
    <div>
        <h1>Дубовые дубы</h1>
        <p>Большинство дубов — крупные, мощные деревья. Многие виды этого рода принадлежат к числу вечнозелёных растений с кожистыми листьями, сохраняющимися на растении по нескольку лет. У других видов листья опадают ежегодно или, высыхая, остаются на дереве и разрушаются постепенно. Большинство вечнозелёных видов имеют цельные листья, остальные — лопастные.</p>
        <img src=''' + path_to_img + '''>
        <p>Цветки раздельнополые, мужские и женские находятся на одном и том же растении. Женские цветки образуют небольшие пучки или серёжки, мужские собраны в висящие или стоячие, часто длинные серёжки.</p>
        <p>Цветочные покровы простые, слабо развитые, но при основании женских цветов формируется множество чешуевидных листочков, расположенных на кольчатом валике, который является разросшимся цветоложем. При созревании плодов этот валик вместе со своими чешуями разрастается ещё больше и таким образом формируется характерное блюдце или «шапочка» — плюска, которая облекает снизу дубовый плод, или жёлудь. У разных видов дуба величина желудей и форма чешуек крайне разнообразны: у одних чешуйки весьма малы, у других, как у дуба венгерского, длиной почти в сантиметр, отвёрнуты и т. д. Завязь цветков дуба почти всегда трёхгнёздая; но во время созревания плодов разрастается только одно гнездо и получается односемянный плод с крепким кожистым околоплодником, причисляемый к числу орехообразных плодов.</p>
        <a href="/">Вернуться на главную</a>
    </div>
</body>
</html>
    ''', 200, {
        'Content-Language': 'ru',
        'X-Custom-Header-1': 'ba',
        'X-Custom-Header-2': 'nok'
    }

# Переменная для хранения состояния ресурса (создан или нет)
resource_created = False

# Обработчик для создания ресурса
@app.route('/lab1/created')
def created():
    path_to_img = url_for('static', filename='oak.jpg') 
    to_img = url_for('static', filename='дуб_м.jpg') 
    global resource_created
    if resource_created:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
            <body>
                <h1>Отказано!</h1>
                <img src=''' + path_to_img + '''>
                <p>Дуб уже посажен.</p>
            </body>
        </html>
        ''', 400
    else:
        resource_created = True
        return '''
        <!DOCTYPE html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <html>
            <body>
                <h1>Успешно!</h1>
                <img src="''' + to_img + '''" height = "30%"  width="30%">
                <p>Дуб был успешно посажен.</p>
            </body>
        </html>
        ''', 201

@app.route('/lab1/delete')
def delete():
    hole = url_for('static', filename='яма.jpg') 
    grass = url_for('static', filename='трава.webp') 
    global resource_created
    if resource_created:
        resource_created = False
        return '''
        <!DOCTYPE html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <html>
            <body>
                <h1>Успешно!</h1>
                <img src="''' + hole + '''" width = "50%">
                <p>Дуб был успешно вырыт.</p>
            </body>
        </html>
        ''', 200
    else:
        return '''
        <!DOCTYPE html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <html>
            <body>
                <h1>Отказано!</h1>
                <img src="''' + grass + '''" width = "50%">
                <p>Дуб не существует.</p>
            </body>
        </html>
        ''', 400
    
@app.route('/lab1/resource')
def resource_status():
    global resource_created
    if resource_created:
        status = "Дуб посажен"
    else:
        status = "Дуб ещё не посажен"
    
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Статус ресурса</title>
            <link rel="stylesheet" href="/static/lab1.css">
        </head>
        <body>
            <h1>Статус дуба: {status}</h1>
            <a href="/lab1/created">Посадить дуб</a><br>
            <a href="/lab1/delete">Вырыть дуб</a>
        </body>
    </html>
    '''
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

@app.route('/lab2/delete_flowers')
def delete_flowers():
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
