https://www.runoob.com/python/python-built-in-functions.html

abs()        返回数字的绝对值

divmod()    把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)

input()  py3接受一个标准输入数据，返回为 string 类型

open()  用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写

staticmethod()  返回函数的静态方法，一般用于类中方法的装饰器

all()   用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False

enumerate()  用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

int()  用于将一个字符串或数字转换为整型

ord()  是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常

str()  将对象转化为适于人阅读的形式

any()  用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。元素除了是 0、空、FALSE 外都算 TRUE。

eval()  用来执行一个字符串表达式，并返回表达式的值

isinstance()  判断一个对象是否是一个已知的类型，类似 type()
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系
isinstance() 会认为子类是一种父类类型，考虑继承关系
如果要判断两个类型是否相同推荐使用 isinstance()。

pow()  返回 xy（x的y次方） 的值

sum()  对系列进行求和计算

basestring()  py2才有是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))

execfile() py2 可以用来执行一个文件
py3 exec(compile(open(filename,"rb").read(), filename, 'exec'), globals, locals)
exec(open(filename).read())

issubclass()  用于判断参数 class 是否是类型参数
classinfo 的子类

print()  用于打印输出，最常见的一个函数

super()  用于调用父类(超类)的一个方法

bin()  返回一个整数 int 或者长整数 long int 的二进制表示

file()  py2 创建一个 file 对象，它有一个别名叫 open()，更形象一些，它们是内置函数。参数是以字符串的形式传递的

iter()  用来生成迭代器。

property()  作用是在新式类中返回属性值

tuple()  数将列表转换为元组

bool()  用于将给定参数转换为布尔类型，如果没有参数，返回 False

filter()  用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中
len()  返回对象（字符、列表、元组等）长度或项目个数
range() 可创建一个整数列表，一般用在 for 循环中
type()   只有第一个参数则返回对象的类型，三个参数返回新的类型对象
bytearray()  返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
float()  用于将整数和字符串转换成浮点数
list()  用于将元组转换为列表
raw_input()  用来获取控制台的输入
unichr()  和 chr()函数功能基本一样， 只不过是返回 unicode 的字符
callable()  用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。

对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True
format()  一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

基本语法是通过 {} 和 : 来代替以前的 % 
locals()  会以字典类型返回当前位置的全部局部变量。

对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True
reduce()  对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
unicode()
chr()   range（256）内的（就是0～255）整数作参数，返回一个对应的字符
frozenset()  返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
long()  将数字或字符串转换为一个长整型
reload()  重新载入之前载入的模块
vars()  返回对象object的属性和属性值的字典对象
classmethod()  修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
getattr()  用于返回一个对象属性值
map()  会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
repr()  将对象转化为供解释器读取的形式
xrange()  用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器
cmp()  于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
globals()  会以字典类型返回当前位置的全部全局变量
max()  返回给定参数的最大值，参数可以为序列
reverse()  用于反向列表中元素
zip()  用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。

如果需要了解 Pyhton3 的应用，可以参考 Python3 zip()。
compile()  函数将一个字符串编译为字节代码。
hasattr()   用于判断对象是否包含对应的属性
memoryview()    函数返回给定参数的内存查看对象(memory view)。

所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问
round()    返回浮点数x的四舍五入值
__import__()  用于动态加载类和函数 。

如果一个模块经常变化就可以使用 __import__() 来动态载入
complex()  用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。
hash()  用于获取取一个对象（字符串或者数值等）的哈希值
min()  返回给定参数的最小值，参数可以为序列
set()  创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
delattr()  用于删除属性。

delattr(x, 'foobar') 相等于 del x.foobar
help()  用于查看函数或模块用途的详细说明
next()  返回迭代器的下一个项目。

next() 函数要和生成迭代器的iter() 函数一起使用
setattr()  对应函数 getattr()，用于设置属性值，该属性不一定是存在的
dict()  用于创建一个字典
hex()  用于将10进制整数转换成16进制，以字符串形式表示
object()
slice()  实现切片对象，主要用在切片操作函数里的参数传递
dir()  函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息
id()  函数返回对象的唯一标识符，标识符是一个整数。

CPython 中 id() 函数用于获取对象的内存地址。
oct()  将一个整数转换成8进制字符串
sorted()  对所有可迭代的对象进行排序操作。

sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
exec 内置表达式  执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。

需要说明的是在 Python2 中exec不是函数，而是一个内置语句(statement)，但是Python 2中有一个 execfile() 函数。可以理解为 Python 3 把 exec 这个 statement 和 execfile() 函数的功能够整合到一个新的 exec() 函数中去了

