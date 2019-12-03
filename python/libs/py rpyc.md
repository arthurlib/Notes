官方文档： https://rpyc.readthedocs.io/en/latest/  
https://rpyc.readthedocs.io/en/latest/tutorial.html

使用场景： 一种是调用远端的模块，另外一种是调用远端的函数

###### server

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
from rpyc import Service
from rpyc.utils.server import ThreadedServer


class TimeService(Service):
    def on_connect(self, *args, **kwargs):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        print("on connect")
        pass

    def on_disconnect(self, *args, **kwargs):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        print("on disconnect")
        pass

        # 对于服务端来说， 只有以"exposed_"打头的方法才能被客户端调用，所以要提供给客户端的方法都得加"exposed_"

    def exposed_get_time(self):
        return time.ctime()  # time模块中的一个内置方法

    def exposed_change_text(self, s):
        return "test+" + s


s = ThreadedServer(service=TimeService, port=12233, auto_register=False)
s.start()

```


###### client

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import rpyc


conn = rpyc.connect('localhost',12233)
#调用服务器端的方法，格式为：conn.root.xxx。xxx代表服务器端的方法名
# get_time是服务端的那个以"exposed_"开头的方法
result = conn.root.get_time()
print(result)
print(conn.root.change_text('ggggggggggggggg'))
conn.close()
```



1. Client一定要 close()连接
2. Server中exposed_打头的函数才能被 客户端调用。所以如果写服务端代码的时候想要让客户端调用 就要加这一个前缀。
3. client要访问服 务器端代码通过c.root.xxx才能访问，如：c.root.get_time() 调用服务器端get_time方法
4. RPYC没有认证机制，任何客 户端都可以直接访问服务器端的暴露的方法
5. 如果cResult是其它类型的数据的话， 你conn.close()之后，cResult就为空的了(这是因为对于其它类型的返回值，服务端返回的是rpyc.netref的封装nobj， 当访问nobj时，它连接到服务端，取值，并返回给客户端，你close之后就连不到服务端了)，所以最好在服务端把计算结果处理下，转换成数字或字符串(对于大字典来说，可以用json转换下，然后客户端再转过来就ok了)




跨服务器调用方案：

gRPC
[java和python使用grpc交互 - zhj_fly的博客 - CSDN博客](https://blog.csdn.net/zhj_fly/article/details/82684970)
[gRPC 官方文档中文版_V1.0](https://doc.oschina.net/grpc?t=58008)
