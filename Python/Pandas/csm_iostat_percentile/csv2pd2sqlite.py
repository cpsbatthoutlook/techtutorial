#  for x in sbpsvrsp261 sbpsvrsp262 sbpsvrwm261 sbpsvrwm262; do
#   # zcat ${x}*.gz | perl -ane '($x,$b)=split(/2020/);$x=~s/\s+(\w)/_$1/g;$x=~s/(.*)\s+/${1}_2020/;print "$x $b" if /\d+t./;' > /tmp/${x}
#   # perl -ane 'print if /\d+t./ && length() < 109 && length()>102;' /tmp/${x} > /tmp/1
#   zcat ${x}*.gz | perl -ane 'print if /\d+t./ && length() < 109 && length()>102;' > /tmp/${x} 
#   # mv /tmp/1 /tmp/${x}
#  done
  
from datetime import datetime
import pandas as pd 
import numpy as ny
col=['TIME','ReadPerSec','WritePerSec','KReadPerSec','KWritePerSec','wsvc','ACTV','WSVC_T','ACTV_T','w','b','dEVICE']
import sqlite3
engine = sqlite3.connect('/tmp/data1.db')
engine.execute('DROP TABLE csm')

dfor = "%a %b %d %H:%M:%S %Y"
ofor = "%Y-%m-%d %H:%M:%S"

# https://honingds.com/blog/pandas-read_csv/#date_parser
# mydateparser = lambda x: pd.datetime.strptime(x, "%a_%b_%d_%H:%M:%S_%Y")
mydateparser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d-%H:%M:%S") #NewFormat


# Fri_Apr_17_16:07:25       120.6   71.7  350.2  224.8  0.0  0.1    0.0    0.7   0   8 c7t50060E8016062E15d0s2
# 2020-04-21-11:26:55   120.4   72.0  350.0  225.6  0.0  0.1    0.0    0.7   0   8 c7t50060E8016062E15d0s2 #New format

#sbpsvrsp261 sbpsvrsp262 sbpsvrwm261 sbpsvrwm262
for svr in ['sbpsvrsp261', 'sbpsvrsp262', 'sbpsvrwm261', 'sbpsvrwm262']:
  f='/tmp/'+svr
  df = pd.read_csv(f, names=col, sep='\s+', encoding = "iso-8859-1", parse_dates = ['TIME'] , date_parser = mydateparser,
    dtype={'b':'int8','KWritePerSec':'float16','WritePerSec':'float16','ACTV':'float16','ACTV_T':'float16','WSVC_T':'float16','ReadPerSec':'float16','w':'int8','wsvc':'float16','KReadPerSec':'float16'})
  df.fillna(0, inplace=True)
  df['K_RW'] = df['KReadPerSec'] + df['KWritePerSec']
  df['IOPS'] = df['ReadPerSec'] + df['WritePerSec']
  df['Servername']=svr
  print(svr)
  df.to_sql('csm', con=engine, if_exists='append') ##{'fail','replace','append'} ##https://www.dataquest.io/blog/python-pandas-databases/

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
# from sqlalchemy import create_engine
# engine = create_engine('sqlite://' + '/tmp/data1.db', echo=False)
# # engine = create_engine('sqlite://' , echo=False)
# df.to_sql('svr', con=engine)
# engine.execute("SELECT * FROM svr").fetchall()

#Read_SQL   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html
#           https://www.programcreek.com/python/example/101381/pandas.read_sql 
#           https://stackoverflow.com/questions/53839451/pandas-read-sql-with-where-clause-using-in 
import sqlite3
from datetime import datetime
import pandas as pd 
import numpy as np
dbfile='/tmp/data.db'
dbfile='csm_singlefile_20200421.db'
engine = sqlite3.connect(dbfile)
    # in_params=['sbpsvrsp261' ] #, 'sbpsvrsp262', 'sbpsvrwm261', 'sbpsvrwm262']
    # SQL = 'select * from csm where Servername in ({})'.format(', '.join(['?' for _ in in_params]))
    # df = pd.read_sql(SQL, con=engine, params=[in_params])
df = pd.read_sql('select * from csm', engine, columns=['TIME','device','Servername','K_RW', 'IOPS' ])
df.TIME = pd.to_datetime(df.TIME)
df['dt-hm'] = df.TIME.dt.strftime('%Y-%m-%d %H:%M')
df['dt-h'] = df.TIME.dt.strftime('%Y-%m-%d %H')
df['dt'] = df.TIME.dt.strftime('%Y-%m-%d')
df.drop(columns=['wsvc','ACTV','WSVC_T','ACTV_T','w','b'],inplace=True)
df.drop(columns=['ReadPerSec','WritePerSec','KReadPerSec','KWritePerSec','wsvc','ACTV','WSVC_T','ACTV_T','w','b'],inplace=True)



# Group by
df.groupby('dEVICE').agg('sum')  #https://kadekillary.work/post/embarrassment-of-pandas/#aggregation
#Pivot   https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html 
pd.pivot_table(df, values=['IOPS','K_RW'], index=['TIME'], columns=['dEVICE'], 
  aggfunc={'IOPS':[min, max, np.mean ], 'K_RW':[min, max, np.mean ]  } )


# >>> df.columns
# Index([u'index', u'TIME', u'ReadPerSec', u'WritePerSec', u'KReadPerSec',u'KWritePerSec', 
#     u' wsvc', u' ACTV', u'WSVC_T', u' ACTV_T', u'w', u'b',u'    ', u'K_RW', u'IOPS'], dtype='object')


## Test PivotTable
# t = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"],
#                         "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"],
#                         "C": ["small", "large", "large", "small", "small", "large", "small", "small", "large"],
#                         "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
#                         "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})


# table = pd.pivot_table(t, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)  # foo/bar, one/two -- large/small -- sum
# table = pd.pivot_table(t, values=['D','E'], index=['A', 'C'],  aggfunc={'D':np.mean, 'E':[min, max, np.mean] } )  # foo/bar, large/small --  mean D/E


## Percentile
for x in d.keys():
   print(x), 
   for i in ['IOPS','K_RW']:
     print(i), 
     np.percentile(df.loc[df['dEVICE'] == x][i], 98)

for svr in ['sbpsvrsp261', 'sbpsvrsp262', 'sbpsvrwm261', 'sbpsvrwm262']:
  print(svr),
  np.percentile(df.loc[df['Servername'] == svr ]['IOPS'],95)
  np.percentile(df.loc[df['Servername'] == svr ]['K_RW'],95)

np.percentile(df['IOPS'],95)
np.percentile(df['IOPS'],95,axis=0)  #https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html
df.groupby(['Servername','device'])['IOPS','K_RW'].quantile(.95)
df.groupby(['dt','Servername'])['IOPS','K_RW'].quantile(.95)


## Matplotlib  https://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
import matplotlib.pyplot as plt

x=df.loc[df['Servername'] == 'sbpsvrsp261']
x[['TIME','IOPS']].sort_values(by=['TIME']).plot(x='TIME', y='IOPS',kind='bar') #
#Scatter diagram
# Line chart
# Bar chart
# Pie chart
x[['TIME','IOPS']].plot(x='TIME', y='IOPS', kind='scatter')
plt.show()


#Line Graph
df.groupby(['Servername','device'])['IOPS','K_RW'].quantile(.95).plot()
plt.show()
