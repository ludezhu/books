
import pymysql
 
def query_db(id, name):
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='test123',
                         database='TESTDB')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    sql = "select id,name from user_table where id = %s and name = %s" % (id, name)
    cursor.execute(sql)

