参考: 
[https://www.jianshu.com/p/abfb47d36fba](https://www.jianshu.com/p/abfb47d36fba)
[https://www.jianshu.com/p/de6b292f005d](https://www.jianshu.com/p/de6b292f005d)

select，poll，epoll都是IO多路复用的机制，这里记录select

```python
### select


# select.select(rlist, wlist, xlist[, timeout])
# rlist: 等待读就绪的list
# wlist: 等待写就绪的list
# xlist: 等待“异常”的list

import socket
import select

s = socket.socket()
s.bind(('127.0.0.1', 8888))
s.listen(5)
r_list = [s, ]
num = 0
while True:
    print("r_list length: " + str(len(r_list)))
    rl, wl, error = select.select(r_list, [], [], 0)  # 返回准备就绪的描述符，原本的只要没有移除就会一直存在
    num += 1
    print(rl)
    print("111")
    for fd in rl:
        print("2222")
        if fd == s:   # socket监听到连接就是读就绪状态
            print("333")
            conn, addr = fd.accept()  # socket的connect对象监听数据
            r_list.append(conn)
            msg = conn.recv(200)
            print("connected")
            conn.sendall(('first----%s' % conn.fileno()).encode())
        else:
            print("44444")
            try:
                msg = fd.recv(200)
                print("get data")
                fd.sendall('second'.encode())
            except ConnectionResetError:
                print("remove")
                r_list.remove(fd)

s.close()
```


```python
import socket

flag = 1
s = socket.socket()
s.connect(('127.0.0.1', 8888))
while flag:
    input_msg = input('input>>>')
    if input_msg == '0':
        break
    s.sendall(input_msg.encode())
    msg = s.recv(1024)
    print(msg.decode())

s.close()

```
