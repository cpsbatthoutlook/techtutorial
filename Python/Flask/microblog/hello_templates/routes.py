from hello_templates import cps
from flask import render_template

@cps.route('/')
@cps.route('/index')

def index():
    user = {'user':  'Frank'}
    title = 'MyTitle'
    icount = ['range(5)']
    # return "Hello World!!"
    return render_template('base.html', cps_title='title', user='fs', cnt=range(3))