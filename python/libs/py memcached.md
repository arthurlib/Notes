
## 安装

```python
pip install python-memcached
```


## 简单示例

```python
#!/usr/bin/env python3
#coding:utf8
import memcache
#链接
mc = memcache.Client(['139.129.5.191:12000'], debug=True)
#插入
mc.set("name", "python")
#读取
ret = mc.get('name')
print (ret)
 
# 输出结果
python
 
# debug=True表示运行出现错误时，可以显示错误信息，正式环境可以不加
```


## 支持集群

> python-memcached模块原生支持集群操作，其原理是在内存中维护一个主机列表，  
且集群中主机的权重值和主机在列表中重复出现的次数成正比

主机列表为：host_list = ["1.1.1.1", "1.1.1.2","1.1.1.2","1.1.1.3","1.1.1.3","1.1.1.3",]

用户如果要在内存中创建一个键值对（如：k1 = "value1"），那么要执行以下步骤：

1. 根据算法将k1转换成一个数字
2. 将数字和主机列表长度求余数，得到一个值N（0 <= N < 长度）
3. 在主机列表中根据第二步得到的值为索引获取主机，例如: host_list[N]
4. 连接将第三步中获取的主机，将k1 = "value1" 放置在该服务器的内存中

```
#!/usr/bin/env python3
#coding:utf8
import memcache
mc = memcache.Client([('1.1.1.1:12000', 1), ('1.1.1.2:12000', 2),('1.1.1.3:12000',3)])
mc.set('k1','value1')
ret = mc.get('k1')
print (ret)
```

## 基本memcached操作


### add

> 添加一条键值对，如果已经存在的key，重复执行add操作会出现异常

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.add('k1', 'v1')
mc.add('k1', 'v2') # 报错，对已经存在的key重复添加，失败！！！
例如：
ret1 = mc.add('name','tom')
print(refalse)
ret2 = mc.add('name','jack')
print(retrue)
结果：
False #当已经存在key 那么返回false
True  #如果不存在key 那么返回true
```

### replace

> replace修改某个key的值，如果key不存在，则异常

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
re = mc.get('name')
print(re)
rereplace = mc.replace('name','jack')
re = mc.get('name')
print(rereplace,re)
结果：
tom  #第一次赋值
True jack #如果存在key那么修改成功为yaoyao 返回True
rereplace = mc.replace('name1','hahaha')
re = mc.get('name1')
print(rereplace,re)
结果：
False None #如果不存在key，修改失败，返回空值
```

### set 和 set_multi

> set : 设置一个键值对，如果Key不存在，则创建，如果key存在，则修改。

> set_multi : 设置多个键值对，如果key不存在，则创建，如果key存在，则修改。

```python
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
re = mc.get('name')
print('set用法',re) #设置一个键值对
dic = {'name':'to,','age':'19','job':'IT'}
mc.set_multi(dic)  #设置多个键值对
#或者mc.set_multi({'name':'tom','age':'19','job':'IT'})
mcname = mc.get('name')
mcage = mc.get('age')
mcjob = mc.get('job')
print('set_multi用法:',mcname,mcage,mcjob)
```

### delete 和 delete_multi

> delete : 在Memcached中删除指定的一个键值对

> delete_multi : 在Memcached中删除指定多个键值对

```python
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
re = mc.get('name')
print('存在',re)
mc.delete('name')
re = mc.get('name')
print('删除',re)  #删除一个键值对
```

### get 和 get_multi

> get : 获取一个键值对

> get_multi : 获取多个键值对

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('name','tom')
re = mc.get('name')
print('get',re)     #获取一个键值对
dic = {'name':'to,','age':'19','job':'IT'}
mc.set_multi(dic)
regetmu=mc.get_multi(['name','age','job'])
print('get_multi',re) #获取多个键值对的值
```

### append 和 prepend

> append : 修改指定key的值，在该值后面追加内容。

> prepend : 修改指定key的值，在该值前面插入内容。

```python
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('num','第一|')
re = mc.get('num')
print(re)
mc.append('num','追加第二个') #在第一后面追加
re = mc.get('num')
print(re)
mc.prepend('num','我是零个')  #在第一前面追加
re = mc.get('num')
print(re)

结果：
第一|
第一|追加第二个
我是零个第一|追加第二个
```

### decr 和 incr

> decr : 自减，将Memcached中的一个值增加N（N默认为1）

>  incr  : 自增，将Memcached中的一个值减少N（N默认为1）

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'])
mc.set('num','1')
re = mc.get('num')
print('我是没加过的值',re)
mc.incr('num','9')
re = mc.get('num')
print('我是加上新增后的值',re)
mc.decr('num','5')
re = mc.get('num')
print('我是减去的值',re)
# 结果：
我是没加过的值 1
我是加上新增后的值 10
是减去的值 5
```

### gets 和 cas

> 使用缓存系统共享数据资源就必然绕不开数据争夺和脏数据（数据混乱）的问题。

假设商城某件商品的剩余个数保存在memcache中，product_count = 900  
A用户刷新页面从memecache中读取到product_count = 900  
B用户刷新页面从memecache中读取到product_count = 900  
A,B用户均购买商品，并修改product_count的值  
A修改后，product_count = 899  
B修改后，product_count = 899  
然而正确数字应该是898，数据就混乱了。  
如果想要避免这种情况的发生，则可以使用  gets　和　cas  

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import memcache
mc = memcache.Client(['0.0.0.0:12000'],cache_cas=True)
mc.set('count','10')
reget = mc.get('count')
print('件数',reget)
regets = mc.gets('count')
print(regets)
# 如果有人在gets之后和cas之前修改了product_count，那么，
下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生
recas = mc.cas('count','11')
print(recas)
regets = mc.gets('count')
print('修改',regets)
```
> 本质上每次执行gets时，会从memcache中获取一个自增的数字，通过cas去修改gets的值时，  
会携带之前获取的自增和memcache中的自增值进行比较，如果相等，则可以提交，如果不相等，  
那么表示在gets和cas执行之间，又有其他人执行了gets，则不允许修改。
