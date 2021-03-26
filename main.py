import os
from data import db_session
from flask import Flask, render_template, request

app = Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           taste_of_day={'img': "img/table1.jpg", 'title': "Салат", 'discribe': "qqqqqqqqqqqqqqqqqqqq"})


@app.route('/singin')
def singin():
    return render_template('singin.html')


@app.route('/singup')
def singup():
    return render_template('singup.html')


@app.route('/recipe')
def recipe():
    return render_template('recipe.html')


@app.route('/foodinfo')
def foodinfo():
    return render_template('foodinfo.html')


@app.route('/rest')
def rest():
    return render_template('rest.html')


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    db_session.global_init("db/kitchen.db")
    # app.run(host='0.0.0.0', port=port)
    app.run('127.0.0.1', 8080, debug=True)
