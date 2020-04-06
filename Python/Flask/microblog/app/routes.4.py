from flask import render_template
from app import app
@app.route('/a')
@app.route('/index')
def index1():
    user = {'username': 'Chander'}
    posts = [
        {
            'author': {'username': 'user1'},
            'body': 'Beautifule user1'
        },
        {
            'author': {'username': 'user2'},
            'body': 'Beautifule user2'
        }
    ]
    return render_template('index.html', title='234234', user=user, posts=posts)
    # index.3.html
    # index.4.html , base.html