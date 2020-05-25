# -*- coding: UTF-8 -*-
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
import pymysql
import time
app = Flask(__name__)

#通过商品名查询
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


@app.route('/H_P_Q/', methods=[ 'POST','GET'])
def Home_page_query(): #首页查询--通过商品名进行查询
    if request.method == 'GET':
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
        Commodity_name = request.args.get("Commodity_name")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
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
    capacity=to_int(capacity)
    pagination=to_int(pagination)
    if Commodity_name=='':
        sql_Trade=cursor.execute("select * from COMMODITY where IS_PUTAWAY='On_the_shelf'")
        if sql_Trade>0:
            para = []
            data=[]
            if sql_Trade/capacity > int(sql_Trade/capacity):
                y = int(sql_Trade/capacity)+1
            else:
                y = int(sql_Trade / capacity)
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集        
            x=capacity*(pagination-1)+1
            #Traverse_to_find_product_result(result)
            text={'total':sql_Trade}
            data.append(text)
            text={'pagination':pagination}
            #data.append(sql_Trade)
            #data.append(pagination)
            data.append(text)
            if (capacity*pagination)>sql_Trade:
                if pagination==y:
                    for x in range(x,sql_Trade+1):
                        text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                        para.append(text)
            else:
                for x in range(x,x+capacity):
                    text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                    para.append(text) 
            data.append({'goods':para})
            db.close()
            # sql_Trade=str(sql_Trade)
            # pagination=str(pagination)
            return json.dumps(data, ensure_ascii=False, indent=4)
        else:
            print('没找到商品！')
            db.close()
            para = []
            text = {'result': '没找到商品！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
    else:    
    #执行查询，并返回受影响的行数
        sql_Trade_name="select * from COMMODITY where COMMODITY_NAME like '%{}%' and IS_PUTAWAY='On_the_shelf'".format(Commodity_name) #通过商品名进行查询
        Trade_name=cursor.execute(sql_Trade_name)
        if Trade_name>0:
            if sql_Trade / capacity > int(sql_Trade / capacity):
                z = int(sql_Trade / capacity) + 1
            else:
                z = int(sql_Trade / capacity)
            para = []
            data =[]
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集        
            x=capacity*(pagination-1)+1
            #Traverse_to_find_product_result(result)
            text={'total':Trade_name}
            data.append(text)
            text={'pagination':pagination}
            #data.append(Trade_name)
            #data.append(pagination)
            data.append(text)
            if (capacity*pagination)>Trade_name:
                if pagination==z:
                    for x in range(x,Trade_name+1):
                        text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                        para.append(text)
            else:
                for x in range(x,x+capacity):
                    text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                    para.append(text)
            data.append({'goods':para})
            db.close()
            Trade_name=str(Trade_name)        
            pagination=str(pagination)            
            return json.dumps(data, ensure_ascii=False, indent=4)
        else:
            print('没有找到商品')
            db.close()
            para = []
            text = {'result': '没找到商品！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)


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
    sql_Trade_id="select * from COMMODITY where  COMMODITY_ID='{}' and IS_PUTAWAY='On_the_shelf'".format(Commodity_id) #通过商品ID进行查询
    Trade_id=cursor.execute(sql_Trade_id)
    if Trade_id>0:
        para = []
        #cursor.execute(sql_Trade_picture)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_id(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'USER_ID':i[1],'COMMODITY_NAME':i[2],'COMMODITY_INFO':i[3],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没找到商品！')
        db.close()
        para = []
        text = {'result': '没找到商品！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


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
    sql_id="select * from COMMODITY where USER_ID='{}' and IS_PUTAWAY='On_the_shelf'".format(User_id) #通过用户ID进行查询
    id=cursor.execute(sql_id)
    if id>0:
        para=[]
        #cursor.execute(sql_Trade_picture)
        result=cursor.fetchall() #返回所有数据集
        #Traverse_to_find_product_result_username(result)
        for i in result:
            text ={'COMMODITY_ID':i[0],'USER_ID':i[1],'COMMODITY_NAME':i[2],'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5]}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没找到商品！')
        db.close()
        para = []
        text = {'result': '没找到商品！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


#通过商品名查询，对时间进行排序
@app.route('/H_P_Q_C/', methods=[ 'POST','GET'])
def Home_page_query_commodityname(): #首页查询--通过商品名进行查询-进行升降序
    if request.method == 'GET':
        Commodity_name = request.args.get("Commodity_name")
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        Commodity_name = json_data.get("Commodity_name")
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
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
    pagination = int(pagination)
    capacity = int(capacity)
    #执行查询，并返回受影响的行数
    # sql_Trade_name="select * from COMMODITY where COMMODITY_NAME like '%{}%' and IS_PUTAWAY='On_the_shelf' order by COMMODITY_ID desc".format(Commodity_name) #通过商品名进行查询
    # Trade_name=cursor.execute(sql_Trade_name)
    if Commodity_name=='':
        sql_Trade=cursor.execute("select * from COMMODITY where IS_PUTAWAY='On_the_shelf' order by COMMODITY_ID desc")
        if sql_Trade>0:
            para = []
            data=[]
            if sql_Trade / capacity > int(sql_Trade / capacity):
                y = int(sql_Trade / capacity) + 1
            else:
                y = int(sql_Trade / capacity)
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集
            x=capacity*(pagination-1)+1
            #Traverse_to_find_product_result(result)
            text={'total':sql_Trade}
            data.append(text)
            text={'pagination':pagination}
            #data.append(sql_Trade)
            #data.append(pagination)
            data.append(text)
            if (capacity*pagination)>sql_Trade:
                if pagination==y:
                    for x in range(x,sql_Trade+1):
                        text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                        para.append(text)
            else:
                for x in range(x,x+capacity):
                    text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                    para.append(text)
            data.append({'goods':para})
            db.close()
            # sql_Trade=str(sql_Trade)
            # pagination=str(pagination)
            return json.dumps(data, ensure_ascii=False, indent=4)
        else:
            print('没找到商品！')
            db.close()
            para = []
            text = {'result': '没找到商品！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
    else:
    #执行查询，并返回受影响的行数
        sql_Trade_name="select * from COMMODITY where COMMODITY_NAME like '%{}%' and IS_PUTAWAY='On_the_shelf' order by COMMODITY_ID desc".format(Commodity_name) #通过商品名进行查询
        Trade_name=cursor.execute(sql_Trade_name)
        if Trade_name>0:
            if sql_Trade / capacity > int(sql_Trade / capacity):
                z = int(sql_Trade / capacity) + 1
            else:
                z = int(sql_Trade / capacity)
            para = []
            data =[]
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集
            x=capacity*(pagination-1)+1
            #Traverse_to_find_product_result(result)
            text={'total':Trade_name}
            data.append(text)
            text={'pagination':pagination}
            #data.append(Trade_name)
            #data.append(pagination)
            data.append(text)
            if (capacity*pagination)>Trade_name:
                if pagination==z:
                    for x in range(x,Trade_name+1):
                        text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                        para.append(text)
            else:
                for x in range(x,x+capacity):
                    text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                    para.append(text)
            data.append({'goods':para})
            db.close()
            Trade_name=str(Trade_name)
            pagination=str(pagination)
            return json.dumps(data, ensure_ascii=False, indent=4)
        else:
            print('没有找到商品')
            db.close()
            para = []
            text = {'result': '没找到商品！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)


#通过商品名查询，对价格进行排序
@app.route('/H_P_Q_P/', methods=[ 'POST','GET'])
def Home_page_query_price(): #首页查询--通过商品名进行查询-进行降序
    if request.method == 'GET':
        Commodity_name = request.args.get("Commodity_name")
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        Commodity_name = json_data.get("Commodity_name")
        pagination=request.args.get("pagination")
        capacity=request.args.get("capacity")
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
    pagination = int(pagination)
    capacity = int(capacity)
    sql_Trade_name="select * from COMMODITY where COMMODITY_NAME like '%{}%' and IS_PUTAWAY='On_the_shelf' order by COMMODITY_PRICE desc".format(Commodity_name) #通过商品名进行查询
    Trade_name=cursor.execute(sql_Trade_name)
    if Commodity_name=='':
        sql_Trade=cursor.execute("select * from COMMODITY where IS_PUTAWAY='On_the_shelf' order by COMMODITY_PRICE desc")
        if sql_Trade>0:
            para = []
            data=[]
            if sql_Trade / capacity > int(sql_Trade / capacity):
                y = int(sql_Trade / capacity) + 1
            else:
                y = int(sql_Trade / capacity)
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集
            x=capacity*(pagination-1)+1
            #Traverse_to_find_product_result(result)
            text={'total':sql_Trade}
            data.append(text)
            text={'pagination':pagination}
            #data.append(sql_Trade)
            #data.append(pagination)
            data.append(text)
            if (capacity*pagination)>sql_Trade:
                if pagination==y:
                    for x in range(x,sql_Trade+1):
                        text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                        para.append(text)
            else:
                for x in range(x,x+capacity):
                    text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                    para.append(text)
            data.append({'goods':para})
            db.close()
            # sql_Trade=str(sql_Trade)
            # pagination=str(pagination)
            return json.dumps(data, ensure_ascii=False, indent=4)
        else:
            print('没找到商品！')
            db.close()
            para = []
            text = {'result': '没找到商品！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
    else:
    #执行查询，并返回受影响的行数
        sql_Trade_name="select * from COMMODITY where COMMODITY_NAME like '%{}%' and IS_PUTAWAY='On_the_shelf' order by COMMODITY_PRICE desc".format(Commodity_name) #通过商品名进行查询
        Trade_name=cursor.execute(sql_Trade_name)
        if Trade_name>0:
            if sql_Trade / capacity > int(sql_Trade / capacity):
                z = int(sql_Trade / capacity) + 1
            else:
                z = int(sql_Trade / capacity)
            para = []
            data =[]
            #cursor.execute(sql_Trade_name)
            result=cursor.fetchall() #返回所有数据集
            x=capacity*(pagination-1)+1
            #Traverse_to_find_product_result(result)
            text={'total':Trade_name}
            data.append(text)
            text={'pagination':pagination}
            #data.append(Trade_name)
            #data.append(pagination)
            data.append(text)
            if (capacity*pagination)>Trade_name:
                if pagination==z:
                    for x in range(x,Trade_name+1):
                        text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                        para.append(text)
            else:
                for x in range(x,x+capacity):
                    text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
                    para.append(text)
            data.append({'goods':para})
            db.close()
            Trade_name=str(Trade_name)
            pagination=str(pagination)
            return json.dumps(data, ensure_ascii=False, indent=4)
        else:
            print('没有找到商品')
            db.close()
            para = []
            text = {'result': '没找到商品！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)


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
        cursor.execute(sql_Trade_id)
        result=cursor.fetchall() #返回所有数据集
        for i in result:
            text ={'USER_ID':i[0],'USER_NAME':i[1],'STUDENT_ID':i[2],'USER_PASSWORD':i[3],'USER_PICTRUE':i[4],'QQ_NUMBER':i[5],'TELEPHONE':i[6],'SPECIALILZED_SUBJECT':i[7],'GRADE':i[8],'SEX':i[9]}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户！')
        db.close()
        para = []
        text = {'result': '没有找到此用户！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


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
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户！')
        db.close()
        para = []
        text = {'result': '没有找到此用户！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


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
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户！')
        db.close()
        para = []
        text = {'result': '没有找到此用户！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


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
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        print('没有找到此用户！')
        db.close()
        para = []
        text = {'result': '没有找到此用户！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


# #通过商品名进行查询——具有页码，容量
# def to_int(str):   #将字符串强制转化为整形的函数
# #    if request.method == 'GET':
# #        str = request.args.get("str")
# #    elif request.method == 'POST':
# #        data = request.get_data()
# #        json_data = json.loads(data.decode('utf-8'))
# #        str = json_data.get("str")
#     try:
#         int(str)
#         return int(str)
#     except ValueError: #报类型错误，说明不是整型的
#         try:
#             float(str) #用这个来验证，是不是浮点字符串
#             return int(float(str))
#         except ValueError:  #如果报错，说明即不是浮点，也不是int字符串。   是一个真正的字符串
#             return False

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
    sql_Trade_name="select * from COMMODITY where COMMODITY_NAME like '%{}%' and IS_PUTAWAY='On_the_shelf'".format(Commodity_name) #通过商品名进行查询
    Trade_name=cursor.execute(sql_Trade_name)
    pagination=to_int(pagination) #将字符串转化为整形
    capacity=to_int(capacity)    #将字符串转化为整形
    if Trade_name>0:
        para = []
        a=[]
        #cursor.execute(sql_Trade_name)
        result=cursor.fetchall() #返回所有数据集
        x=capacity*(pagination-1)+1
        Trade_name=str(Trade_name)
        pagination=str(pagination)
        para.append(Trade_name)
        para.append(pagination)
        #Traverse_to_find_product_result(result)
        for x in range(x,x+capacity):
            text ={'COMMODITY_ID':result[x-1][0],'COMMODITY_NAME':result[x-1][2],'COMMODITY_PRICE':result[x-1][4],'COMMODITY_PICTURE':result[x-1][5]}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)

    else:
        print('没有找到商品')
        db.close()
        para = []
        text = {'result': '没找到商品！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)


if __name__ == '__main__':
#     import os
#     key_path = os.environ.get("")
    app.run(host='127.0.0.1', port=6184,
            ssl_context = 'adhoc'
            # ssl_context=('/root/Campus_Transaction/script/python/cert/3853291_campustransaction.xyz.pem','/root/Campus_Transaction/script/python/cert/33853291_campustransaction.xyz.key')
           )