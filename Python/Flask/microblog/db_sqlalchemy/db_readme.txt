sqlalchemy: https://www.sqlalchemy.org/ 
    ORM with underlying wide layers of datbases, MySQL, Postgres, Sqlite, others


Reference: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
            https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

pip install flask-sqlalchemy


 pip install flask-migrate #more migrate/update/expand

 set FLASK_APP=db-flask-app.py
 ## Setup __init__.py with App, DB, SQLITE file, and Migrate funcs
    Setup Models and set the same 
    Run "flask db init"
                Creating directory C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations ...  done
                Creating directory C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations\versions ...  done
                Generating C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations\alembic.ini ...  done
                Generating C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations\env.py ...  done
                Generating C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations\README ...  done
                Generating C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations\script.py.mako ...  done
                Please edit configuration/connection/logging settings in 'C:\\Temp\\workspace\\PyWork\\Flask\\microblog\\db_sqlalchemy\\migrations\\alembic.ini' before proceeding.
    Run "flask db migrate "users table" 
                INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
                INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
                INFO  [alembic.autogenerate.compare] Detected added table 'user'
                INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
                INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
                Generating C:\Temp\workspace\PyWork\Flask\microblog\db_sqlalchemy\migrations\versions\9052f83156f3_users_table.py ...  done
    Run - flask db upgrade   ##Will create DB file
                INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
                INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
                INFO  [alembic.runtime.migration] Running upgrade  -> 9052f83156f3, users table


## Manually testing in Python [ outside the db_sqlalchemy ]

from db_sqlalchemy import db
from db_sqlalchemy import fdb
from db_sqlalchemy.models  import User, Post

u = User(username='user1', email='user1@email.com')
db.session.add(u)
db.session.commit()
u = User(username='user2', email='user2@email.com')
db.session.add(u)
db.session.commit()

u = User.query.all()
u 
for i in u:
    print(i.id, i.email, i.username)

    
