import requests
import json
import time
from multiprocessing.dummy import Pool as ThreadPool

def main():
    url = 'http://localhost:8888/amazon_execute/seller'
    content_1 = {'store_id':'test','method_type':'products','method':'GetMatchingProduct','asin':'B00HHIA5XA,B06XHJMK87','market_place':'usa'}
    content_2 = {'store_id':'test','method_type':'products','method':'ListMatchingProducts','keyword':'condom dildo','market_place':'usa'}
    content_3 = {'store_id':'test','method_type':'sellers','method':'ListMarketplaceParticipations','market_place':'usa'}
    content_4 = {'store_id':'test','method_type':'sellers','method':'GetServiceStatus','market_place':'usa'}

    time_1 = time.time()
    r=requests.post(url,content_4)
    time_2 = time.time()

    print(r.headers,'\n',time_2-time_1)

# def thread_test(num):
#     url = 'http://localhost:8888/thread_test'
#     content = {'thread':str(num)}
#     r=requests.post(url,content)

# num_list = range(0,100)
# pool = ThreadPool(20)

# pool.map(thread_test,num_list)


print(main())