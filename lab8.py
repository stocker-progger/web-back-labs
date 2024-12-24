from flask import Blueprint, render_template, jsonify, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def laba8():
    return render_template('lab8/lab8.html', login=session.get('login'))

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password') 

    if not login_form:
        return render_template('lab8/register.html', error='Имя пользователя не должно быть пустым')
    
    if not password_form:
        return render_template('lab8/register.html', error='Пароль не должен быть пустым')

    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return redirect('/lab8/')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html', error=None)

    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember = 'remember' in request.form  

    if not login_form:
        return render_template('lab8/login.html', error='Логин не должен быть пустым')

    if not password_form:
        return render_template('lab8/login.html', error='Пароль не должен быть пустым')

    user = users.query.filter_by(login=login_form).first()

    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember=remember)  
            return redirect('/lab8/')
    
    return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')

@lab8.route('/lab8/articles/')
@login_required
def article_list():
    all_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template('lab8/articles.html', articles=all_articles)

@lab8.route('/lab8/logout/', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if title and content:
            new_article = articles(title=title, content=content, user_id=current_user.id)
            db.session.add(new_article)
            db.session.commit()
            return redirect('/lab8/articles')
        else:
            return render_template('lab8/create.html', error="Название и содержание обязательны")

    return render_template('lab8/create.html')

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles.query.get_or_404(article_id)

    if article.user_id != current_user.id:
        return redirect('/lab8/')

    if request.method == 'POST':
        article.title = request.form.get('title')
        article.content = request.form.get('content')
        db.session.commit()
        return redirect('/lab8/articles')

    return render_template('lab8/edit.html', article=article)

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = articles.query.get_or_404(article_id)

    if article.user_id != current_user.id:
        return redirect('/lab8/')

    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/articles')
