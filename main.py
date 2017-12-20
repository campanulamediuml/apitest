import tornado.ioloop
import tornado.web
from common_methods import http_method

# class get_test_1(tornado.web.RequestHandler):
#     def get(self):
#         result = method.get_method(self)
#         print(result)
#         self.write(result)

class wish_execute(tornado.web.RequestHandler):
    def post(self):
        result = http_method.wish_execute_method(self)
        print(result)
        self.write(result)
#对应wish的操作
class joom_execute(tornado.web.RequestHandler):
    def post(self):
        result = http_method.joom_execute_method(self)
        print(result)
        self.write(result)
#对应joom的操作
class amazon_execute(tornado.web.RequestHandler):
    def post(self):
        result = http_method.amazon_execute_method(self)
        print(result)
        self.write(result)
#对应亚马逊的操作
method_list = [("/joom_execute",joom_execute),("/wish_execute",wish_execute),("/amazon_execute",amazon_execute)]
#初始化方法列表
application = tornado.web.Application(method_list)

if __name__ == "__main__":
    print('running...')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    #开始使用，监听8888端口