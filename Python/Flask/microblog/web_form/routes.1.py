from web_form import webform
from flask import render_template
from web_form.forms import LoginForm

@webform.route('/')
@webform.route('/index')
def index():
    return render_template('base.html', title="FormTitle")

@webform.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', f=form, title='Sign In')