
# https://virtualzero.net/blog/connect-a-flask-app-to-a-mysql-database-with-sqlalchemy-and-pymysql

from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

userpass = 'mysql+pymysql://root:test'
basedir  = '172.17.0.3'
dbname   = '/mysql'
#socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
#dbname   = dbname + socket
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'


if __name__ == '__main__':
    app.run(debug=True)
