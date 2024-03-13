
```
# coding: utf8

def test():
	for i in range(100000):
		a = i * i


def test_timeit():
	"""timeit只输出被测试代码的总运行时间，单位为秒，没有详细的统计"""
	import timeit

	t = timeit.timeit('test()', 'from __main__ import test', number=1)
	print(t)


def test_profile():
	"""
	ncall：函数运行次数
	tottime： 函数的总的运行时间，减去函数中调用子函数的运行时间
	first percall：percall = tottime / nclall 
	cumtime:函数及其所有子函数调整的运行时间，也就是函数开始调用到结束的时间。
	second percall：percall = cumtime / nclall 
	"""
	import profile
	profile.run('test()')


def test_cProfile():
	"""
	c语言实现的性能测试模块，接口和profile一样
	ncall：函数运行次数
	tottime： 函数的总的运行时间，减去函数中调用子函数的运行时间
	first percall：percall = tottime / nclall 
	cumtime:函数及其所有子函数调整的运行时间，也就是函数开始调用到结束的时间。
	second percall：percall = cumtime / nclall 
	"""
	import cProfile
	cProfile.run('test()')


if __name__ == '__main__':
	# test_timeit()
	test_profile()
	test_cProfile()

```


```
# coding: utf8
"""
检查每行
pip install line_profiler

使用时不导入 profile

命令行运行： kernprof -l -v C:\Python34\test.py

Total Time：测试代码的总运行时间
Hits：表示每行代码运行的次数
Time：每行代码运行的总时间
Per Hits：每行代码运行一次的时间
% Time：每行代码运行时间的百分比
"""
"""
检查每行内存占用
pip install memory_profiler  
pip install psutil  

命令行运行： python -m memory_profiler C:\Python34\test.py

"""
import time


@profile
def fun():
	a = 0
	b = 0
	for i in range(100000):
		a = a + i * i

	for i in range(3):
		b += 1
		time.sleep(0.1)

	return a + b


fun()

```

```
# objgraph

"""
objgraph
内存检测，内存泄露
https://www.cnblogs.com/xybaby/p/7491656.html#_label_6
http://blog.sina.com.cn/s/blog_ad0672d60102xadn.html
"""




import objgraph




class OBJ(object):
	pass


def func_to_leak():
	_cache = []
	o = OBJ()
	_cache.append(o)
	# do something with o, then remove it from _cache

	if True:  # this seem ugly, but it always exists
		return

	_cache.remove(o)


if __name__ == '__main__':
	objgraph.show_growth()
	try:
		func_to_leak()
	except:
		pass
	print('********after call func_to_leak*********')
objgraph.show_growth()

```

```
# coding: utf8
"""
pycharm 分析
使用： profile '' 运行, pycharm会分析结果
https://blog.csdn.net/xiemanr/article/details/69398057
"""
import time


def fun1(a, b):
	print('fun1')
	print(a, b)
	time.sleep(1)


def fun2():
	print('fun2')
	time.sleep(1)


def fun3():
	print('fun3')
	time.sleep(2)


def fun4():
	print('fun4')
	print('fun4')
	print('fun4')
	time.sleep(1)


def fun5():
	print('fun5')
	time.sleep(1)
	fun4()


fun1('foo', 'bar')
fun2()
fun3()
fun5()

```
