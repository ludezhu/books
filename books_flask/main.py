# -*-coding:utf-8-*-
# @author ludezhu
# 2020/11/11下午2:55

from flask import Flask, jsonify
from books import Book

'''
接口说明：
1. 返回json数据
2.结构:
    {
        resCode: 0 ,    # 非0即错误，
        message: "说明"，
        data:[]        # 数组
    }
'''

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def helo_word():
    book = Book()
    arrData = book.get_books_infos_limit()
    return jsonify(arrData)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=1943, debug=True)