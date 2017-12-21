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

def make_access_param(user_access_dict,execute_command):
    #添加请求中包含的asin
    params = [
    'AWSAccessKeyId='+quote(user_access_dict['aws_access_key_id']),
    'MarketplaceId='+quote(market_place_dict[execute_command['market_place']]),
    'MWSAuthToken='+quote(user_access_dict['mws_token']),
    'SellerId='+quote(user_access_dict['seller_id']),
    ]
    return params

def database_connection():
    conn = mydatabase.connect(host=db.host, port=db.port, user=db.user, passwd=db.passwd, db=db.db, charset=db.charset)
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

def get_amazon_keys(store_id):
    cursor,conn = database_connection()
    cursor.execute('SELECT aws_access_key_id,secret_key,seller_id,mws_token FROM store WHERE store_id = %s',store_id)
    store_info = cursor.fetchall()[0]
    user_access = ['aws_access_key_id','secret_key','seller_id','mws_token']
    user_access_dict = {}
    for i in user_access:
        user_access_dict[i] = store_info[user_access.index(i)]
    return user_access_dict

market_place_dict = {
    'usa':'ATVPDKIKX0DER',
    'canada':'A2EUQ1WTGCTBG2',
}

headers = {
            "Host":"mws.amazonservices.com",
            "x-amazon-user-agent": "AmazonJavascriptScratchpad/1.0 (Language=Javascript)",
            "Content-Type": "text/xml"
            }
        #公用请求头

default_params = [
            'SignatureMethod=HmacSHA256',
            'SignatureVersion=2',
            'Timestamp='+get_time_stamp(),
        ]
        #公用请求参数