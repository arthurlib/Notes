# 基本数据类型

|   关键字   |  类型   |
|:-------:|:-----:|
|   int   |  整型   |
|   int   |  整型   |
|  long   |  长整型  |
|  float  |  浮点数  |
| boolean |  布尔   |
| string  |  字符串  |
|  list   | 列表 [] |
|  tuple  | 元组 () |
|  dict   | 字典 {} |
|   set   |  集合   |

> 不可变类型: int, long, float, string, tuple

> 可变类型:   list, dict, set


* r"" 不转义


# 关于中文

> py3原生支持utf8, py2有以下操作

在文件开始添加
```python
# -*- coding: UTF-8 -*-
```
或者这样定义 utf-8 编码的中文字符串
```python
s = u"中文"
```
或者
```python
a = "啊啊啊啊"
a.decode('utf-8')  #转换成 utf-8
```


# 有用的函数

|       函数        |      说明       |
|:---------------:|:-------------:|
|     type()      |   查看变量的数据类型   |
|     help()      |    查看帮助文档     |
|      id()       |    查看变量 id    |
|      dir()      |    查看有哪些方法    |
|      len()      |    查看字符串长度    |
| sys.getrefcount | python内部的引用计数 |


# 关于变量

1. 动态特性 可以赋予不同的数据类型
2. 多重赋值

```python
#下面相当于 a,b,c = ("str","str1",4)
a,b,c = "str","str1",4

del b  #删除变量
```


# print 使用

```python
print(2)
print(2,3)  # 输出到同一行
```


# 控制流语句

## if
```python
# pass 表示什么都不执行，可以避免报错
if True: 
    pass
else:
    pass

if True:
    pass
elif True:
    pass
else:
    pass
    
if True:
    pass
    
if not False:
    pass
```


## 布尔值的运算符

| 关键字 | 说明               |
|:----:|:-----------------:|
| and | 全部都为bool值        |
| or  | 至少有一项为bool真      |
| is  | 检查共享，检查是否引用同一个对象 |
| ==  | 检查值              |
| not | 非                |


## 三元表达式

```python
4 if True else 3
#相当于
if True:
	print(4)
else:
	print(3)
```

## while,for

```python
while True:
    print(3)
else:
	print('在while正常跑完时执行,没有break')
```

## break,continue

```python
for x in "i am a man".split(" "):#以空格分隔
    print(x)
else:
    print('与while相同')
# x保留最后迭代值
```

## or的运用

```python
a = url.get(from) or None #如果前一个为null, 则赋值None
```

## for 使用

```python
a = "asdfas"
for i in a:
    print(i)

b = [1,2,3,4,5]
for i in b:
    pirnt(i)

c = ('a','b','c')
for i in c:
    print(i)


#如果定义了重复的键，只取最后一个
a = {'key1':'value1','key2':'value2','key2':'vale3'}

#遍历键
for i in a.keys():
    print(i)

#同时遍历键值
for x,y in a.items():
    print(x,y)

```

根据字典的值得到字典的键
1. 字典索引的是键，而不是值->迭代，穷举
2. 字典具有唯一键，单值却不要求是唯一的
3. 一个值可能对应多个键



# with语句

```python
g = open('a.txt'，'w')
g.write("hahhahahahah\nhahah")
g.close()

#下面的代码与上面等同，会自动关闭文件
with open('a.txt','a') as g:
    g.write('xixixi')
```



# list(列表)

