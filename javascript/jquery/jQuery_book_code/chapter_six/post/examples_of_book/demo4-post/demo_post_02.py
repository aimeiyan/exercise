__author__ = 'nancy'

import tornado.web
import tornado.ioloop
import json


class MainHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument("username");
        content = self.get_argument("content");
        data = {'username': username, 'content': content}
        self.write(json.dumps(data))


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/post/examples_of_book/demo4-post"})
])

if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()