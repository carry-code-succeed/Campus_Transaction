# -*- coding: UTF-8 -*-
import os
import json
from flask_cors import *
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=[ 'POST'])
def 查询1():
    import pymysql
    import time
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config)
    # 初始化游标（创建游标）
    cursor = db.cursor()
    # 执行查询，并返回受影响的行数
    cursor.execute("select * from COMMODITY")
    # 返回所有的结果集 
    result = cursor.fetchall()
    para = []
    for i in result:
        text = {'id':i[0],'name':i[1],'password':i[2],'IS_PUTAWAY':i[6]}
        para.append(text)
    db.close()
    return json.dumps(para, ensure_ascii=False, indent=4)
if __name__ == '__main__':
    app.run(host='192.168.3.159', port=5590,
#             ssl_context='adhoc'
           )