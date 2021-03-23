from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='world'):
    if name is not None:
        return render_template('base.html',name='sdfghjkl')

host='127.0.0.1'
port=8080
app.run(host,port,debug=True)