from flask import Flask

# app = Flask(__name__ , instance_relative_config=True)
app = Flask(__name__)

# from config import Config
#Web Forms
app.config['SECRET_KEY']= 'abc123'  # not good for separation of duties, use import config...
# app.config.from_object(Config)


from app import routes

