from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html') #Jinja - шаблонизированный язык https://pythonru.com/uroki/7-osnovy-shablonizatora-jinja

@app.route('/forma',methods=['GET','POST'])
def login(name=None):
    if request.method=='GET':
        return render_template('forma.html')
    else:
        name=request.form['first_form']
    return render_template('index.html',name=name)


host='127.0.0.1'
port=8080
app.run(host,port,debug=True)