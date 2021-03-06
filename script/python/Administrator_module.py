# -*- coding: UTF-8 -*-
import os
import json
import hashlib
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/Q_B_C_N/', methods=[ 'POST','GET'])
def Find_item():   # Find_item = 查找商品        NameOrId = 商品名字或商品ID
    if request.method == "GET":
        NameOrId = request.args.get("NameOrId")
    else:
        # NameOrId = request.form.get_data("NameOrId")
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        NameOrId = json_data.get("NameOrId")
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
    sql_Q_B_C_N = "select * from COMMODITY where COMMODITY_NAME='{}' and IS_PUTAWAY='On_the_shelf'".format(NameOrId)   # sql_Q_B_C_N = Q_B_C_N  Query by commodity name  通过商品ID查询,sql语句，通过格式化对{}内容输入变量
    sql_Q_B_C_I = "select * from COMMODITY where COMMODITY_ID='{}' and IS_PUTAWAY='On_the_shelf'".format(NameOrId)   # sql_Q_B_C_I = Q_B_C_N  Query by commodity name  通过商品ID查询,sql语句，通过格式化对{}内容输入变量
    Q_B_C_N = cursor.execute(sql_Q_B_C_N) # Q_B_C_N  Query by commodity name  通过商品ID查询
    Q_B_C_I = cursor.execute(sql_Q_B_C_I) # Q_B_C_N  Query by commodity name  通过商品ID查询
    if Q_B_C_N>0:
        cursor.execute(sql_Q_B_C_N)
        result = cursor.fetchall()  # 返回所有的结果集
        para = []
        for i in result:
            text = {'COMMODITY_ID': i[0], 'USER_ID': i[1], 'COMMODITY_NAME': i[2], 'COMMODITY_INFO': i[3],
                    'COMMODITY_PRICE': i[4], 'COMMODITY_PICTURE': i[5], 'IS_PUTAWAY': i[6]}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    elif Q_B_C_I>0:
        cursor.execute(sql_Q_B_C_I)
        result = cursor.fetchall()  # 返回所有的结果集
        para = []
        for i in result:
            text = {'COMMODITY_ID':i[0],'USER_ID':i[1],'COMMODITY_NAME':i[2],'COMMODITY_INFO':i[3],
                    'COMMODITY_PRICE':i[4],'COMMODITY_PICTURE':i[5],'IS_PUTAWAY':i[6]}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:       # 操作失败，返回 None
        print('没找到商品！')
        db.close()
        para = []
        text = {'result':'没找到商品！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)

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
    sql_O_T_S_G = "update COMMODITY set IS_PUTAWAY='Admin_dismounts' where COMMODITY_ID='{}' and IS_PUTAWAY='On_the_shelf'".format(COMMODITY_ID)   # sql语句，通过格式化对{}内容输入变量
    O_T_S_G = cursor.execute(sql_O_T_S_G)   # O_T_S_G = Off the shelf goods 下架商品
    if O_T_S_G>0:    # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        O_T_S_G = cursor.execute(sql_O_T_S_G)
        db.commit()
        db.close()
        text = {'result':'成功！'}
        para = []
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:       # 操作失败，返回 False
        db.close()
        para = []
        text = {'result':'下架商品失败！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)

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
    sql_D_U_P_R = "delete from COMMODITY where USER_ID='{}'".format(USER_ID) # sql_D_U_P_R = D_U_P_R Delete user product really 真删除用户商品
    print(sql_L_O_U_A_1)
    print(sql_L_O_U_A_2)
    print(sql_D_U_P_R)
    L_O_U_A_1 = cursor.execute(sql_L_O_U_A_1)  # 在用户信息表中删除用户账号
    L_O_U_A_2 = cursor.execute(sql_L_O_U_A_2)  # 在学生表中删除用户账号
    D_U_P_R = cursor.execute(sql_D_U_P_R)  # 在学生表中真删除用户商品
    print(L_O_U_A_1)
    print(L_O_U_A_2)
    print(D_U_P_R)
    if L_O_U_A_1>0 and L_O_U_A_2>0:     # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        L_O_U_A_1 = cursor.execute(sql_L_O_U_A_1)
        db.commit()
        L_O_U_A_2 = cursor.execute(sql_L_O_U_A_2)
        db.commit()
        D_U_P_R = cursor.execute(sql_D_U_P_R)
        db.commit()
        db.close()
        if (D_U_P_R > 0):
            para = []
            text = {'result':'成功！'}
            para.append(text)
            text = {'result':'删除商品成功！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
        else:
            para = []
            text = {'result': '成功！'}
            para.append(text)
            text = {'result': '删除商品失败！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
    else:
        para = []
        if L_O_U_A_1 == 0:       # 操作失败
            text = {'result':'在用户信息表中删除用户账号失败！'}
            para.append(text)
        elif L_O_U_A_2 == 0:
            text = {'result': '在学生表中删除用户账号失败！'}
            para.append(text)
        elif L_O_U_A_2 == 0:
            text = {'result': '在学生表中真删除用户商品失败！'}
            para.append(text)
        db.close()
        return json.dumps(para, ensure_ascii=False, indent=4)

@app.route('/M_U_I/', methods=[ 'POST','GET'])
def Modify_user_information():   # Modify_user_information = 修改用户信息  USER_ID = 用户ID    Information_name = 信息名称    Information_content = 信息内容
    if request.method == 'GET':
        USER_ID = request.args.get("USER_ID")
        USER_NAME = request.args.get("USER_NAME")
        USER_PICTRUE = request.args.get("USER_PICTRUE")
        QQ_NUMBER = request.args.get("QQ_NUMBER")
        TELEPHONE = request.args.get("TELEPHONE")
        SPECIALILZED_SUBJECT = request.args.get("SPECIALILZED_SUBJECT")
        GRADE = request.args.get("GRADE")
        SEX = request.args.get("SEX")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        USER_ID = json_data.get("USER_ID")
        USER_NAME = json_data.get("USER_NAME")
        USER_PICTRUE = json_data.get("USER_PICTRUE")
        QQ_NUMBER = json_data.get("QQ_NUMBER")
        TELEPHONE = json_data.get("TELEPHONE")
        SPECIALILZED_SUBJECT = json_data.get("SPECIALILZED_SUBJECT")
        GRADE = json_data.get("GRADE")
        SEX = json_data.get("SEX")
    if GRADE == '':
        GRADE = 0
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
    sql_U_N = "update USER_INFO set USER_NAME='{}' where USER_ID='{}'".format(USER_NAME,USER_ID)   # sql语句，通过格式化对{}内容输入变量
    sql_U_PIC = "update USER_INFO set USER_PICTRUE='{}' where USER_ID='{}'".format(USER_PICTRUE, USER_ID)
    sql_Q_N = "update USER_INFO set QQ_NUMBER='{}' where USER_ID='{}'".format(QQ_NUMBER, USER_ID)
    sql_T = "update USER_INFO set TELEPHONE='{}' where USER_ID='{}'".format(TELEPHONE, USER_ID)
    sql_S_S = "update USER_INFO set SPECIALILZED_SUBJECT='{}' where USER_ID='{}'".format(SPECIALILZED_SUBJECT, USER_ID)
    sql_G = "update USER_INFO set GRADE={} where USER_ID='{}'".format(GRADE, USER_ID)
    sql_S = "update USER_INFO set SEX='{}' where USER_ID='{}'".format(SEX, USER_ID)
    U_N = cursor.execute(sql_U_N)
    db.commit()
    U_PIC = cursor.execute(sql_U_PIC)
    db.commit()
    Q_N = cursor.execute(sql_Q_N)
    db.commit()
    T = cursor.execute(sql_T)
    db.commit()
    S_S = cursor.execute(sql_S_S)
    db.commit()
    G = cursor.execute(sql_G)
    db.commit()
    S = cursor.execute(sql_S)
    db.commit()
    if U_N>0 or U_PIC>0 or Q_N>0 or T>0 or S_S>0 or G>0 or S>0:   # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        db.close()
        para = []
        text = {'result':'成功！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)
    else:       # 操作失败，返回 False
        db.close()
        para = []
        text = {'result':'修改用户信息失败！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)

@app.route('/C_P/', methods=[ 'POST','GET'])
def Change_Password():   # Change_Password = 修改密码
    if request.method == 'GET':
        USER_ID = request.args.get("USER_ID")
        STUDENT_ID = request.args.get("STUDENT_ID")
        STUDENT_NAME = request.args.get("STUDENT_NAME")
        USER_PASSWORD = request.args.get("USER_PASSWORD")
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        USER_ID = json_data.get("USER_ID")
        STUDENT_ID = json_data.get("STUDENT_ID")
        STUDENT_NAME = json_data.get("STUDENT_NAME")
        USER_PASSWORD = json_data.get("USER_PASSWORD")
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
    md5 = hashlib.md5()
    md5.update(USER_PASSWORD.encode('utf8'))
    USER_PASSWORD = md5.hexdigest()
    sql_S_I = "select * from STUDENT where STUDENT_ID='{}'".format(STUDENT_ID)   # sql语句，通过格式化对{}内容输入变量
    sql_U_P = "update USER_INFO set USER_PASSWORD='{}' where USER_ID='{}'".format(USER_PASSWORD, USER_ID)
    S_I = cursor.execute(sql_S_I)
    result = cursor.fetchall()  # 返回所有的结果集
    if S_I>0:   # 如果操作数大于0，表示有对表进行修改，表示sql语句执行成功
        if result[0][1] == STUDENT_NAME:
            U_P = cursor.execute(sql_U_P)
            db.commit()
            if U_P > 0:
                db.close()
                para = []
                text = {'result':'成功！'}
                para.append(text)
                return json.dumps(para, ensure_ascii=False, indent=4)
            else:
                db.close()
                para = []
                text = {'result': '修改用户密码失败！'}
                para.append(text)
                return json.dumps(para, ensure_ascii=False, indent=4)
        else:
            db.close()
            para = []
            text = {'result': '学号验证失败！'}
            para.append(text)
            return json.dumps(para, ensure_ascii=False, indent=4)
    else:       # 操作失败，返回 False
        db.close()
        para = []
        text = {'result':'未找到学号信息！'}
        para.append(text)
        return json.dumps(para, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6178,ssl_context = 'adhoc'
           )