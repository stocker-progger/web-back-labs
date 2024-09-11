from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route("/web")
def web():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask<h1>
               <a href="/author">author</a> <br>
               <a href="/lab1/oak">Дуб</a> <br>
               <a href="/lab1/count">Счетчик</a> <br>
           </body>
        </html>""", 200, {
            "X-Server": "sample",
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/author")
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
               <a href="/web">web</a>
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
        Сколько раз вы сюда заходили:''' + str(count) + '''
    </body>
</html>
'''

@app.route('/info')
def info():
    return redirect("/author")

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