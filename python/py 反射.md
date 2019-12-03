
例子

```python
#encoding=utf-8
'''
Created on 2013-08-29

@author: Martine
'''


class Test(object):
    def __init__(self):
        self.name = 'tesname'
        
    def foo(self,name):
        self.name = name
        
        
if __name__ == "__main__":
#     print 'this is my first python ...'
    eval_test = eval('Test()')
    print eval_test
    print 'old name is :%s ' % eval_test.name
    func = getattr(eval_test, 'foo')
    print func
    
    func('new_name')
    print 'new name is :%s ' % eval_test.name
```



例子
```python
#dynamic.py
imp = input("请输入模块:")
dd = __import__(imp)
# 等价于import imp
inp_func = input("请输入要执行的函数：")

f = getattr(dd,inp_func，None)#作用:从导入模块中找到你需要调用的函数inp_func,然后返回一个该函数的引用.没有找到就烦会None

f() # 执行该函数
```



介绍四个内置函数:
```python
1. getattr()函数是Python自省的核心函数，具体使用大体如下：
class A: 
def __init__(self): 
self.name = 'zhangjing'
#self.age='24'
def method(self): 
print"method print"
  
Instance = A() 
print getattr(Instance , 'name, 'not find') #如果Instance 对象中有属性name则打印self.name的值，否则打印'not find'
print getattr(Instance , 'age', 'not find') #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'
print getattr(a, 'method', 'default') #如果有方法method，否则打印其地址，否则打印default 
print getattr(a, 'method', 'default')() #如果有方法method，运行函数并打印None否则打印default 

2. hasattr(object, name)

说明：判断对象object是否包含名为name的特性（hasattr是通过调用getattr(ojbect, name)是否抛出异常来实现的）

3. setattr(object, name, value)

这是相对应的getattr()。参数是一个对象,一个字符串和一个任意值。字符串可能会列出一个现有的属性或一个新的属性。这个函数将值赋给属性的。该对象允许它提供。例如,setattr(x,“foobar”,123)相当于x.foobar = 123。

4. delattr(object, name)

与setattr()相关的一组函数。参数是由一个对象(记住python中一切皆是对象)和一个字符串组成的。string参数必须是对象属性名之一。该函数删除该obj的一个由string指定的属性。delattr(x, 'foobar')=del x.foobar
```

基于反射机制模拟web框架路由

　　需求：比如我们输入:www.xxx.com/commons/f1，返回f1的结果。

```python
# 动态导入模块，并执行其中函数
url = input("url: ")

target_module, target_func = url.split('/')
m = __import__('lib.'+target_module, fromlist=True)

inp = url.split("/")[-1]  # 分割url,并取出url最后一个字符串
if hasattr(m,target_func):  # 判断在commons模块中是否存在inp这个字符串
    target_func = getattr(m,target_func)  # 获取inp的引用
    target_func()  # 执行
else:
    print("404")
```



python中反射4种方法的基本使用

```python
class Foo(object):

    def __init__(self):
        self.name = "laozhang"

    def func(self):
        return "hello python"

obj = Foo()
#判断ｏｂｊ中是否有第二个参数
#如果第二个只是属性，则返回属性值，如果是方法名，则返回方法的内存地址，如果第二个参数没有在对象中找到，程序崩溃
# res = getattr(obj,"name１") #程序崩溃
# res = getattr(obj,"name") #返回属性值 并同时可省略r = res()
res = getattr(obj,"func") #res为ｆｕｎｃ的内存地址
r = res()
print(r)

#检查ｏｂｊ中是否存在func成员,当找到第二个参数时返回ｔｒｕｅ，否则返回ｆａｌｓｅ
res = hasattr(obj,"func")
print(res)

print(obj.name) #查看之前obj的ｎａｍｅ
#设置obj中ｎａｍｅ为laowang
res = setattr(obj,"name","laowang")
print(obj.name)
#当设置的值不存在时，会自动添加到实例对象中
#setattr需要三个参数: x,y,z　==> x.y =z
#相当于obj.age = 10
setattr(obj,"age","10")
print("name=%s,age=%s"%(obj.name,obj.age))  #laowang 10

#删除对象的属性
delattr(obj,"age")
print("name=%s,age=%s"%(obj.name,obj.age))  #程序崩溃

```

Python：import 与__import__()

参考： https://www.cnblogs.com/f1194361820/p/9675960.html

```
首先来说一下两者的区别：

　　import指令做了两件事：1）搜索module，2）绑定到局部变量
　　内置函数__import__()只做了一件事：搜索module

　　import指令执行过程中是调用__import__()来完成Module检索的。
```

python 动态导入模块 importlib.import_module

https://blog.csdn.net/tumi678/article/details/80514028
> 作为python标准库提供，提供python import语法和(__import__()函数)的实现，另外importlib提供了开发者可以创建自己的对象(即importer)来处理导入过程

