***目前目的是搞清楚py的协程发展，以及常见的模块的联系，因为之前感觉很混乱，故整理如下。找时间还要再整理看下***


从0到1，Python异步编程的演进之路 - 知乎 https://zhuanlan.zhihu.com/p/25228075

参考：  
* gevent: http://hhkbp2.com/gevent-tutorial/#
* gevent: https://softlns.github.io/2015/11/28/python-gevent/

gevent是基于协程的Python网络库,基于libevent的快速事件循环(Linux上epoll，FreeBSD上kqueue)

* gevent和asyncio: https://zhuanlan.zhihu.com/p/54657754

使用asyncio(基于生成器的协程)，不建议使用 gevent. 为什么： https://toutiao.io/posts/w4qjkn/preview

* asyncio官方文档: https://docs.python.org/zh-cn/3/library/asyncio-task.html

> 协程底层原理,yield

```python
# 协程底层原理,yield
import time


def task_1():
    t = 0
    while True:
        time.sleep(1)
        print("start a")
        yield t
        t += 1
        print("end a")


def task_2():
    t = 0
    while True:
        time.sleep(1)
        print("start b")
        yield t
        t += 1
        print("end b")


fa = task_1()
fb = task_2()

while True:
    print(next(fa))
    print(next(fb))

```

> greenlet实现协程，封装了yield）

```python
# greenlet实现协程，封装了yield）
from greenlet import greenlet  # 需要安装greenlet模块  sudo pip3 install greenlet (python2.x使用pip)
import time


def test1():
    while True:
        print("---A--")
        gr2.switch()  # 切换到gr2中的任务。
        time.sleep(0.5)


def test2():
    while True:
        print("---B--")
        gr1.switch()  # 切换到gr1中的任务。
        time.sleep(0.5)


gr1 = greenlet(test1)  # greenlet 底层封装了yield。
gr2 = greenlet(test2)

# 切换到gr1中运行
gr1.switch()

print("end")

```

> gevent实现协程，封装了greenlet(pip show gevent 可以查看依赖关系)，遇到阻塞代码自动切换协程任务

```python
# gevent实现协程，封装了greenlet，遇到阻塞代码自动切换协程任务
import gevent  # 需要安装gevent模块  sudo pip3 install gevent (python2.x使用pip) 
import time
 
 
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)   # 为了提高协程效率,遇到阻塞类代码,会自动切换协程任务。
        # time.sleep(0.5)   # 阻塞类代码必须使用gevent自己包装的代码，原生阻塞类代码不会切换协程任务。 
                            # 可以使用monkey.patch_all()将所有原生阻塞类代码替换成gevent包装的阻塞类代码。 
 
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # <Greenlet "Greenlet-0" at 0x7f4a09b34648: f1(5)> 0
        gevent.sleep(0.5)
        # time.sleep(0.5)
 
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)
        # time.sleep(0.5)
 
 
g1 = gevent.spawn(f1, 5)  # gevent其实是对greenlet的封装。
g2 = gevent.spawn(f2, 5)  # 第一个参数f2表示协程执行的具体任务(函数)，第二个参数5表示要传给f2的参数
g3 = gevent.spawn(f3, 5)
g1.join()   # 遇到阻塞类代码,自动切换协程任务。
g2.join()
g3.join()
```

> gevent打补丁，monkey自动替换原生阻塞类代码。重要，常用

```python
# gevent打补丁，monkey自动替换原生阻塞类代码。重要，常用
import gevent  # 需要安装gevent模块  sudo pip3 install gevent (python2.x使用pip)
import time
from gevent import monkey
 
# gevent打补丁
monkey.patch_all()  # 将所有原生阻塞类代码自动替换成gevent包装的阻塞类代码。 
 
 
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)  # 会自动替换成 gevent.sleep(0.5)
 
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
 
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
 
 
# g1 = gevent.spawn(f1, 5)
# g2 = gevent.spawn(f2, 5)
# g3 = gevent.spawn(f3, 5)
# g1.join()
# g2.join()
# g3.join()
 
# 一种简便写法
gevent.joinall([
        gevent.spawn(f1, 5),
        gevent.spawn(f2, 5),
        gevent.spawn(f3, 5)
])
```

> gevent底层原理

```python
# gevent底层原理
import socket
import time
 
tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_tcp.bind(("", 7899))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)  # 设置套接字为非堵塞的方式。 (接收数据时如果没有接到数据(阻塞)那么就抛异常,否则正常接收数据。)
 
client_socket_list = list()  # 用于保存与客户端连接的套接字。
 
while True:
 
    # time.sleep(0.5)
 
    try:
        new_socket, new_addr = tcp_server_tcp.accept()  # 用抛异常的方式代替阻塞。
    except Exception as ret:
        print("---没有新的客户端到来---")
    else:
        print("---只要没有产生异常，那么也就意味着 来了一个新的客户端----")
        new_socket.setblocking(False)  # 设置套接字为非堵塞的方式。 (如果需要阻塞就直接抛异常代替阻塞)
        client_socket_list.append(new_socket)
        
    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)    # 用抛异常的方式代替阻塞。
        except Exception as ret:
            print("----这个客户端还没有发送过来数据----")
        else:
            if recv_data:
                # 对方发送过来数据
                print("----客户端发送过来了数据-----")
            else:
                # 对方调用close 导致了 recv返回
                client_socket.close()
                client_socket_list.remove(client_socket)
                print("---客户端已经关闭----")
        
```


> 从yield/send => asyncio.coroutine和yield from => async和await, 参考:  
http://blog.guoyb.com/2016/07/03/python-coroutine/

> async/await入门指南： https://zhuanlan.zhihu.com/p/27258289
