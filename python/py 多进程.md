> Linux 操作系统提供了一个 fork() 函数用来创建子进程，这个函数很特殊，调用一次，返回两次，  
因为操作系统是将当前的进程（父进程）复制了一份（子进程），然后分别在父进程和子进程内返回。  
子进程永远返回0，而父进程返回子进程的 PID。  
我们可以通过判断返回值是不是 0 来判断当前是在父进程还是子进程中执行

> 最后，由于 fork() 是 Linux 上的概念，所以如果要跨平台，最好还是使用 subprocess 模块来创建子进程

```python
import os
import time

print("Before fork process pid=%s, ppid=%s" % (os.getpid(), os.getppid()))

pid = os.fork()
if pid == 0:
    print("I am child process pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    time.sleep(5)
else:
    print("I am parent process pid=%s, ppid=%s" % (os.getpid(), os.getppid()))
    time.sleep(5)

# 下面的内容会被打印两次，一次是在父进程中，一次是在子进程中。
print("After fork process pid=%s, ppid=%s" % (os.getpid(), os.getppid()))

```

multiprocessing模块

```python
# Python提供一个跨平台的多进程支持。
# multiprocessing模块就是跨平台版本的多进程模块，可以在win上用
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

```

```python
# 使用进程池
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 由于Pool的默认大小是CPU的核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  #调用close()之后就不能继续添加新的Process了
    p.join()
    print('All subprocesses done.')

```

subprocess

> subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出

```python
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# # 
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```


分布式进程

https://www.liaoxuefeng.com/wiki/1016959663602400/1017631559645600

