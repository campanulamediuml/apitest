import sys
sys.path.append('../')
import sys
import requests
import json
from urllib.parse import quote
from wish import config

# debug = 1
# if debug:
#     json_line = {"shop":"wish","method":"create"}

def retrieve_a_product(json_line):
    access_line = (config.access_token,'T_DVa_test')
    url = 'https://merchant.wish.com/api/v2/variant?access_token=%s&sku=%s'%access_line
    r = requests.post(url)
    print(r.text)

def update_a_product(json_line):
    access_token = quote(config.access_token)
    parent_sku = quote('DVa_test')
    name = quote('longlongagothereisaDVa')
    description = quote('This DVa is the best on Wish')
    tags = quote('I like DVa')
    url = "https://merchant.wish.com/api/v2/product/update?access_token=%s&parent_sku=%s&name=%s&description=%s&tags=%s"%(access_token,parent_sku,name,description,tags)
    r = requests.post(url)
    print(r.text)

def create_a_product(json_line):
    line = [config.access_token,'https://static.zerochan.net/D.Va.full.2078278.jpg','D.Va_test_6','just_a_test_item','test,d.va,overwatch','DVa_test_get_test_6','10','9999','100','https://static.zerochan.net/D.Va.full.2024803.jpg','DVa_test_get_test_6']
    item_line = []
    for i in line:
        item_line.append(quote(i))
    item_line = tuple(item_line)
    #print item_line
    url = "http://merchant.wish.com/api/v2/product/add"
    content ="access_token=%s&main_image=%s&name=%s&description=%s&tags=%s&sku=%s&inventory=%s&price=%s&shipping=%s&extra_images=%s&parent_sku=%s"%item_line
    print(content)
    # r = requests.get(url,content)
    # print r.text