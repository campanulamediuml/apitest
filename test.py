import tornado.ioloop
import tornado.web
import method

class get_test_1(tornado.web.RequestHandler):
    def get(self):
        #填写
        self.write()

class post_test_1(tornado.web.RequestHandler):
    def post(self):
        result = method.post_method(self)
        print(result)
        if not result:
            self.set_status(400)
            self.write("content is null.")
            self.finish()
            return
        else:
            self.write(result)
            return

method_list = [("/get_test_1",get_test_1),("/post_test_1",post_test_1)]

application = tornado.web.Application(method_list)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()