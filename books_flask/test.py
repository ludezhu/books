
args = (id, type)
cur.execute('select id,name from user_table where id = %s and name = %s', args )
rs=c.execute("select * from log where f_UserName=:usr",{"usr":"jetz"})
rs=c.execute("select * from log where f_UserName=:1 ",["jetz"])

cxn=psycopg2.connect(database='lap',user='postgres',password='root')
cur = cxn.cursor()
cur.execute('insert into t_user (username,password) VALUES (%s,%s)',('%ab','*'))
cur.execute('select * from t_user where username = %s',("%ab",))
rows = cur.fetchall()
cur.execute('delete from t_user where userid = %s',(14,))
cur.execute('select * from t_user where password = %s',("*",))

sql = "select id,name from user_table where id = %s and name = %s" % (id, name)
cur.execute(sql)
