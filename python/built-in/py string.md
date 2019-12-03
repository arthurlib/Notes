
# 字符串拼接

1. 字符串拼接 "+" 号连接 浪费性能，不推荐
2. 字符串模板
'%s' :字符串占位符
'%d' :整型占位符
```python
"test %s test" % "this"
"test %s test %s" % ("this","that")
```
3. 优秀拼接方案
```
a = 'one'
b = 'two'
c = 'three'
",".join([a,b,c]) #以逗号分隔返回字符串
"".join([a,b,c]) #返回拼接后的字符串
```
4. format使用
```python
#下面 前面的数字对应后面的位置，也可不填数字，此时前后一一对应
a = "test {1} {0} " .format("one" , "two")
#更人性化的方式
a = "test {whose} {fruit} " .format(fruit="one" , whose="two")
```
5. 字典方式
```python
a = "test %(whose)s %(fruit)s" % {'whose':'my','fruit':'apple'}
```

# string 操作

字符串替换
```python
a = a.replace("原字符串","目标字符串")
```

```python
import string
g = string.maketrans('123',"abc") #g 为模板
a = '1234567'
print(a.translate(g)) #根据模板替换
#上面输出为：
#abc4567
#是逐个替换，有对应关系1->a这样
translate(g,'1') #删除字符串中全部的 1
```

字符串查找
```python
a.find("要查询的字符串")    #返回开始的位置
a.find("要查询的字符串",20) #从字符串的20位开始查找
```

字符串排序
```python
a = "234rsDSFJ"
print(sorted(a,reverse=True))
print(sorted(a,key=str.upper))
```


# 文件操作
```python
d = open('a.txt', 'w') #打开文件,模式可以是w/r/a
d.write('test,\ntest')
d.close()            #关闭
d.readline()
d.seek(0)            #偏移量移动到开头
d.read(1000)         #读多少个字节
```

```python
import linecache
linecache.getline("a.txt",int(line)) #获取某一行
linecache.getline("a.txt ")         #获取全部
```
