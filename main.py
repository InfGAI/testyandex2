from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html') #Jinja - шаблонизированный язык https://pythonru.com/uroki/7-osnovy-shablonizatora-jinja

host='127.0.0.1'
port=8080
app.run(host,port,debug=True)