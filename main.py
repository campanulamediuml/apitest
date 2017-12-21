import tornado.ioloop
import tornado.web
from common_methods import http_method


# class get_test_1(tornado.web.RequestHandler):
#     def get(self):
#         result = method.get_method(self)
#         print(result)
#         self.write(result)

# class wish_execute(tornado.web.RequestHandler):
#     def post(self):
#         result = http_method.wish_execute_method(self)
#         print(result)
#         self.write(result)
# #对应wish的操作
# class joom_execute(tornado.web.RequestHandler):
#     def post(self):
#         result = http_method.joom_execute_method(self)
#         print(result)
#         self.write(result)
#对应joom的操作
class amazon_execute_product(tornado.web.RequestHandler):
    def post(self):
        result = http_method.amazon_execute_method_product(self)
        self.write(result)

class amazon_execute_order(tornado.web.RequestHandler):
    def post(self):
        result = http_method.amazon_execute_method_order(self)
        self.write(result)

class amazon_execute_seller(tornado.web.RequestHandler):
    def post(self):
        result = http_method.amazon_execute_method_seller(self)
        self.write(result)

#对应亚马逊的product接口

method_list = [
        ("/amazon_execute/product",amazon_execute_product),
        ('/amazon_execute/order',amazon_execute_order),
        ('/amazon_execute/seller',amazon_execute_seller)
        ]
#初始化方法列表
application = tornado.web.Application(method_list)


if __name__ == "__main__":
    print('running')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    

    
    #开始使用，监听8888端口