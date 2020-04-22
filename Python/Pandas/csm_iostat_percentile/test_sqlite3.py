from datetime import datetime
import sqlite3

header="r/s,w/s,kr/s,kw/s,wait,actv,wsvc_t,asvc_t,%w,%b,device"
data = "Mon Apr 20 07:00:54 2020"
dfor = "%a %b %d %H:%M:%S %Y"
ofor = "%Y-%m-%d %H:%M:%S"

f = open("sbpsvrsp262_data.txt")
raw_data = f.readlines()
f.close()



#Fri Apr 17 16:07:25 2020   120.6   71.7  350.2  224.8  0.0  0.1    0.0    0.7   0   8 c7t50060E8016062E15d0s2

# https://pymotw.com/3/sqlite3/
import csv, sqlite3,  sys
from datetime import datetime

db_filename = '/tmp/data.db'
# data_filename = sys.argv[1]
data_filename = '/tmp/abc.csv'

SQL = """
insert into svr (SVR, TIME,ReadPerSec, WritePerSec,KReadPerSec,KWritePerSec, wsvc, ACTV,WSVC_T, ACTV_T, w, b, dEVICE)
values (:SVR,:TIME ,:ReadPerSec,:WritePerSec,:KReadPerSec,:KWritePerSec,:wsvc,:ACTV,:WSVC_T,:ACTV_T,:w,:b,:dEVICE)
"""
CREATETABLE = """
        CREATE TABLE svr (SVR  VARCHAR(20),TIME DATETIME,ReadPerSec DECIMAL,WritePerSec DECIMAL,KReadPerSec DECIMAL, 
    KWritePerSec DECIMAL, WSVC DECIMAL, ACTV DECIMAL, WSVC_T DECIMAL, ACTV_T DECIMAL, W DECIMAL, B DECIMAL, Device  VARCHAR(50))""" 

with open(data_filename, 'rt') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            # cursor.execute(CREATETABLE)
            cursor.executemany(SQL, csv_reader)


# # hOW TO insert datatime in SQLite3 .. use format '2007-01-01 10:00:00'
# https://stackoverflow.com/questions/1933720/how-do-i-insert-datetime-value-into-a-sqlite-database

# CREATE TABLE svr (
#     SVR  VARCHAR(20),
#     TIME DATETIME,
#     ReadPerSec DECIMAL,
#     WritePerSec DECIMAL, 
#     KReadPerSec DECIMAL, 
#     KWritePerSec DECIMAL, 
#     WSVC DECIMAL, 
#     ACTV DECIMAL, 
#     WSVC_T DECIMAL, 
#     ACTV_T DECIMAL, 
#     W DECIMAL, 
#     B DECIMAL,
#     Device  VARCHAR(50)
# );

# insert into svr (SVR, TIME,ReadPerSec, WritePerSec,KReadPerSec,KWritePerSec, wsvc, ACTV,
#   WSVC_T, ACTV_T, w, b, dEVICE ) VALUES ( 'SVR1','2007-01-01 10:00:00', '0.0','2.0','0.0','2.0','0.0','0.0','0.0','0.2','0','0','c7t50060E8016062E04d0s2' );

 
from datetime import datetime
from pandas import pd 
col=['TIME', 'ReadPerSec', ' WritePerSec', 'KReadPerSec', 'KWritePerSec', ' wsvc', ' ACTV', 'WSVC_T', ' ACTV_T', ' w', ' b', ' dEVICE']
# perl -ane '($x,$b)=split(/2020/);$x=~s/\s+(\w)/_$1/g;print "$x   $b" if /\d+t./;' > /tmp/1.txt

f='/tmp/1.txt'
df = pd.read_csv(f, names=col, sep='\s+')

