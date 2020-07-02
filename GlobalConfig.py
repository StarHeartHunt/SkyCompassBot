import json
import requests
import re

class GlobalConfig:
    def __init__(self):
        with open("./config/app_config.json", "r") as f:
            app_config = json.load(f)
           
        with open("./config/network_config.json", "r") as f1:
            network_config = json.load(f1)
       
        self.auth_key = app_config["auth_key"]
        self.res_ver = app_config["res_ver"]
        self.client_id = app_config["client_id"]
        self.refresh_key = app_config["refresh_key"]
        self.meta_url = network_config["meta"]
        self.token_url = network_config["token"]
        self.schedules_url = network_config["schedules"]
        self.app_ver = GlobalConfig.get_app_version()
    
    def get_header(self):
        header = {
            "Host": "api.skycompass.io", 
            "authorization": self.auth_key, 
            "x-device": "2", 
            "x-app-ver": self.app_ver, 
            "x-res-ver": self.res_ver, 
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
        return header
    
    def get_post_header(self):
        post_header = {
            "Host": "api.skycompass.io", 
            "authorization": self.auth_key, 
            "x-device": "2", 
            "x-app-ver": self.app_ver, 
            "x-res-ver": self.res_ver, 
            "x-device-id": "02:00:00:00:00:00", 
            "x-device-name": "ONE A2001", 
            "x-ip-address": "192.168.0.101", 
            "x-platform-os-version": "Android 9", 
            "x-platform": "2", 
            "x-language": "zh", 
            "x-region-code": "CN", 
            "accept-encoding": "gzip", 
            "user-agent": "okhttp/3.12.0",
            "Content-Type":"application/json"
        }
        return post_header
    
    def get_app_version():
        url = "https://apps.qoo-app.com/app/5038"
        resp = requests.get(url)
        regex = "\<cite\>版本：\<\/cite\>\<var\>(.*)\<\/var\>"

        version = re.search(regex, resp.text).group(1)
        return version
        
    def export_config(self):
        app_config = {}
        app_config["auth_key"] = self.auth_key
        app_config["res_ver"] = self.res_ver
        app_config["refresh_key"] = self.refresh_key
        app_config["client_id"] = self.client_id
        app_config["app_ver"] = self.app_ver
        
        with open("./config/app_config.json", "w") as f:
            json.dump(app_config, f, ensure_ascii=False, indent=4)