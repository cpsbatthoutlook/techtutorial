from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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
    # forms.1.html

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requeted for user {} , remember_me = {} '. format(
            form.username.data, form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)
