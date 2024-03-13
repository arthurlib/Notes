
```
import os
import subprocess
import sys

import tornado.ioloop
import tornado.web

base_path = os.path.dirname(os.path.realpath(sys.argv[0]))

logs_dir = os.path.join(base_path, "./logs")
static_dir = os.path.join(base_path, "./static")
print(logs_dir)
print(static_dir)


def init():
    """初始化目录"""
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)


class BaseHandler(tornado.web.RequestHandler):
    # blog.csdn.net/moshowgame 解决跨域问题
    def set_default_headers(self):
        # Tornado获取请求'origin'的方法
        origin = self.request.headers.get('Origin', '')
        print("origin: " + self.request.headers.get('Origin', ''))

        self.set_header('Access-Control-Allow-Origin',
                        origin or '*')  # 设置允许的'origin'，只设置'*'时某些特定情况下会失败故最好优先获取请求的域加入允许组中
        self.set_header('Access-Control-Allow-Credentials',
                        'true')  # 设置是否允许客户端携带证书式访问。通过对 Credentials 参数的设置，就可以保持跨域 Ajax 时的 Cookie
        hs = 'Origin, Content-Type, uid, shop_type, shop_parent, shop_children, session_id, flowid, call_chain, Authorization, md5, User-Agent, Aaaa, Origin, X-Requested-With, Content-Type'
        self.set_header('Access-Control-Allow-Headers', hs)  # 允许提交的头部参数，必须明确写明
        self.set_header('Access-Control-Expose-Headers', 'Content-Length')  # 列出了哪些首部可以作为响应的一部分暴露给外部
        self.set_header('Access-Control-Allow-Methods', '*')  # 设置允许请求的方法
        # self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')

    def options(self):  # 携带了多的header参数时必须
        print("run options")
        self.set_status(204)


class LogSaveHandler(BaseHandler):
    def post(self):
        data = {
            "success": False,
            "msg": ""
        }
        namespace = self.get_argument("namespace", "")
        text = self.get_argument("text", "")

        if not namespace or not text:
            data["msg"] = "error: namespace,text are necessary and can not be null or '';"
            self.write(data)
            return

        with open(os.path.join(logs_dir, namespace), "a") as f:
            f.write(text + '\n')

        data['success'] = True
        self.write(data)

    def get(self):
        self.post()


class LogGetHandler(BaseHandler):
    def get(self, namespace, num):
        # data = {
        #     "success": False,
        #     "msg": ""
        # }
        result = subprocess.Popen('tail -n {} {}'.format(str(num), os.path.join(logs_dir, namespace)),
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

        result = result.stdout.readlines()
        self.write('<br/>'.join([r.decode("utf8") for r in result]))

    def post(self, namespace, num):
        self.get(namespace, num)


settings = {
    "static_path": static_dir,
}


def make_app():
    return tornado.web.Application([
        (r"/log/save", LogSaveHandler),
        (r"/log/get/(?P<namespace>.*)/(?P<num>.*)", LogGetHandler),
    ], **settings)


if __name__ == "__main__":
    init()
    app = make_app()
    app.listen(8280)
    print("172.24.30.221:8280")
    print("server is runing...")
    tornado.ioloop.IOLoop.current().start()

```
