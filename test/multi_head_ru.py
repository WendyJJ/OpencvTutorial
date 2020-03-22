import base64
import datetime
import hashlib
import json

import pytz
import requests

clients_name = "creditech"
clients_password = "ABCDE12345abcde12345abcde12345ab"
timestamp = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y%m%d%H%M")
auth_value = hashlib.md5((clients_name + clients_password + timestamp).encode()).hexdigest()
headers_info = {"timestamp": timestamp, "sign_info": auth_value,
               "c_name": clients_name, "Content-Type": "application/json;charset=utf-8"}

# print("timestamp==", timestamp)
# print("auth_value==", auth_value)


# 生产环境：https://in.creditech.biz/multi_head/
# 测试环境： https://preapi.creditech.biz/multi_head/

Post_data = {"uid":"1234567890","callbackURL": ""}

url = "https://in.creditech.biz/multi_head/return/"
aa = requests.post(url,json=Post_data,headers=headers_info,verify=False).text
print(aa,9999999999)