1. 有序的集合
2. 通过偏移来索引，从而读取数据
3. 支持嵌套
4. 可变的类型
1. 切片：
a = [1,2,3，4，5，6，7］
正向索引 :a[1:5]
反向索引 :a[-4:-1]
默认索引 :a[:], a[:3], a[1:]

## 添加操作
* '+'生成一个新的列表
* extend() :接受参数并将该参数的每个元素都添加到原有的列表中，原地修改列表而不是新建列表
* append() :添加任意对象到列表的末端
* insert() :插入任意对象到列表中，可以控制插入位置。

## 修改

修改列表本身只需要直接赋值操作就行。
```python
A   = [1,2,3]
A[0]='haha'
```

## 删除操作

* del()   :我们通过索引删除指定位置的元素。
* remove():移除列表中指定值的第一个匹配值。如果没找到的话，会抛异常。
* pop()   :返回最后一个元素，并从list中删除它。

## 成员关系：

In , not in :我们可以判断一个元素是否在列表里。返回一个bool类型，元素在列表里返回true，否则返回fasle.

## 列表推导式

[expr for iter_var in iterable]

1. 首先迭代iterable里所有内容，每一次迭代，都把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

比如我们要生成一个包含1到10的列表
```python
[x for x in range(1,11)]

Range(1,11)
```

[expr for iter_var in iterable if cond_expr]

2. 加入了判断语句，只有满足条件的内容才把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

要生成包含1到10的所有奇数列表。
```python
range(1,11,2)

[x for x in range(1,11) if x % 2 == 1]
```

```
[x*x for x in range(100)]

#生成字符串
['the %s'%d for d in xrange(10)]

#生成元组
[(x,y) for x in range(2) for y in range(2)]

#生成字典
dict([(x,y) for x in range(3) for y in range(2)])
```

## 内置list方法
```
list(a) #返回一个列表，参数是可迭代对象，可传入字符串，元组
```
range 返回一个列表对象
xrange 返回xrange对象
上面的区别在python3中已经没有了

del a 删除列表对象的引用
del a[:] 清空列表对象里的元素


## 	排序:sort 翻转:reverse

a = [33,11,22,44]

b = a.sort() #排序，默认从小到大, 返回值为None
b = a. reverse() #反转一个list返回值为none,结合上面从大到小排序

## list 其他操作

```python
b = a[:]  #这样可以拷贝,而不是拷贝引用
````

# 集合

## 创建集合
set():可变的，不可变的frozenset()
## 操作
1. 添加 add，update
2. 删除：remove
3. 交集，并集，差集：& | -
4. 成员关系 in ,  not in
5. set去重，列表内容元素重复
```python
a=[1,2,1,2,12,1,2]
list(set(a)) #这样可以将列表内容去重
```

# 字典

## 创建

{} , dict()
```python
info = {'name':'lilei','age':20}
info = dict(name='lilei',age=20)
```
字典的键必须是不可变的数据类型，比如数字，字符串，元组
binfo = {1:'22',2:'33'}
binfo = {(1,2),'as',(a,b),"df"}

##添加内容
a['xx'] = 'xx'
```python
info['phone'] = 'iphone'
```
## 修改内容
a['xx'] = 'xx'
```python
例如 info['phone'] = 'htc'
```

## update
参数是一个字典的类型，会覆盖相同的值
```python
info.update({'city':'beijing','phone':'nokia'})
```
## 删除清空操作
```python
del info['phone']       #删除某个元素
info.clear()            #删除字典的全部元素
info.pop('name')        #返回值，删除键名
info.pop('name','1234') #name 不存在返回默认值 1234
```

## get
```python
info.get('name')      #没有返回 NoneType 类型
info.get('age2','22') #可以设置默认值
```

## 成员关系操作
in 和has_key()
```python
phone in info
info.has_key('phone')
```
## 其他操作
keys()   :返回的是列表，里面包含了字典的所有键
values() :返回的是列表，里面包含了字典的所有值
items()  :生成一个字典的容器 :[()]

binfo = {'a':[1,2,3],'b':[4,5,6]}
binfo['a'][2] = 5     #修改的方式

字典排序，以键从小到大
```
key_list = a.keys()
key_list.sort()
for x in key_list:
    print(x,a[x])
```


# 函数

定义
```python
def a():
    "在这里写函数文档"
    retur 4

print(test.__doc__) #输出函数文档
#是class时写在class开头，也可写在整个文件的开头，使用模块名.__doc__方式访问
```

带参数，有默认值
```python
def test(a=4):
    return a

def test3(a,c,d="json"):
    return
test3(2,3,d="xml")
```

```python
global b #在函数中声明全局变量，声明后可以修改全局变量
```

```python
def test1(**kr):
    return kr
print(test1(c=1,g=24)) #转换成字典输出


def test2(*z):
    return z
print(test2(1,2,3,435,[2,3,4])) #转换成元组输出


def test(*z,**kr): #一种用法：可以用于读取多余的参数，保函数运行
    return z,kr

#"**" 字典
#"*"  元组
```


# 函数注意点

* 功能完整
* 异常处理完善
* 参数默认值:更省事，更可配置

```python
 assert add(2,4) == 3     #assert :断言，对函数返回值和类型进行确认

dir(func.__code)__)       #查看该属性拥有的项
func.__code__.co_varnames #查看函数有哪些参数
func.__code__.co_filename #查看该函数来自哪个文件
```

# lambda

1. lambda是一个表达式。
2. 它没有名称，存储的也不是代码块，而是表达式。
3. 它被用作执行很小的功能，不能在里面使用条件语句。


```python
d = lambda x:x+1
print(d(2))

d = lambda x:x+1 if x > 0 else "error"

#d = lambda x:列表推导式
d = lambda x:[(x,i) for i in xrange(0,10)]

t = [1,2,3,4,5]
g = filter(lambda x:x > 3,t) #过滤出大于 3 的数字
```

# 函数参数位置：
1. 先是位置匹配的参数
2. 再是关键字匹配的参数
3. 收集匹配的元组参数
4. 收集匹配的关键字参数



1. 如何去定义一个最基本的class
2. class最基本的子元素
3. class传参
4. __init__方法
5. class和函数的区别

# 定义 class
可继承，重写，
```python
# -*- coding: utf-8 -*-
class test(object): #所有的class都是object的派生类

	a = 1 #属性

	#当定义一个class的内置方法时，方法的参数的第一个永远是self。
	def __init__(self,var1): #构造函数
		self.var1 = var1 #这里的 self.var1 为全局变量

	#get被称之为test对象的方法
	def get(self,a=None):
		return self.var1

	def __del__(self): #析构函数
		del self.arg1

	pass


#使用
t = test('test str heiheihei')
print(t.get())
```
1. 通过在一个变量或者函数之前加上下划线来表示私有变量的，例如__spam(这里是两个下划线)就是私有的。
2. Python会在类的内部自动的把你定义的__spam变量的名字替换成为 _classname__spam(注意，classname前面是一个下划线，spam前是两个下划线)，Python把这种技术叫做“name mangling”。因此，用户在外部访问__spam的时候就会提示找不到相应的变量。

# 模块

包的创建 :文件夹中创建 __init__.py 文件


搜索模块
```python
import  sys
sys.path.append('/tmp/m2') #添加模块搜索路径
```

下面的含义是: 当前文件作为主函数时执行，其他文件 import 不执行
```
if __name__ == "__main__":
    pass
```

# 异常

## 捕获异常
```python
try:
    pass
except Error:
    pass
fjinally:  #终止行为
    pass
```

## 引发异常
```python
try:
    raise IndexError #引发异常
except IndexError:
    pass
```

assert语句也可以用来触发异常，它是一个有条件的raise，主要用在开发过程中调试

assert False, "出错信息"


## 用户自定义的异常
```python
class Bad(Exception):
    pass

def doomed():
    raise Bad()

try:
    doomed()
except Bad:
    print('got Bad')
```

