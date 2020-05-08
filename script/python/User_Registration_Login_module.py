#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re 
import os
import json
import hashlib
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/U_R/', methods=[ 'POST','GET'])
#注册
def User_Registration():
    if request.method == "GET":
        user_id = request.args.get("user_id")#账号
        user_name = request.args.get("user_name")#用户名
        student_id = request.args.get("student_id")#学号
        student_name = request.args.get("student_name")#姓名
        user_password = request.args.get("user_password")#密码（数字字母下划线6-12位）
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        user_id = json_data.get("user_id")
        user_name = json_data.get("user_name")
        student_id = json_data.get("student_id")
        student_name = json_data.get("student_name")
        user_password = json_data.get("user_password")
    # 创建数据库连接
    import pymysql
    config = {           # 连接用的字典结构
        'host': '139.196.203.66',     # 服务器ip
        'port': 3306,       # mysql端口号
        'user': 'root',        # mysql登录账号
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',       # 密码
        'db': 'CAMPUS_TRANSACTION_SQL',       # 数据库名字
        'charset': 'utf8mb4'
    }
    db = pymysql.connect(**config)
    # 创建游标
    cursor = db.cursor()
    md5 = hashlib.md5()
   
    # 1.用正则检验用户输入是否合法
    if (len(user_id.strip())==0):
        print('账号不能为空！')
        return 'ERROR'
    elif(len(user_name.strip())==0):
        print('用户名不能为空！')
        return 'ERROR'
    elif(len(student_id.strip())==0):
        print('学号不能为空！')
        return "ERROR"
    elif(len(student_name.strip())==0):
        print('姓名不能为空！')
        return "ERROR"
    elif not(re.match('\w{6,12}$', user_password)):
        print('请输入正确的密码（6-12位）！')
        return "ERROR"
    # 2.查询数据库中账号和用户名是否已经被注册
    sql_userid = 'select USER_ID from USER_INFO where USER_ID = "{}"'.format(user_id)
    cursor.execute(sql_userid)
    if cursor.rowcount:
        print('该账号已注册！')
        return "ERROR"
    
    sql_username = 'select USER_NAME from USER_INFO where USER_ID = "{}"'.format(user_name)
    cursor.execute(sql_username)
    if cursor.rowcount:
        print('该用户名已注册！')
        return "ERROR"
    #3.验证学号是否存在
    cursor.execute('select STUDENT_ID from STUDENT')
    result = cursor.fetchall()
    student_ids=[]#创建student_ids数组储存所有的学号
    for i in result:
        student_ids.append(i[0])
    if student_id not in student_ids:
        print('请输入正确的学号！')
        return "ERROR"
    #4.验证学号和姓名是否已经被注册以及是否匹配
    cursor.execute('select STUDENT_NAME,IS_REGISTER from STUDENT where STUDENT_ID= "{}"'.format(student_id))
    result = cursor.fetchone()
    if not result[1] is None:
        print('该学号已注册！')
        return "ERROR"
    elif result[0] != student_name:
        print('请输入正确学号或者姓名！')
        return "ERROR"
    # md5加密
    md5.update(user_password.encode('utf8'))
    password = md5.hexdigest()
    try:
        sql_user_info = 'insert into USER_INFO (USER_ID,USER_NAME,STUDENT_ID,USER_PASSWORD) values ("{}","{}","{}","{}")'.format(user_id, user_name,student_id,user_password)
        cursor.execute(sql_user_info)
        db.commit()
        sql_student = 'update STUDENT set IS_REGISTER= "{}" where STUDENT_ID="{}"'.format(user_id,student_id)
        cursor.execute(sql_student)
        db.commit()
        print("注册成功")
        return "OK"
    except:
        print('注册失败！')
        return "ERROR"
    finally:
        # 关闭游标
        db.close()
        
@app.route('/U_L/', methods=[ 'POST','GET'])
#登录
def User_Login():
    if request.method == "GET":
        user_id = request.args.get("user_id")#账号
        user_password = request.args.get("user_password")#密码
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        user_id = json_data.get("user_id")
        user_password = json_data.get("user_password")
    
    import pymysql
    config = {           # 连接用的字典结构
        'host': '139.196.203.66',     # 服务器ip
        'port': 3306,       # mysql端口号
        'user': 'root',        # mysql登录账号
        'passwd': '%E7%A0%81%E5%88%B0%E6%88%90%E5%8A%9F',       # 密码
        'db': 'CAMPUS_TRANSACTION_SQL',       # 数据库名字
        'charset': 'utf8mb4'
    }

    db = pymysql.connect(**config)

    # 创建游标
    cursor = db.cursor()

    if (len(user_id.strip())==0):
        print('账号不能为空！')
        return "ERROR"
    elif not(re.match('\w{6,12}$', user_password)):
        print('请输入正确的密码（6-12位）！')
        return "ERROR"
    sql = 'select USER_ID,USER_PASSWORD from USER_INFO where USER_ID = "{}"'.format(user_id)
    cursor.execute(sql)
    if not cursor.rowcount:
        print("用户不存在")
        return "ERROR"

    if cursor.fetchone()[1] != user_password :
        print("请输入正确的密码")
        return "ERROR"
    print("登陆成功")
    return "OK"
    

@app.route('/M_I/', methods=[ 'POST','GET'])
#修改信息
def Modify_Informaion():
    if request.method == "GET":
        user_id = request.args.get("user_id")#账号
        name = request.args.get("name")#要修改的名称
        info = request.args.get("info")#要修改的信息
    elif request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        user_id = json_data.get("user_id")
        name = json_data.get("name")
        info = json_data.get("info")
        
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
    sql = 'update USER_INFO set {}="{}" where USER_ID="{}"'.format(name,info,user_id)
    M_P = cursor.execute(sql)
    if M_P >0:
        M_P = cursor.execute(sql)
        db.commit()
        db.close()
        return "OK"
    else:
        db.close()
        return "ERROR"
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6166,
            ssl_context = 'adhoc'
            # ssl_context=('/root/Campus_Transaction/script/python/cert/3853291.pem','/root/Campus_Transaction/script/python/cert/33853291.key')
           )







