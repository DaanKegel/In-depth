#!/usr/bin/python3

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
    	(r"/index.php", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {path: "."}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()