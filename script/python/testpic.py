# -*- coding: UTF-8 -*-
import os
import json,random
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/S_P/', methods=[ 'POST','GET'])
def Save_picture():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))       #生成随机字符串，防止图片名字重复
    img = request.files.get('upload')     # 获取图片文件 name = upload
    path = "/root/CAMPUS_TRANSACTION/USER_PICTURE"       # 定义一个图片存放的位置 存放在static下面
    imgName = ran_str + img.filename                # 图片名称
    file_path = path + imgName            # 图片path和名称组成图片的保存路径
    img.save(file_path)                   # 保存图片
    url = path + imgName        # url是图片的路径
    return url

    # print('11111111111111111111111111')
    # if request.method == 'POST':
    #     print('22222222222222222222222')
    #     data = request.get_data()
    #     print(data)
    #     json_data = json.loads(data.decode('utf-8'))
    #     print(json_data)
    #     name = json_data.get("name")
    #     print(name)
    #     return "OK"
    # elif request.method == 'GET':
    #     print('3333333333333333333333333')
    # else:
    #     print('44444444444444444444444444')
    #     return "ERROR"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6178,
            ssl_context = 'adhoc'
           )