from flask import Flask
app = Flask(__name__)

@app.route("/web")
def web():
    return """<!dostype html>
        <html>
           <body>
               <h1>web-сервер на flask<h1>
               <a href="/author">author</a>
           </body>
        </html>"""

@app.route("/author")
def author():
    name = "Трохин Данил Витальевич"
    group = "ФБИ-21"
    faculty = "ФБ"
    
    return """<!dostype html>
        <html>
           <body>
               <p>Студент: """ + name + """<p>
               <p>Студент: """ + group + """<p>
               <p>Студент: """ + faculty + """<p>
               <a href="/web">web</a>
           </body>
        </html>"""