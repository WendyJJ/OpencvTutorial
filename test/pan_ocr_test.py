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

with open(r"D:\MyAPP\ocr_img_cut\ocr_img_after\1024_7955097_pan.jpg", 'rb') as image:
    img2= base64.b64encode(image.read()).decode()



app_id = "test_temp-DT2N0-89KG7PK-YAYC0XE"
app_key = "3H3RV-HqSV-1FPzJj5-M4O19r"
post_data = {"app_id":app_id,
"par1":"ocr and verification",
"app_key":app_key,
"uid":"9999999998",
"imei_code":"1234567890",
"par2": "",  #"http://139.159.210.162:5001/callback/",
"img1":img2}


url='http://ai.creditech.biz/pan_img/'
# url = 'http://testdb.creditech.biz/pan_img/'
aa = requests.post(url,json=post_data,headers=headers_info,verify=False).text
print(aa,9999999999)
print(json.loads(aa).get("data"))


