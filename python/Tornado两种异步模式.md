Tornado两种异步模式：

1，add_callback(基于asyncio，资源消耗少，性能还不错)

2，run_in_executor((基于线程池/进程池，性能很好，但是资源消耗要高于add_callback的方案)

 

add_callback方案：
```
from tornado.ioloop import IOLoop, PeriodicCallback
import requests

# 业务逻辑操作写在这里
def job():
    url    = 'http://www.httpbin.org/get'
    resp   = requests.get(url)
    print(resp.text)


async def runner():
    loop   = IOLoop.current()
    #任务派发写在这里
    for i in range(10):
        loop.add_callback(job)

    print('This will be executed before loop is finished')

if __name__ == '__main__':
    IOLoop.current().run_sync(runner)
 
```
run_in_executor方案：
```

from tornado.ioloop import IOLoop, PeriodicCallback
import requests
from concurrent.futures import ThreadPoolExecutor

# 业务逻辑写在这里
def job():
    url    = 'http://www.httpbin.org/get'
    resp   = requests.get(url)
    print(resp.text)


async def runner():
    loop   = IOLoop.current()

    # 也可以用进程池ProcessPoolExecutor
    exectutor  = ThreadPoolExecutor(20)
    # 任务派发写在这里
    for i in range(10):
        loop.run_in_executor(exectutor, job)

    print('This will be executed before loop is finished')


if __name__ == '__main__':
    IOLoop.current().run_sync(runner)
```