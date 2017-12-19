import requests

url = 'http://localhost:8888/post_test_1'
content = {'content':'just a content'}
r = requests.post(url,content)
print(r.text)