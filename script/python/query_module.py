# -*- coding: UTF-8 -*-
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
import pymysql
import time
app = Flask(__name__)

#通过商品名查询
@app.route('/H_P_Q/', methods=[ 'POST','GET'])
def Home_page_query(): #首页查询--通过商品名进行查询
    if request.method == 'GET':
        Commodity_name = request.args.get("*Commodity_name")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        Commodity_name = json_data.get("*Commodity_name")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    if Commodity_name==():
        print(Commodity_name)
        print(1)
        print(type(Commodity_name))
        sql_Trade=cursor.execute("select * from COMMODITY")
        print(sql_Trade)
        if sql_Trade>0:
            para=[]
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集
            #Traverse_to_find_product_result(result)
            for i in result:
                text ={'COMMODITY_NAME':i[2],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
                para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
        else:
            print('没有找到商品')
            return None
    else:    
    #执行查询，并返回受影响的行数
        print(Commodity_name)
        print(2)
        print(type(Commodity_name))
        sql_Trade_name="select * from COMMODITY where COMMODITY_NAME='{}'".format(*Commodity_name) #通过商品名进行查询
        print(sql_Trade_name)
        Trade_name=cursor.execute(sql_Trade_name)
        if Trade_name>0:
            para=[]
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集
            #Traverse_to_find_product_result(result)
            for i in result:
                text ={'COMMODITY_NAME':i[2],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
                para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
        else:
            print('没有找到商品')
            return None


#通过商品ID进行查询
@app.route('/C_I_Q/', methods=[ 'POST','GET'])
def Commodity_id_query(): #通过商品ID进行查询
    if request.method == 'GET':
        Commodity_id = request.args.get("Commodity_id")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        Commodity_id = json_data.get("Commodity_id")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_id="select * from COMMODITY where  COMMODITY_ID='{}'".format(Commodity_id) #通过商品ID进行查询
    Trade_id=cursor.execute(sql_Trade_id)
    if Trade_id>0:
        para=[]
        #cursor.execute(sql_Trade_picture)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_id(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'USER_ID':i[1],'COMMODITY_NAME':i[2],'COMMODITY_INFO':i[3],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到商品')
        return "error"


#通过用户名进行查询
@app.route('/U_N_Q/', methods=[ 'POST','GET'])
def User_name_query(): #通过用户ID进行查询
    if request.method == 'GET':
        User_id = request.args.get("User_id")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        User_id = json_data.get("User_id")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_id="select * from COMMODITY where USER_ID='{}'".format(User_id) #通过用户ID进行查询
    id=cursor.execute(sql_id)
    if id>0:
        para=[]
        #cursor.execute(sql_Trade_picture)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_username(result)
        for i in result:
            text ={'USER_ID':i[1],'COMMODITY_NAME':i[2],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到商品')
        return "error"


#通过商品名查询，对时间进行排序
@app.route('/H_P_Q_C/', methods=[ 'POST','GET'])
def Home_page_query_commodityname(): #首页查询--通过商品名进行查询-进行升降序
    if request.method == 'GET':
        Commodity_name = request.args.get("Commodity_name")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        Commodity_name = json_data.get("Commodity_name")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_name="select * from COMMODITY where COMMODITY_NAME ='{}' order by COMMODITY_ID desc".format(Commodity_name) #通过商品名进行查询
    Trade_name=cursor.execute(sql_Trade_name)
    if Trade_name>0:
        para=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_time(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'COMMODITY_NAME':i[2],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到商品')
        return "error"


#通过商品名查询，对价格进行排序
@app.route('/H_P_Q_P/', methods=[ 'POST','GET'])
def Home_page_query_price(): #首页查询--通过商品名进行查询-进行降序
    if request.method == 'GET':
        Commodity_name = request.args.get("Commodity_name")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        Commodity_name = json_data.get("Commodity_name")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_name="select * from COMMODITY where COMMODITY_NAME ='{}' order by COMMODITY_PRICE desc".format(Commodity_name) #通过商品名进行查询
    Trade_name=cursor.execute(sql_Trade_name)
    if Trade_name>0:
        para=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_price(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'COMMODITY_NAME':i[2],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到商品')
        return "error"


#通过用户ID查询用户信息表
@app.route('/U_I_Q/', methods=[ 'POST','GET'])
def User_information_query(): #用户信息查询
    if request.method == 'GET':
        User_id = request.args.get("User_id")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        User_id = json_data.get("User_id")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_id="select * from USER_INFO where USER_ID ='{}'".format(User_id) #通过用户ID进行查询
    Trade_id=cursor.execute(sql_Trade_id)
    if Trade_id>0:
        para=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        #User_information_table_result(result)
        for i in result:
            text ={'USER_ID':i[0],'USER_NAME':i[1],'STUDENT_ID':i[2],'USER_PICTRUE':i[4]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户')
        return "error"


#对我的商品进行查询
@app.route('/A_P_Q/', methods=[ 'POST','GET'])
def All_product_query(): #个人全部商品查询
    if request.method == 'GET':
        User_id = request.args.get("User_id")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        User_id = json_data.get("User_id")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_id="select * from COMMODITY where USER_ID ='{}'".format(User_id) #通过用户ID进行查询
    Trade_id=cursor.execute(sql_Trade_id)
    if Trade_id>0:
        para=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_mycommodity(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'COMMODITY_NAME':i[2],'COMMODITY_INFO':i[3],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5],'IS_PUTAWAY':i[6]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户')
        return "error"


#对我的商品上架中进行查询
@app.route('/A_P_Q_O/', methods=[ 'POST','GET'])
def All_product_query_on(): #个人上架中的商品查询
    if request.method == 'GET':
        User_id = request.args.get("User_id")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        User_id = json_data.get("User_id")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_id="select * from COMMODITY where USER_ID ='{}' AND IS_PUTAWAY='On_the_shelf'".format(User_id) #通过用户ID进行查询
    Trade_id=cursor.execute(sql_Trade_id)
    if Trade_id>0:
        para=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_on(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'COMMODITY_NAME':i[2],'COMMODITY_INFO':i[3],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5],'IS_PUTAWAY':i[6]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户')
        return "error"


#对我的商品下架中进行查询
@app.route('/A_P_Q_U/', methods=[ 'POST','GET'])
def All_product_query_under(): #个人下架中的商品查询
    if request.method == 'GET':
        User_id = request.args.get("User_id")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        User_id = json_data.get("User_id")
    # 创建数据库连接
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_id="select * from COMMODITY where USER_ID ='{}' AND IS_PUTAWAY='Under_the_shelf'".format(User_id) #通过用户ID进行查询
    Trade_id=cursor.execute(sql_Trade_id)
    if Trade_id>0:
        para=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_under(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'COMMODITY_NAME':i[2],'COMMODITY_INFO':i[3],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5],'IS_PUTAWAY':i[6]}
            para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户')
        return "error"


#通过商品名进行查询——具有页码，容量
def to_int(str):   #将字符串强制转化为整形的函数
#    if request.method == 'GET':                               
#        str = request.args.get("str")
#    elif request.method == 'POST':
#        data = request.get_data()
#        json_data = json.loads(data.decode('utf-8'))
#        str = json_data.get("str")
    try:
        int(str)
        return int(str)
    except ValueError: #报类型错误，说明不是整型的
        try:
            float(str) #用这个来验证，是不是浮点字符串
            return int(float(str))
        except ValueError:  #如果报错，说明即不是浮点，也不是int字符串。   是一个真正的字符串
            return False

@app.route('/H_P_Q_P_C/', methods=[ 'POST','GET'])
def Home_page_query_pag_cap(): #首页查询--通过商品名进行查询
    if request.method == 'GET':                               #pagination页码       capacity容量
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
        Commodity_name = request.args.get("Commodity_name")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
        Commodity_name = request.args.get("Commodity_name")
    # 创建数据库连接                                  
    config = {
        'host': '139.196.203.66',
        'port': 3306,
        'user': 'root',
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',
        'db': 'CAMPUS_TRANSACTION_SQL',
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config) #对mysql进行连接
    # 初始化游标（创建游标）
    cursor = db.cursor()
    #执行查询，并返回受影响的行数
    sql_Trade_name="select * from COMMODITY where COMMODITY_NAME='{}'".format(Commodity_name) #通过商品名进行查询
    Trade_name=cursor.execute(sql_Trade_name)
    pagination=to_int(pagination) #将字符串转化为整形
    capacity=to_int(capacity)    #将字符串转化为整形
    if Trade_name>0:
        para = []
        a=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集       
        x=capacity*(pagination-1)+1
        #Traverse_to_find_product_result(result)
        for x in range(x,x+capacity):
            text ={'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
            para.append(text)
        Trade_name=str(Trade_name)
        a.append(Trade_name)
        pagination=str(pagination)
        return json.dumps(a, ensure_ascii=False, indent=4),json.dumps(para, ensure_ascii=False, indent=4)
        
    else:
        print('没有找到商品')
        return "error"


if __name__ == '__main__':
#     import os
#     key_path = os.environ.get("")
    app.run(host='127.0.0.1', port=6184,
            ssl_context = 'adhoc'
            # ssl_context=('/root/Campus_Transaction/script/python/cert/3853291_campustransaction.xyz.pem','/root/Campus_Transaction/script/python/cert/33853291_campustransaction.xyz.key')
           )