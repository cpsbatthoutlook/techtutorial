from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
basedir = os.path.abspath(os.path.dirname(__file__))

fdb = Flask(__name__)
fdb.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test-sqlite.db')
fdb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(fdb)
migrate = Migrate(fdb, db)

from db_sqlalchemy  import routes, models

