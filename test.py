#coding=utf-8
import requests
import json
from urllib import quote
import hashlib
import os

# string = ""
# headers = {"Content-Type":"application/x-www-form-urlencoded"}
# url = "http://172.18.158.115/data2force/web/index.php?r=site/login&name=13888888888&password=123456"
# r = requests.get(url,headers=headers)
# print r.text

json_string = {"a":"2","b":"123"}
url = "http://172.18.158.117:8087/add"
r = requests.post(url,json_string)
print r.content