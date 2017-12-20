import sys
sys.path.append('../')
import requests
from urllib.parse import quote
import time
from common_methods import common_unit


headers = common_unit.headers
default_params = common_unit.default_params
host_name = headers['Host']
port_point = '/Products/2011-10-01'
# 关于api的分类和版本
def connect_url(params,signature):
    url = 'https://'+host_name+port_point+'?'+params+'&Signature='+signature
    return url

class interface_products:
    def __init__(self):
        pass     
#直接在亚马逊的class中添加接口方法
#通过连接请求参数，创建亚马逊请求网址
    def GetMatchingProduct(execute_command):
        params = ['Action=GetMatchingProduct']
        user_access_dict = common_unit.get_amazon_keys(execute_command['store_id'])
        # 获取包含认证参数的字典
        if 'asin' in execute_command:
            asin_list = execute_command['asin'].split(',')
        asin_param_list = []
        #计算asin列表
        try:
            for i in asin_list:
                asin_param_list.append('ASINList.ASIN.'+str(asin_list.index(i)+1)+'='+i)
        except:
            asin_param_list = ['ASINList.ASIN.1=']
        # 如果不存在asin列表，则直接返回一个空列表扔掉
        # 上面计算的asin列表是该接口的特征参数
        # 添加请求中包含的asin
        params = params + common_unit.make_access_param(user_access_dict,execute_command) + default_params + asin_param_list
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


    def ListMatchingProducts(execute_command):
        params = ['Action=ListMatchingProducts']
        user_access_dict = common_unit.get_amazon_keys(execute_command['store_id'])

        if 'keyword' in execute_command:
            params.append('Query='+ quote(execute_command['keyword']))
        else:
            params.append('Query=')
        # 如果不存在搜索关键词，则直接返回一个空的query
        # 获取特征参数query即搜索关键词
        params = params + common_unit.make_access_param(user_access_dict,execute_command) + default_params
        params = sorted(params)
        # 拼接公有请求参数，认证请求参数，和特征请求参数，并进行排序
        # 拼接请求身，需要按首字母排序
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

