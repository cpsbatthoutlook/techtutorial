import sqlite3

#https://www.alexforencich.com/wiki/en/scripts/python/percentile 
class PercentileFunc:
    def __init__(self):
        self.list = []
        self.percent = None
 
    def step(self, value, percent):
        if value is None:
            return
        if self.percent is None:
            self.percent = percent
        if self.percent != percent:
            return
        self.list.append(value)
 
    def finalize(self):
        if len(self.list) == 0:
            return None
        self.list.sort()
        return self.list[int(round((len(self.list)-1)*self.percent/100.0))]
 
# with sqlite3.connect(':memory:') as con:
with sqlite3.connect('csm_singlefile_20200420.db') as con:
 
    con.create_aggregate("percentile", 2, PercentileFunc)
    cur = con.cursor()

    cur.execute("select percentile(iops, 90) from csm")
    print("percentile: %f" % cur.fetchone()[0])

    # cur.execute("create table test(i)")
    # cur.executemany("insert into test(i) values (?)", [(k,) for k in range(100)])
    # cur.execute("insert into test(i) values (null)")
    # cur.execute("select avg(i) from test")
    # print("avg: %f" % cur.fetchone()[0])
    # cur.execute("select percentile(i, 90) from test")
    # print("percentile: %f" % cur.fetchone()[0])