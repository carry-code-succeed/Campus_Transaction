# -*- coding: UTF-8 -*-
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/L_G/', methods=[ 'POST','GET'])
def Listing_goods():   # Listing_goods = 上架商品   传入参数和商品表的列名一致
    if request.method == 'GET':
        USER_ID = request.args.get("USER_ID")
        COMMODITY_NAME = request.args.get("COMMODITY_NAME")
        COMMODITY_INFO = request.args.get("COMMODITY_INFO")
        COMMODITY_PRICE = request.args.get("COMMODITY_PRICE")
        COMMODITY_PICTURE = request.args.get("COMMODITY_PICTURE")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        USER_ID = json_data.get("USER_ID")
        COMMODITY_NAME = json_data.get("COMMODITY_NAME")
        COMMODITY_INFO = json_data.get("COMMODITY_INFO")
        COMMODITY_PRICE = json_data.get("COMMODITY_PRICE")
        COMMODITY_PICTURE = json_data.get("COMMODITY_PICTURE")
    import time
    import pymysql   #引入pymysql库
    # 创建数据库连接
    config = {           # 连接用的字典结构
        'host': '139.196.203.66',     # 服务器ip
        'port': 3306,       # mysql端口号
        'user': 'root',        # mysql登录账号
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',       # 密码
        'db': 'CAMPUS_TRANSACTION_SQL',       # 数据库名字
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config)   # 对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    # 执行查询，并返回受影响的行数
    ticks = time.strftime("%Y%m%d%H%M%S",time.localtime())
#     print(ticks)
    nr ={"COMMODITY_ID":ticks,
         "USER_ID":USER_ID,
         "COMMODITY_NAME":COMMODITY_NAME,
         "COMMODITY_INFO":COMMODITY_INFO,
         "COMMODITY_PRICE":COMMODITY_PRICE,
         "COMMODITY_PICTRUE":COMMODITY_PICTURE,
         "IS_PUTAWAY":"On_the_shelf"}
    sql_L_G="INSERT INTO COMMODITY (COMMODITY_ID,USER_ID,COMMODITY_NAME,COMMODITY_INFO,COMMODITY_PRICE,COMMODITY_PICTRUE,IS_PUTAWAY) VALUES ('{COMMODITY_ID}','{USER_ID}','{COMMODITY_NAME}','{COMMODITY_INFO}',{COMMODITY_PRICE},'{COMMODITY_PICTRUE}','{IS_PUTAWAY}')".format(**nr)
#     print(sql_L_G)
    L_G = cursor.execute(sql_L_G) # L_G  Listing goods  上架商品
    if L_G>0:
#         cursor.execute(sql_L_G)
        db.commit()
        result = cursor.fetchall()  # 返回所有的结果集
#         Traverse_to_find_product_results(result)
        db.close()
        return "OK"
    else:       # 操作失败，返回 None
        print('上架失败！')
        db.close()
        return "ERROR"

@app.route('/O_T_S_G/', methods=[ 'POST','GET'])
def Off_the_shelf_goods():   # Off_the_shelf_goods = 下架商品        COMMODITY_ID = 商品ID
    if request.method == 'GET':
        COMMODITY_ID = request.args.get("COMMODITY_ID")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        COMMODITY_ID = json_data.get("COMMODITY_ID")
    import pymysql   #引入pymysql库
    # 创建数据库连接
    config = {           # 连接用的字典结构
        'host': '139.196.203.66',     # 服务器ip
        'port': 3306,       # mysql端口号
        'user': 'root',        # mysql登录账号
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',       # 密码
        'db': 'CAMPUS_TRANSACTION_SQL',       # 数据库名字
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config)   # 对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    # 执行查询，并返回受影响的行数
    sql_O_T_S_G = "update COMMODITY set IS_PUTAWAY='Under_the_shelf' where COMMODITY_ID='{}' and IS_PUTAWAY='On_the_shelf'".format(COMMODITY_ID)   # sql语句，通过格式化对{}内容输入变量
#     print(sql_O_T_S_G)   # sql_O_T_S_G = O_T_S_G   Off the shelf goods 下架商品
    O_T_S_G = cursor.execute(sql_O_T_S_G)   # O_T_S_G = Off the shelf goods 下架商品
#     print(O_T_S_G)
    if O_T_S_G>0:    # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        O_T_S_G = cursor.execute(sql_O_T_S_G)
        db.commit()
#         result = cursor.fetchall()  # 返回所有的结果集
#         print(result)
#         Traverse_to_find_product_results(result)
        db.close()
        return "OK"
    else:       # 操作失败，返回 False
#         result = cursor.fetchall()  # 返回所有的结果集
#         print(result)
#         Traverse_to_find_product_results(result)
        db.close()
        return "ERROR"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6178,
            ssl_context = 'adhoc'
            # ssl_context=('/root/Campus_Transaction/script/python/cert/3853291_campustransaction.xyz.pem','/root/Campus_Transaction/script/python/cert/33853291_campustransaction.xyz.key')
           )