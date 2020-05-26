# -*- coding: UTF-8 -*-
import os
import json,random,string
from werkzeug.utils import secure_filename
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/S_P/', methods=[ 'POST','GET'])
def Save_picture():
    print('11111111111111111111111111')
    if request.method == 'POST':
        print('22222222222222222222222')
        # data = request.get_data()
        # print(data)
        # json_data = json.loads(data.decode('utf-8'))
        # print(json_data)
        # name = json_data.get("name")
        # print(name)
        # return "OK"
        #################################
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))  # 生成随机字符串，防止图片名字重复
        # img = request.files.get('upload')  # 获取图片文件 name = upload
        # path = "/root/CAMPUS_TRANSACTION/USER_PICTURE"  # 定义一个图片存放的位置 存放在static下面
        # imgName = ran_str + img.filename  # 图片名称
        # file_path = path + imgName  # 图片path和名称组成图片的保存路径
        # img.save(file_path)  # 保存图片
        # url = path + imgName  # url是图片的路径
        f = request.files['file']
        name = ran_str+f.filename
        upload_path = os.path.join('/home/CAMPUS_TRANSACTION/USER_PICTURE',
                                   secure_filename(name))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        upload_path = upload_path.replace('\\', '/')
        f.save(upload_path)
        print(upload_path)
        jieguo = upload_path
    elif request.method == 'GET':
        jieguo = "GET"
    else:
        jieguo = "ERROR"
    return jieguo

# @app.route('/D_P/', methods=[ 'POST','GET'])
# def Download_picture():
#     if request.method == "GET":
#         FileName = request.args.get("FileName")
#     elif request.method == 'POST':
#         data = request.get_data()
#         json_data = json.loads(data.decode('utf-8'))
#         FileName = json_data.get("FileName")
#
#         f = request.files['file']
#         name = ran_str+f.filename
#         upload_path = os.path.join('/root/CAMPUS_TRANSACTION/USER_PICTURE',
#                                    secure_filename(name))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
#         upload_path = upload_path.replace('\\', '/')
#         f.save(upload_path)
#         print(upload_path)
#         jieguo = upload_path
#
#     elif request.method == 'GET':
#         jieguo = "GET"
#         print('3333333333333333333333333')
#
#     else:
#         print('44444444444444444444444444')
#         jieguo = "ERROR"
#     return jieguo

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6109,
            ssl_context = 'adhoc'
           )