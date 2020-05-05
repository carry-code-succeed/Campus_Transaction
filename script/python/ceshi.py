# -*- coding: UTF-8 -*-
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=[ 'POST','GET'])
def b():
    bbb = request.args.get("bbb")
    return bbb


@app.route('/A/', methods=[ 'POST','GET'])
def a():
    aaa = request.args.get("aaa")
    return aaa

if __name__ == '__main__':
    app.run(host='172.19.6.224', port=6178,
#             ssl_context='adhoc'
           )