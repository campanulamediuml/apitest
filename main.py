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
        result = http_method.post_method(self)
        print(result)
        self.write(result)

class joom_execute(tornado.web.RequestHandler):
    def post(self):
        result = http_method.post_method(self)
        print(result)
        self.write(result)

class amazon_execute(tornado.web.RequestHandler):
    def post(self):
        result = http_method.post_method(self)
        print(result)
        self.write(result)


method_list = [("/joom_execute",joom_execute),("/wish_execute",wish_execute)]

application = tornado.web.Application(method_list)

if __name__ == "__main__":
    print('running...')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()