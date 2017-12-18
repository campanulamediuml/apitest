import requests
import json
from urllib import quote
import config
import xmltodict
import hashlib
import time

file = 'test'
action = 'SubmitFeed'
 

def xmltojson(xmlstr): 
    xmlparse = xmltodict.parse(xmlstr)  
    jsonstr = json.dumps(xmlparse,indent=1)  
    return jsonstr

def get_md5(string):
    md5=hashlib.md5(string).hexdigest()
    return md5


string_tuple = (str(config.AWSAccessKeyId),str(config.seller_id))

time_stamp = time.localtime()
print time_stamp
time_stamp = quote(str(time_stamp[0])+'-'+str(time_stamp[1])+'-'+str(time_stamp[2])+'T'+str(int(time_stamp[3])-8)+':'+str(time_stamp[4])+':'+str(time_stamp[5])+'.'+str(time_stamp[6]))
print time_stamp

headers = {'Host':'mws.amazonservices.com','Content-MD5':get_md5(file),'Content-Type':'text/tab-separated-values; charset=iso-8859-1'}

amz_string = ['https://mws.amazonservices.com',
'/?AWSAccessKeyId=2'+config.AWSAccessKeyId,
'&Action=SubmitFeed',
'&FeedType=_POST_PRODUCT_DATA_',
'&MWSAuthToken='+config.MWS_token,
'&MarketplaceIdList.Id.1=ATVExampleDER',
'&SellerId=A1XExample5E6',
'&SignatureMethod=HmacSHA256',
'&SignatureVersion=2',
'&Timestamp='+time_stamp,
'&Version=2009-01-01',
'&Signature=SvSExamplefZpSignaturex2cs%3D']
url = ''.join(amz_string)

r = requests.post(url)
# print r.text
print xmltojson(r.text)
 

def send_feed_data():
    return 0


def test_upload():
    return 0

