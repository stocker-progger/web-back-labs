from flask import Flask, url_for, redirect, render_template
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Подключение миграций
from flask_login import LoginManager
from db import db
from db.models import users

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9

app = Flask(__name__)

# Настройка для flask-login
login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

# Конфигурация Flask-приложения
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey12345')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Конфигурация базы данных
if app.config['DB_TYPE'] == 'postgres':
    db_name = 'danil_orm'
    db_user = 'danil_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432
    
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "danil_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

# Инициализация SQLAlchemy
db.init_app(app)  # Здесь мы только вызываем init_app

# Инициализация миграций
migrate = Migrate(app, db)

# Регистрируем Blueprints
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

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
                    <li><a href="/lab4/">Четвертая лабораторная</a></li>
                    <li><a href="/lab5/">Пятая лабораторная</a></li>
                    <li><a href="/lab6/">Шестая лабораторная</a></li>
                    <li><a href="/lab7/">Седьмая лабораторная</a></li>
                    <li><a href="/lab8/">Восьмая лабораторная</a></li>
                    <li><a href="/lab9/">Девятая лабораторная</a></li>
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
