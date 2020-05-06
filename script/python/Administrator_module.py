# -*- coding: UTF-8 -*-
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

# @app.route('/Q_B_C_N/', methods=[ 'POST','GET'])
# def Find_item():   # Find_item = 查找商品        NameOrId = 商品名字或商品ID
#     if request.method == "GET":
#         NameOrId = request.args.get("NameOrId")
#     else:
#         NameOrId = request.form.get_data("NameOrId")
#     import pymysql   #引入pymysql库
#     # 创建数据库连接
#     config = {           # 连接用的字典结构
#         'host': '139.196.203.66',     # 服务器ip
#         'port': 3306,       # mysql端口号
#         'user': 'root',        # mysql登录账号
#         'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',       # 密码
#         'db': 'CAMPUS_TRANSACTION_SQL',       # 数据库名字
#         'charset': 'utf8mb4'
#     }
#     db = pymysql.connect(**config)   # 对mysql进行连接
#     # 初始化游标（创建游标）
#     cursor = db.cursor()
#     # 执行查询，并返回受影响的行数
#     sql_Q_B_C_N = "select * from COMMODITY where COMMODITY_NAME='{}' and IS_PUTAWAY='sjz'".format(NameOrId)   # sql_Q_B_C_N = Q_B_C_N  Query by commodity name  通过商品ID查询,sql语句，通过格式化对{}内容输入变量
# #     print('sql_Q_B_C_N',sql_Q_B_C_N)
#     sql_Q_B_C_I = "select * from COMMODITY where COMMODITY_ID='{}' and IS_PUTAWAY='sjz'".format(NameOrId)   # sql_Q_B_C_I = Q_B_C_N  Query by commodity name  通过商品ID查询,sql语句，通过格式化对{}内容输入变量
# #     print('sql_Q_B_C_I',sql_Q_B_C_I)
#     Q_B_C_N = cursor.execute(sql_Q_B_C_N) # Q_B_C_N  Query by commodity name  通过商品ID查询
#     Q_B_C_I = cursor.execute(sql_Q_B_C_I) # Q_B_C_N  Query by commodity name  通过商品ID查询
#     if Q_B_C_N>0:
#         cursor.execute(sql_Q_B_C_N)
#         result = cursor.fetchall()  # 返回所有的结果集
# #         Traverse_to_find_product_results(result)
#         para = []
#         for i in result:
#             text = {'id':i[0],'name':i[1],'password':i[2],'IS_PUTAWAY':i[6]}
#             para.append(text)
#         db.close()
#         return json.dumps(para, ensure_ascii=False, indent=4)
#     elif Q_B_C_I>0:
#         cursor.execute(sql_Q_B_C_I)
#         result = cursor.fetchall()  # 返回所有的结果集
# #         Traverse_to_find_product_results(result)
#         para = []
#         for i in result:
#             text = {'id':i[0],'name':i[1],'password':i[2],'IS_PUTAWAY':i[6]}
#             para.append(text)
#         db.close()
#         return json.dumps(para, ensure_ascii=False, indent=4)
#     else:       # 操作失败，返回 None
#         print('没找到商品！')
#         db.close()
#         return "NONE"

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
    sql_O_T_S_G = "update COMMODITY set IS_PUTAWAY='Administrator_dismounts' where COMMODITY_ID='{}' and IS_PUTAWAY='On_the_shelf'".format(COMMODITY_ID)   # sql语句，通过格式化对{}内容输入变量
    print(sql_O_T_S_G)   # sql_O_T_S_G = O_T_S_G   Off the shelf goods 下架商品
    O_T_S_G = cursor.execute(sql_O_T_S_G)   # O_T_S_G = Off the shelf goods 下架商品
    print(O_T_S_G)
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

@app.route('/M_U_I/', methods=[ 'POST','GET'])
def Modify_user_information():   # Modify_user_information = 修改用户信息  USER_ID = 用户ID    Information_name = 信息名称    information_content = 信息内容
    if request.method == 'GET':
        USER_ID = request.args.get("USER_ID")
        Information_name = request.args.get("Information_name")
        Information_content = request.args.get("Information_content")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        USER_ID = json_data.get("USER_ID")
        Information_name = json_data.get("Information_name")
        Information_content = json_data.get("Information_content")
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
    sql_M_U_I = "update USER_INFO set {}='{}' where USER_ID='{}'".format(Information_name,Information_content,USER_ID)   # sql语句，通过格式化对{}内容输入变量
    print(sql_M_U_I)
    M_U_I = cursor.execute(sql_M_U_I)
    print(M_U_I)
    if M_U_I>0:   # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        M_U_I = cursor.execute(sql_M_U_I)
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

@app.route('/L_O_U_A/', methods=[ 'POST','GET'])
def Log_off_user_account():   #Log_off_user_account = 注销用户账号  USER_ID = 用户ID
    if request.method == 'GET':
        USER_ID = request.args.get("USER_ID")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        USER_ID = json_data.get("USER_ID")
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
    sql_L_O_U_A_1 = "delete from USER_INFO where USER_ID='{}'".format(USER_ID) # sql_L_O_U_A_1 = L_O_U_A_1 Log off user account 注销用户账号
    sql_L_O_U_A_2 = "update STUDENT set IS_REGISTER=null where IS_REGISTER='{}'".format(USER_ID) # sql_L_O_U_A_2 = L_O_U_A_2 Log off user account 注销用户账号
    L_O_U_A_1 = cursor.execute(sql_L_O_U_A_1)  # 在用户信息表中删除用户账号
    L_O_U_A_2 = cursor.execute(sql_L_O_U_A_2)  # 在学生表中删除用户账号
    if L_O_U_A_1>0 and L_O_U_A_2>0:     # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        L_O_U_A_1 = cursor.execute(sql_L_O_U_A_1)
        db.commit()
        L_O_U_A_2 = cursor.execute(sql_L_O_U_A_2)
        db.commit()
        db.close()
        return "OK"
    else:       # 操作失败，返回 False
        db.close()
        return "ERROR"

if __name__ == '__main__':
    import os
    key_path = os.environ.get("")
    app.run(host='127.0.0.1', port=6178,
            ssl_context = 'adhoc'
            # ssl_context=('/root/Campus_Transaction/script/python/cert/3853291_campustransaction.xyz.pem','/root/Campus_Transaction/script/python/cert/33853291_campustransaction.xyz.key')
           )