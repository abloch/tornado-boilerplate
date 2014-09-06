#!/usr/bin/env python
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
import os

class HelloHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    settings = { "static_path": os.path.join(os.path.dirname(__file__), "static"), }
    
    return Application([
        url(r"/", HelloHandler),
        ],**settings)


def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
