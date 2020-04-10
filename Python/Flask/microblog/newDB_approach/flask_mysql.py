from flask import Flask
from flask import request, redirect,render_template
from flask_mysqldb import MySQL

#https://www.codementor.io/@adityamalviya/python-flask-mysql-connection-rxblpje73
#https://flask-mysqldb.readthedocs.io/en/latest/

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'MyDB'
#
# OR
#
#use db.yaml file   mysql_host: 'localhost' \n mysql_user: 'root'  ....

import yaml
db = yaml.load('db.yaml')
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['userpasswd']
app.config['MYSQL_DB'] = db['appname']

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'] )
def main():
    return "Welcome"
    if request.method == 'POST':
        data  = request.form
        name = data['name']
        email = data['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email ))
        mysql.conection.commit()  #https://flask-mysqldb.readthedocs.io/en/latest/
    return render_template('index.html')


@app.route('/', methods=['GET','POST'] )
def main():
        cur = mysql.connection.cursor()
        rv = cur.execute("SELCT * FROM USERS")
        if rv > 0:
            data = cur.fetchall()
            return render_template('user.html')  ##User Jinja template
            
if __name__ == "__main__":
    app.run(debug=True)