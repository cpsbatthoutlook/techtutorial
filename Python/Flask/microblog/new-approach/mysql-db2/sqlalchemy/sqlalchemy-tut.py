from sqlalchemy import create_engine

#https://github.com/besnik/tutorials/tree/master/sqlalchemy
#https://www.youtube.com/watch?v=woKYyhLCcnU

engine = create_engine('mysql+pymysql://root:test@172.17.0.3:3306/test')
#engine = create_engine("sqlite:///some.db") # create sqlite db. use "////" to specify absolute path
# engine = create_engine("sqlite:///:memory:", echo=True)

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

#engine-1-select.py
#CREATE TABLE EMPLOYEE (EMP_ID INTEGER PRIMARY KEY, EMP_NAME VARCHAR(30));
engine.execute("""CREATE TABLE emp (id INTEGER PRIMARY KEY, name VARCHAR(50))""")
# insert data (connectionless execution (via engine))
engine.execute("INSERT INTO emp (name) VALUES (:name)", name="Slavo")
engine.execute("INSERT INTO emp (name) VALUES (:name)", name="Jano")
engine.execute("INSERT INTO emp (name) VALUES (:name)", name="Vlado")
