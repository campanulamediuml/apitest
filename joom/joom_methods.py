import sys
sys.path.append('../')
import requests
import json
from urllib.parse import quote
from joom import config

debug = 0

def create_a_product():
    url = 'https://api-merchant.joom.com/api/v2/product/add'
    post_dict = {}
    r = requests.post(url,post_dict)
    print(r.text)

# def 

#create_a_product()