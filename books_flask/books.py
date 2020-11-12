# -*-coding:utf-8-*-
# @author ludezhu
# 2020/11/12下午2:15

from pymysql import connect
from pymysql.cursors import DictCursor
from setting import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_CHATSET

class Book(object):
    def __init__(self):
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset=MYSQL_CHATSET
        )
        self.cursor = self.conn.cursor(DictCursor)  # 可以返回字典形式

    def __del__(self):   # 释放对象同时执行的代码
        self.cursor.close()
        self.conn.close()

    def get_books_infos_limit(self):
        sql = "select * from book_infos"
        self.cursor.execute(sql)
        # return data
        data = self.cursor.fetchall()
        return list(data)