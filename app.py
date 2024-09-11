from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask<h1>
               <a href="/lab1/author">author</a> <br>
               <a href="/lab1/oak">Дуб</a> <br>
               <a href="/lab1/counter">Счетчик</a> <br>
           </body>
        </html>""", 200, {
            "X-Server": "sample",
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    name = "Трохин Данил Витальевич"
    group = "ФБИ-21"
    faculty = "ФБ"
    
    return """<!doctype html>
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