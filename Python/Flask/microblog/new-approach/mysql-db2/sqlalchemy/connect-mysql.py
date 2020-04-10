from sqlalchemy import create_engine
import pymysql


# https://docs.sqlalchemy.org/en/13/core/engines.html
engine = create_engine('mysql+pymysql://root:test@172.17.0.3:3306/mysql')
# engine = create_engine('sqlite:///foo.db')

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

with engine.connect() as connection:  #https://docs.sqlalchemy.org/en/13/core/connections.html
    result = connection.execute("Select 1")
    for row in result:
        print('value  : {} '.format(row['1']))

