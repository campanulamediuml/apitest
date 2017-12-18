import tornado.ioloop
import tornado.web
import method

class get_test_1(tornado.web.RequestHandler):
    def get(self):
        result = method.get_method(self)
        print(result)
        self.write(result)

class wish_execute(tornado.web.RequestHandler):
    def post(self):
        result = method.post_method(self)
        print(result)
        self.write(result)

method_list = [("/get_test_1",get_test_1),("/wish_execute",wish_execute)]

application = tornado.web.Application(method_list)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()