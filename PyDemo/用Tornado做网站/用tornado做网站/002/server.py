#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define, options
import signal

from handlers.index import IndexHandler


url = [
    (r"/", IndexHandler),
]
define("port", default = 8000, help = "run on the given port", type = int)

def main():
    tornado.options.parse_command_line()

   # 信号注册函数
    signal.signal(signal.SIGINT, signal.SIG_DFL)


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


    instance = tornado.ioloop.IOLoop.instance()

    # tornado.autoreload.start(instance)

    instance.start()




if __name__ == "__main__":
    main()