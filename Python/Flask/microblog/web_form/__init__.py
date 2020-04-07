from flask import Flask

webform = Flask(__name__)
webform.config['SECRET_KEY']='this is a test'

from web_form import routes