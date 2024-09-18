from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    path_to_pic = url_for("static", filename="i.webp")
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Страница не найдена</title>
        <link rel="stylesheet" href="static/lab1.css">
    </head>
        <body>
            <div class="container">
                <h1>Ой, страница не найдена!</h1>
                <p>К сожалению, запрашиваемая вами страница не существует. Пожалуйста, проверьте URL или вернитесь на главную.</p>
                <img src="''' + path_to_pic + '''">
                <br>
                <a href="/">Вернуться на главную</a>
            </div>
        </body>
    </html>
    ''', 404

@app.route('/lab1/400')
def bad_request():
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Запрос некорректен</h1>
            </body>
        </html>
        ''', 400

@app.route('/lab1/401')
def unauthorized():
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Необходима авторизация</h1>
            </body>
        </html>
        ''', 401

@app.route('/lab1/402')
def payment_required():
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Требуется оплата</h1>
            </body>
        </html>
        ''', 401

@app.route('/lab1/403')
def forbidden():
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Доступ запрещен</h1>
            </body>
        </html>
        ''', 403

@app.route('/lab1/405')
def method_not_allowed():
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Метод запроса недопустим</h1>
            </body>
        </html>
        ''', 405

@app.route('/lab1/418')
def im_a_teapot():
    return '''
        <!doctype html>
        <html>
            <body>
                <h1>Запрос не может быть выполнен, так как сервер является чайником</h1>
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
        <link rel="stylesheet" href="static/lab1.css">
    </head>
    <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
        <main> 
             <div class ="menu">
                <ol>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                </ol>
            </div>
        </main>
        <footer>
            Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024
        </footer>
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
        <link rel="stylesheet" href="static/lab1.css">
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
                <li><a href="/lab1/created">Создано</a></li>
                <li><a href="/lab1/error500">Ошибка500</a></li>
                <li><a href="/lab1/web">Сервер</a></li>
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
    return """<!doctype html>
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
    <!doctype html>
        <html>
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
    css_style_path = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <title>Oak Tree</title>
        <link rel="stylesheet" href="''' + css_style_path + '''">
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
<!doctype html>
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

@app.route('/lab1/created')
def created():
    return '''
<!doctype html>
<html>
    <body>
      <h1>Создано успешно</h1>
      <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

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
    <div class="container">
        <h1>Дубовые дубы</h1>
        <p>Большинство дубов — крупные, мощные деревья. Многие виды этого рода принадлежат к числу вечнозелёных растений с кожистыми листьями, сохраняющимися на растении по нескольку лет. У других видов листья опадают ежегодно или, высыхая, остаются на дереве и разрушаются постепенно. Большинство вечнозелёных видов имеют цельные листья, остальные — лопастные.</p>
        <img src="''' + path_to_img + '''" alt="Изображение для лабораторной работы">
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
