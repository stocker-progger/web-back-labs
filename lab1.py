from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1', __name__)


@lab1.route('/lab1/400')
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


@lab1.route('/lab1/401')
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


@lab1.route('/lab1/402')
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


@lab1.route('/lab1/403')
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


@lab1.route('/lab1/405')
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


@lab1.route('/lab1/418')
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


@lab1.route('/lab1')
def lab():
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


@lab1.route("/lab1/web")
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


@lab1.route("/lab1/author")
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


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/counter')
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


@lab1.route('/lab1/decounter')
def decounter():
    global count
    count = 0
    return redirect("/lab1/counter")


@lab1.route('/lab1/info')
def info():
    return redirect("/lab1/author")


@lab1.route('/lab1/error500')
def trigger_error():
    return 1 / 0


@lab1.route('/lab1/customlg')
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
@lab1.route('/lab1/created')
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


@lab1.route('/lab1/delete')
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

 
@lab1.route('/lab1/resource')
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


