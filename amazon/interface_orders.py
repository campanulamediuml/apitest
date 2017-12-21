import sys
sys.path.append('../')
import requests
from urllib.parse import quote
import time
from common_methods import common_unit

headers = common_unit.headers
default_params = common_unit.default_params
host_name = headers['Host']
port_point = '/Orders/2013-09-01'
api_version = ['Version=2013-09-01']
#本类中的公用方法
connect_url = lambda x,y:'https://'+host_name+port_point+'?'+x+'&Signature='+y


class interface_orders:
    def __init__(self):
        pass     
#直接在亚马逊的class中添加接口方法
#通过连接请求参数，创建亚马逊请求网址
    def ListOrders(execute_command):
        params = ['Action=ListOrders']+api_version
        user_access_dict = common_unit.get_amazon_keys(execute_command['store_id'])
        params += default_params
        # 获取认证参数
        # 把认证参数添加进请求头
        params += common_unit.make_access_param(user_access_dict,execute_command)

        if 'fulfill' in execute_command:
            fulfill_list = execute_command['fulfill'].split(',')
        fulfill_param_list = []
        try:
            for i in asin_list:
                fulfill_param_list.append('FulfillmentChannel.Channel.'+str(fulfill_list.index(i)+1)+'='+i)
        except:
            fulfill_param_list = ['FulfillmentChannel.Channel.1=AFN','FulfillmentChannel.Channel.2=MFN']
        params+=fulfill_param_list
        # 添加邮寄方式
        if 'last_time' in execute_command:
            params += ['CreatedBefore']
