import requests
import json

def get_weekly_schedule_history(month):
    with open("../config/app_config.json", "r") as f:
        app_config = json.load(f)
    
    with open("../config/network_config.json", "r") as f1:
        network_config = json.load(f1)
    
    auth_key = app_config["auth_key"]
    res_ver = app_config["res_ver"]
    app_ver = app_config["app_ver"]
    header = {
    "Host": "api.skycompass.io", 
    "authorization": auth_key, 
    "x-device": "2", 
    "x-app-ver": app_ver, 
    "x-res-ver": res_ver, 
    "x-device-id": "02:00:00:00:00:00", 
    "x-device-name": "ONE A2001", 
    "x-ip-address": "192.168.0.101", 
    "x-platform-os-version": "Android 9", 
    "x-platform": "2", 
    "x-language": "zh", 
    "x-region-code": "CN", 
    "accept-encoding": "gzip", 
    "user-agent": "okhttp/3.12.0"
    }
        
    url = network_config["schedules"]

    params = {
        "month": month,
        "group_by": "week"
    }
    
    resp = requests.get(url, headers=header, params=params)
    
    resp_json = json.dumps(json.loads(resp.text), ensure_ascii=False)
    
    return resp_json