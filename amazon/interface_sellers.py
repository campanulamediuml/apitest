import sys
sys.path.append('../')
import requests
from urllib.parse import quote
import time
from common_methods import common_unit

headers = common_unit.headers
default_params = common_unit.default_params
host_name = headers['Host']
port_point = '/Sellers/2011-07-01'
api_version = ['Version=2011-07-01']
# 关于api的分类和版本
connect_url = lambda x,y:'https://'+host_name+port_point+'?'+x+'&Signature='+y

class interface_sellers:
    def __init__(self):
        pass

    def ListMarketplaceParticipations(execute_command):
        params = ['Action=ListMarketplaceParticipations']+api_version
        user_access_dict = common_unit.get_amazon_keys(execute_command['store_id'])
        params += common_unit.make_access_param(user_access_dict,execute_command)
        params = params + default_params
        params = sorted(params)
        # 拼接公有请求参数，认证请求参数，和特征请求参数，并进行排序
        # 拼接请求身，需要按首字母排序
        # 关于api的分类和版本
        params = '&'.join(params)
        # print(params)
        # 对请求身进行分割
        sig_string = 'POST\n'+host_name+'\n'+port_point+'\n'+params
        # 连接签名字符串
        signature = quote(str(common_unit.cal_signature(sig_string,user_access_dict['secret_key'])))
        # 计算字符串的加密签名
        url = connect_url(params,signature)
        # 拼接请求字符串
        r = requests.post(url,headers=headers)
        # 发起请求
        # print(common_unit.xmltojson(r.text))
        return common_unit.xmltojson(r.text)

    def GetServiceStatus(execute_command):
        params = ['Action=GetServiceStatus']+api_version
        user_access_dict = common_unit.get_amazon_keys(execute_command['store_id'])
        params += common_unit.make_access_param(user_access_dict,execute_command)
        params = params + default_params
        params = sorted(params)
        # 拼接公有请求参数，认证请求参数，和特征请求参数，并进行排序
        # 拼接请求身，需要按首字母排序
        # 关于api的分类和版本
        params = '&'.join(params)
        # print(params)
        # 对请求身进行分割
        sig_string = 'POST\n'+host_name+'\n'+port_point+'\n'+params
        # 连接签名字符串
        signature = quote(str(common_unit.cal_signature(sig_string,user_access_dict['secret_key'])))
        # 计算字符串的加密签名
        url = connect_url(params,signature)
        # 拼接请求字符串
        r = requests.post(url,headers=headers)
        # 发起请求
        # print(common_unit.xmltojson(r.text))
        return common_unit.xmltojson(r.text)