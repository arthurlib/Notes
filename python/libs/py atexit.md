
> 当成程序在退出时(不论是否正常退出，ctrl+c无效)，  
注册执行的函数，栈式，先进后出调用

```python
import atexit


@atexit.register
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')


print(4)

atexit.register(b)
atexit.register(c)

print(3)
atexit.unregister(b)

```
