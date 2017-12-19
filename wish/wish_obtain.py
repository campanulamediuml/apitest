import requests
import json
from urllib import quote
import config


def get_token():
    accessment = (config.client_id,config.client_secret,config.code,'https://www.guokr.com/')
    url = 'https://merchant.wish.com/api/v2/oauth/access_token?client_id=%s&client_secret=%s&code=%s&redirect_uri=%s&grant_type=authorization_code'%accessment
    r = requests.post(url)
    print r.text
    write_dict = json.loads(r.text)
    config_content = open('config.py').readlines()
    if len(config_content) == 5:
        config_content = config_content[:-2]
    fh = open('config.py','w')
    for line in config_content:
        fh.write(line)
    fh.write('access_token = "'+write_dict['data']['access_token']+'"\n')
    fh.write('refresh_token = "'+write_dict['data']['refresh_token']+'"')

def test_token():
    url = 'https://merchant.wish.com/api/v2/auth_test?access_token=%s'%config.access_token
    r = requests.post(url)
    print r.text

def refresh_token():
    accessment = (config.client_id,config.client_secret,config.refresh_token)
    url = 'https://merchant.wish.com/api/v2/oauth/refresh_token?client_id=%s&client_secret=%s&refresh_token=%s&grant_type=refresh_token'%accessment
    r = requests.post(url)
    print r.text
    write_dict = json.loads(r.text)
    config_content = open('config.py').readlines()
    if len(config_content) == 5:
        config_content = config_content[:-2]
    fh = open('config.py','w')
    for line in config_content:
        fh.write(line)
    fh.write('access_token = "'+write_dict['data']['access_token']+'"\n')
    fh.write('refresh_token = "'+write_dict['data']['refresh_token']+'"')

test_token()