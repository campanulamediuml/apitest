import sys
sys.path.append('../')
import json
from wish import wish_methods
from joom import joom_methods
from urllib.parse import unquote
from amazon import interface_products
import requests

# def get_method(request):
#     content = request.get_argument("content",None)
#     result = {"tip":"get successful","content":content}
#     result = json.dumps(result)
#     return result

# def wish_execute_method(request):
#     execute_method = request.get_argument("method",None)
#     execute_type = request.get_argument("type",None)
#     if method == "create":
#         wish_methods.cread(method)
#     elif method == "retrieve":
#         pass
#     elif method == "update":
#         pass
#     else:
#         result == {"status_code":"0","error_message":"illegal execute"}
#     result = json.dumps(result)
#     return result   

def amazon_execute_method_product(request):
    print('/amazon_execute/product is recieved a post request')
    data = request.request.body
    print(data)
    data = data.decode('utf-8').split('&')
    execute_command = {}
    for item in data:
        execute_command[unquote(item.split('=')[0])] = unquote(item.split('=')[1])
    method = eval('interface_products.interface_products.'+execute_command['method'])
    # 传入的json字符串中有method这个键，通过eval直接寻找对应键值的方法名
    print(execute_command)
    return_data = method(execute_command)
    #处理请求参数，
    result = return_data
    return result
    
# def joom_execute_method(request):
#     execute_method = request.get_argument("method",None)
#     execute_type = request.get_argument("type",None)
#     if method == "create":
#         wish_methods.cread(method)
#     elif method == "retrieve":
#         pass
#     elif method == "update":
#         pass
#     else:
#         result == {"status_code":"0","error_message":"illegal execute"}
#     result = json.dumps(result)
#     return result

def thread_test_method(request):
    data = request.get_argument("thread")
    requests.get('http://scp-wiki-cn.wikidot.com/scp-series')
    print('thread finished',data)
    return '0'
    