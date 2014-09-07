#!/usr/bin/env python
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado import template
import os

class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    settings = {
		"static_path": os.path.join(os.path.dirname(__file__), "static"),
		"template_path": os.path.join(os.path.dirname(__file__),"templates"),
	}
    templatesLoader = template.Loader(os.path.join(os.path.dirname(__file__), "templates"))
    return Application([
        url(r"/", IndexHandler),
        ],**settings)


def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
