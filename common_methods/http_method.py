import sys
sys.path.append('../')
import json
from wish import wish_methods
from joom import joom_methods
from urllib.parse import unquote
from amazon import interface_products
from amazon import interface_sellers
from amazon import interface_orders
import requests

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

def amazon_execute_method_product(request):
    print('/amazon_execute/order is recieved a post request')
    data = request.request.body
    print(data)
    data = data.decode('utf-8').split('&')
    execute_command = {}
    for item in data:
        execute_command[unquote(item.split('=')[0])] = unquote(item.split('=')[1])
    method = eval('interface_orders.interface_orders.'+execute_command['method'])
    # 传入的json字符串中有method这个键，通过eval直接寻找对应键值的方法名
    print(execute_command)
    return_data = method(execute_command)
    #处理请求参数，
    result = return_data
    return result
    
def amazon_execute_method_seller(request):
    print('/amazon_execute/seller is recieved a post request')
    data = request.request.body
    print(data)
    data = data.decode('utf-8').split('&')
    execute_command = {}
    for item in data:
        execute_command[unquote(item.split('=')[0])] = unquote(item.split('=')[1])
    method = eval('interface_sellers.interface_sellers.'+execute_command['method'])
    # 传入的json字符串中有method这个键，通过eval直接寻找对应键值的方法名
    print(execute_command)
    return_data = method(execute_command)
    #处理请求参数，
    result = return_data
    return result

    