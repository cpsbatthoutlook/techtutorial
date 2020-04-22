https://docs.python.org/3/library/csv.html

SQlite3

https://www.techonthenet.com/sqlite/datatypes.php
https://docs.python.org/2/library/sqlite3.html
https://pymotw.com/3/sqlite3/
https://www.alexforencich.com/wiki/en/scripts/python/percentile

Pandas:  Summary 
	https://kadekillary.work/post/embarrassment-of-pandas/
	https://datatofish.com/convert-string-to-float-dataframe/
	https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
	#Matplotlib  Pandas
	https://proquestcombo-safaribooksonline-com.ezproxy.torontopubliclibrary.ca/book/databases/business-intelligence/9781839213106
	https://medium.com/@bingobee01/pandas-tricks-and-tips-a7b87c3748ea
	https://medium.com/@deallen7/managing-date-datetime-and-timestamp-in-python-pandas-cc9d285302ab

SQlite:

create table x as select * from csm limit 5;

# https://www.techonthenet.com/sqlite/functions/strftime.php
select strftime('%m-%d-%M',time), count(*) from t group by 1;
select datetime('now','localtime');
select datetime('now')

select time(time, '+2 hours') from t; #Add 2 hours
select date(time, '+23 days') from t;  ## Add 23 days



Pandas:
df.loc[df['Servername'] == 'sbpsvrsp261']
df.groupby(['Servername','device']).mean()
df.groupby(['Servername','device']).size()
np.percentile(df['IOPS'],95,axis=0)
df.groupby(['Servername','device'])['IOPS','K_RW'].quantile(.95)
df['year_of_birth'] = df['date_of_birth'].map(lambda x: x.strftime('%Y')) #

  #datetime
  x.TIME = pd.to_datetime(x.TIME)
  #'pandas.core.indexes.accessors.DatetimeProperties'>  https://medium.com/@deallen7/managing-date-datetime-and-timestamp-in-python-pandas-cc9d285302ab
  x.TIME.dt.week  [month, day, ]
  x.TIME.dt.strftime('%Y-%m-%d %H:%M') 

#https://www.geeksforgeeks.org/python-pandas-dataframe-where/
