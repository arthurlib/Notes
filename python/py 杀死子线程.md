https://blog.csdn.net/vinsuan1993/article/details/78158589

python杀死子线程例子
```python
# coding:utf8
import ctypes
import inspect
import threading
import time

import neco
import uiautomator2 as ut2


class Runner(object):

    def __init__(self, ip, port, packagename):
        self.ip = ip
        self.neco_port = port
        self.packagename = packagename

    def setup_handlers(self):
        # 链接uiautomator2
        self.u = ut2.connect(self.ip)

        # 链接neco
        self.n = neco.safe_connect("{ip}:{port}".format(ip=self.ip, port=self.neco_port))


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def _dump_hierarchy(n, ui_tree):
    hierarchy = n.dump_hierarchy()
    ui_tree.append(hierarchy)


def dump_hierarchy(n, time_out=60):
    ui_tree = []
    hierarchy_thread = threading.Thread(target=_dump_hierarchy, name='_dump_hierarchy', args=[n, ui_tree])
    # 将父线程设置为了守护线程。根据setDaemon()方法的含义，父线程打印内容后便结束了，不管子线程是否执行完毕了。
    hierarchy_thread.setDaemon(True)
    hierarchy_thread.start()

    count = 0
    while True:
        if count > time_out:
            stop_thread(hierarchy_thread)
            raise RuntimeError("dump_hierarchy faild: 没有获取到ui树")

        if ui_tree:
            return ui_tree[0]

        time.sleep(1)
        count += 1
        # print(hierarchy_thread.isAlive())


if __name__ == "__main__":
    runner = Runner("10.242.166.182", "18812", "com.netease.frxy")
    runner.setup_handlers()

    n = runner.n
    u = runner.u
    time.sleep(5)
    a = dump_hierarchy(n, time_out=5)
    print(a)


```