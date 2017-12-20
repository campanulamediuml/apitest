import sys
sys.path.append('../')
import time
from urllib.parse import quote
import hmac
import base64
import hashlib
import xmltodict
import json
import pymysql as mydatabase
from common_methods import db

def database_connection():
    conn = mydatabase.connect(host=db.host, port=db.port, user=db.user, passwd=db.passwd, db='db_dolphin', charset=db.charset)
    cursor = conn.cursor()
    return cursor,conn

def cal_signature(string,secret_key):
    message = bytes(string.encode('utf-8'))
    secret = bytes(secret_key.encode('utf-8'))
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    signature = signature.decode('utf-8')
    return signature
    #计算签名，必须解码成utf-8的格式

def xmltojson(xmlstr): 
    xmlparse = xmltodict.parse(xmlstr)  
    jsonstr = json.dumps(xmlparse,indent=1)  
    return jsonstr
    #把返回的xml格式处理成json

def get_md5(string):
    md5=hashlib.md5(string).hexdigest()
    return md5
    #计算md5校验

def get_time_stamp():
    time_stamp = time.localtime()
    time_stamp = quote(str(time_stamp[0])+'-'+str(time_stamp[1])+'-'+str(time_stamp[2])+'T'+str(int(time_stamp[3])-8)+':'+str(time_stamp[4])+':'+str(time_stamp[5])+'.'+str(time_stamp[6]))
    stmp = time_stamp[:-2]+'Z'
    return stmp
    # 计算美国当地时间的时间戳（很重要）