from flask import Flask, render_template,request,json
# https://github.com/PyMySQL/PyMySQL
import pymysql.cursors

# https://ampersandacademy.com/tutorials/flask-framework/flask-framework-mysql-connection-using-pymysql
# ##Create SQL database
# create database test;
# # use test;
# create table userdata (id int(2) primary key auto_increment, username text, email text,
#    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#   dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP); # https://dev.mysql.com/doc/refman/5.7/en/timestamp-initialization.html

# https://pymysql.readthedocs.io/en/latest/modules/cursors.html
import pymysql.cursors
# Connect to the database
pymysql.connections.DEBUG = True
connection = pymysql.connect(host='172.17.0.3',user='root',password='test',db='test',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask(__name__)

@app.route("/")
@app.route("/get-reg")
def login():
    # return render_template('reg.html')
     try:
      with connection.cursor() as cur:
        # curl  http://127.0.0.1:5000
        # Read a single record
        sql = "SELECT * FROM userdata"
        cur.execute(sql)
        print(cur.description)
        print()
        for row in cur:
            print(row)
        cur.close()
     finally:
      connection.close()
      return "Saved successfully."

@app.route('/save-post',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
     # curl -d "user=user1&email=user1@email.com" http://127.0.0.1:5000/save-post
     name=request.form['name']
     email=request.form['email']
     try:
      with connection.cursor() as cursor:
      # Read a single record
        sql = "INSERT INTO userdata (username,email) VALUES (%s, %s)"
        cursor.execute(sql, (name,email))
        connection.commit()
     finally:
      connection.close()
      return "Saved successfully."
    else:
      return "error"

if __name__ == "__main__":
    app.run()