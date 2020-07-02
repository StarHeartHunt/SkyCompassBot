from flask import Flask
from flask import request
from flask import make_response
from history import *
import os
import time

app=Flask(__name__)

@app.route("/current", methods=['post','get'])
def current():
    dir_res = '../data/'
    curr_month = time.strftime("%Y%m")
    
    with open(dir_res + curr_month + ".json", "r") as f:
        text = f.read()
    rst = make_response(text)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    
    return rst, 200
    
@app.route("/history", methods=['post','get'])
def history():
    month = request.args.get('month')
    print(month)
    if month != None:
        resp = get_weekly_schedule_history(month)
        rst = make_response(resp)
        rst.headers['Access-Control-Allow-Origin'] = '*'
        
        return rst, 200
    else:
        return "parameter month cannot be empty!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4544, debug=True)