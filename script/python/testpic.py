# -*- coding: UTF-8 -*-
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)

@app.route('/S_P/', methods=[ 'POST'])
def save_picture(): 
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        json_data = json.loads(data.decode('utf-8'))
        print(json_data)
        name = json_data.get("name")
        return "OK"
    else:
        return "ERROR"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6178,
            ssl_context = 'adhoc'
           )