from flask import Blueprint, url_for, request, redirect, render_template, session, current_app
rgz = Blueprint('rgz', __name__)
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path


@rgz.route('/rgz/')
def rgz_main():
    return render_template('rgz/rgz.html', login=session.get('login'))


@rgz.route('/rgz/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('rgz/login.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('rgz/login.html', error='Заполните все поля')


@rgz.route('/rgz/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('rgz/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')