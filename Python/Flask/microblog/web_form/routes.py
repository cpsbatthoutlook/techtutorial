from web_form import webform
from flask import render_template
from flask import flash, redirect
from web_form.forms import LoginForm

@webform.route('/')
@webform.route('/index')
def index():
    return render_template('base.html', title="FormTitle")

@webform.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user: {}, password {}, and other data '.format(form.user.data, form.password.data) )
        return redirect('/')
    return render_template('login.html', f=form, title='Sign In')