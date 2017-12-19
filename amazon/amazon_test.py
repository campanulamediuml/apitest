import sys
sys.path.append('../')
import requests
from urllib.parse import quote
import config
import time
from common_methods import common_unit


file = 'test'
action = 'SubmitFeed'

headers = {
    "Host":"mws.amazonservices.com",
    "x-amazon-user-agent": "AmazonJavascriptScratchpad/1.0 (Language=Javascript)",
    "Content-Type": "text/xml"
    }
#请求头，按照亚马逊的要求

params = sorted([
'AWSAccessKeyId='+quote(config.AWSAccessKeyId),
'Action=GetMatchingProduct',
'MarketplaceId=ATVPDKIKX0DER',
'ASINList.ASIN.1=B00TUA0R6I',
'MWSAuthToken='+quote(config.MWS_token),
'SellerId='+quote(config.seller_id),
'SignatureMethod=HmacSHA256',
'SignatureVersion=2',
'Timestamp='+common_unit.get_time_stamp(),
'Version=2011-10-01'])
#请求身，需要按首字母排序

host_name = headers['Host']
port_point = '/Products/2011-10-01'
#关于api的分类和版本
params = '&'.join(params)
#对请求身进行分割
sig_string = 'POST\n'+host_name+'\n'+port_point+'\n'+params
#连接签名字符串
signature = quote(str(common_unit.cal_signature(sig_string,config.secret_key)))
#计算字符串的加密签名
url = 'https://'+host_name+port_point+'?'+params+'&Signature='+signature
#拼接请求字符串
r = requests.post(url)
#发起请求
print(common_unit.xmltojson(r.text))

def send_feed_data():
    return 0


def test_upload():
    return 0

