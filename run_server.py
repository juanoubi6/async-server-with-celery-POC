import tornado.ioloop
from tornado.web import Application

from app.controllers import CpuBoundController


def make_app():
    return Application([
        (r"/cpu-bound-task", CpuBoundController),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(9000)
    print("Starting server at port 9000")
    tornado.ioloop.IOLoop.current().start()
