from flask import render_template
from app import app
@app.route('/a')
@app.route('/index')
def index1():
    user = {'username': 'Chander'}
    return render_template('index.html', title='234234', user=user)
    # index.2.html