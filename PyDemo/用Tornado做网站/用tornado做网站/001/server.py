#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define, options



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read: www.itdiffer.com\r\n')
url = [
    (r"/", IndexHandler),
]
define("port", default = 8000, help = "run on the given port", type = int)

def main():
    tornado.options.parse_command_line()

    settings = dict(
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "statics")
        )
    application = tornado.web.Application(
        handlers = url,
        **settings
        )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print("Development server is running at http://127.0.0.1:%s" % options.port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()