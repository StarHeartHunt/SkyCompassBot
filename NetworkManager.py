import requests
import json
import time

def get_meta(config):
    resp = requests.get(config.meta_url, headers=config.get_header())
    print(resp.text)
    
    try:
       code = resp.json()["status"]["code"]
    except KeyError:
       code = ""
    
    if code == 1008:
        refresh_token(config)
    else:
        config.auth_key = resp.headers.get("authorization")
        config.res_ver = resp.headers.get("x-res-ver")
        config.export_config()
    
def refresh_token(config):
    refresh_body = {
        "grant_type":"refresh_token",
        "refresh_token":config.refresh_key,
        "client_id":config.client_id
    }
    
    resp = requests.post(config.token_url, headers=config.get_post_header(), data=json.dumps(refresh_body))
    config.auth_key = resp.headers.get("authorization")
    config.refresh_key = json.loads(resp.text)["refresh_token"]
    config.export_config()
    print(resp.text)
    
def get_weekly_schedule(config):
    month = time.strftime("%Y%m")
    params = {
        "month": month,
        "group_by": "week"
    }
    
    resp = requests.get(config.schedules_url, headers=config.get_header(), params=params)
    
    with open("./data/%s.json" % month, "w") as f:
        json.dump(json.loads(resp.text), f, ensure_ascii=False)
    
    print("数据已保存在/data/%s.json中" % month)