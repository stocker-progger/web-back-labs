from flask import Flask, url_for, redirect, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)


@app.errorhandler(404)
def not_found(err):
    path_to_pic = url_for("static", filename="lab1/i.webp")
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Страница не найдена</title>
        <link rel="stylesheet" href="/static/lab1/lab1.css">
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
        <link rel="stylesheet" href="/static/lab1/lab1.css">
    </head>
    <body>
        <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
        <main> 
             <div class ="menu">
                <ol>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                    <li><a href="/lab2/">Вторая лабораторная</a></li>
                    <li><a href="/lab3/">Третья лабораторная</a></li>
                    <li><a href="/lab4/">Четверта лабораторная</a></li>
                </ol>
            </div>
        </main>
        <footer>Трохин Данил Витальевич, ФБИ-21, 3 курс, 2024</footer>
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
            <link rel="stylesheet" href="/static/lab1/lab1.css">
        </head>
        <body>
            <div>
                <h1>Произошла ошибка на сервере</h1>
                <p>К сожалению, при обработке вашего запроса возникла ошибка. Учите математику...</p>
                <a href="/">Вернуться на главную</a>
            </div>
        </body>
    </html>
    ''', 500

