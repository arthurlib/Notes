
```python
# coding: utf8
"""
单例模式: 使得一个类最多生成一个实例

很奇怪，本书讲完了都没有讲到单例模式。python的单例模式有各种实现，元类、装饰器等，但是还有一种说法：

I don’t really see the need, as a module with functions (and not a class) would serve well as a singleton.
All its variables would be bound to the module, which could not be instantiated repeatedly anyway.
If you do wish to use a class, there is no way of creating private classes or private constructors in Python,
so you can’t protect against multiple instantiations, other than just via convention in use of your API.
I would still just put methods in a module, and consider the module as the singleton.
也就是说，实际上，python中，如果我们只用一个实例，写法如下
"""


# some module.py
class SingletonClass:
    pass


# 在别处我们想用这个实例都直接使用 module.single_instance 这个实例就好。
# 这是最简单也是最直观的一种方式,嗯，直接导入这个实例用，而不是导入class，简单粗暴
single_instance = SingletonClass()

```
