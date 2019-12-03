> Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。  
绝大多数情况下，我们只需要使用threading这个高级模块。  
thread 模块是py2.7的，py3为兼容改名_thread，用py3 的thrading就行


一个thread模块的例子（不建议使用，py2可用）
```python
import time  
import thread  

def runner(arg):  
    for i in range(6):  
        print(str(i)+':'+arg)

        time.sleep(1)  
    #结束当前线程  
    thread.exit_thread()  #等同于thread.exit()  

#启动一个线程，第一个参数为函数名，  
#第二个参数为一个tuple类型，是传给函数的参数  
thread.start_new_thread(runner, ('hello world',))   #等同于thread.start_new(runner, ('hello world'))  

#创建一个锁，锁用于线程同步，通常控制对共享资源的访问  
lock = thread.allocate_lock()  #等同于thread.allocate()  
num = 0  
#获得锁，成功返回True，失败返回False  
if lock.acquire():  
    num += 1  
    #释放锁  
    lock.release()  
#thread模块提供的线程都将在主线程结束后同时结束，因此将主线程延迟结束  
time.sleep(10)  
print('num:'+str(num)) 
```
----------

```
threading.Thread类的常用方法

1.在自己的线程类的__ init__里调用threading.Thread.__init__(self,name=threadname)，threadname为线程的名字。
2.run()，通常需要重写，编写代码实现做需要的功能。
3.getName()，获得线程对象名称。
4.setName()，设置线程对象名称。
5.start()，启动线程。
6.join([timeout])，等待另一线程结束后再运行。
7.setDaemon(bool)，设置子线程是否随主线程一起结束，必须在start()之前调用。默认为False。
8.isDaemon()，判断线程是否随主线程一起结束。
9.isAlive()，检查线程是否在运行中。

```

```python
import time, threading


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 直接实例化
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

```

```python
# 继承方式
import time, threading
class runner(threading.Thread):  
    def __init__(self, name):  
        threading.Thread.__init__(self)  
        self.name = name  
        self.thread_stop = False  
    def run(self):  
        while not self.thread_stop:  
            print str(self.name)+':'+'hello world'  
            time.sleep(1)  
    def stop(self):  
        self.thread_stop = True  

def test():  
    t = runner('thread')  
    t.start()  
    time.sleep(10)  
    t.stop()  

if __name__ == '__main__':  
    test()  
```


带锁 Lock
```python
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```

带锁RLock


```python
import time  
import threading  
num=0  
lock = threading.RLock()  
class runner(threading.Thread):  
    def __init__(self, name):  
        threading.Thread.__init__(self)  
        self.name = name  

    def run(self):  
        global num    
        while True:   
            if num >= 6: break  
            if lock.acquire():  
                print "Thread(%s) locked, Number: %d" % (self.name, num)    
                time.sleep(1)  
            lock.release()  
            print "Thread(%s) released, Number: %d" % (self.name, num)  
            time.sleep(1)  
            num += 1   

def test():  
    t1 = runner('thread1')  
    t2 = runner('thread2')  
    t1.start()  
    t2.start()  

if __name__== '__main__':    
    test()    
    
# 在threading module中，python又提供了Lock对象的变种:
# RLock对象。RLock对象内部维护着一个Lock对象，它是一种可重入的对象。
# 对于Lock对象而言，如果一个线程连续两次进行acquire操作，
# 那么由于第一次acquire之后没有release，第二次acquire将挂起线程。
# 这会导致Lock对象永远不会release，使得线程死锁

# RLock对象允许一个线程多次对其进行acquire操作，因为在其内部通过一个counter变量维护着线程acquire的次数。
# 而且每一次的acquire操作必须有一个release操作与之对应，在所有的release操作完成之后，别的线程才能申请该RLock对象。
```


每个线程保存自己的变量
```python
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

线程池

https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p07_creating_thread_pool.html
