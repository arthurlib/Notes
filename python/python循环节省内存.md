```
from itertools import chain, accumulate, compress, dropwhile, takewhile, filterfalse
# 节省内存

# 拼接元素
# itertools 中的 chain 函数实现元素拼接，原型如下，参数 * 表示个数可变的参数
# chain(iterables)
t = chain(['I', 'love'], ['python'], ['very', 'much'])
l = list(t)
print(t)
print(l)  # ['I', 'love', 'python', 'very', 1]

# 逐个累积
# 返回列表的累积汇总值，原型：
# accumulate(iterable[, func, *, initial=None])
t = accumulate([1, 2, 3, 4, 5, 6], lambda x, y: x * y)
l = list(t)
print(t)
print(l)  # [1, 2, 6, 24, 120, 720]

# 漏斗筛选
# 它是 compress 函数，功能类似于漏斗功能，所以我称它为漏斗筛选，原型：
# compress(data, selectors)
t = compress('abcdefg', [1, 1, 0, 1])
l = list(t)
print(t)
print(l)  # ['a', 'b', 'd']

# 段位筛选
# 扫描列表，不满足条件处开始往后保留，原型如下：
# dropwhile(predicate, iterable)
t = dropwhile(lambda x: x < 3, [1, 0, 2, 4, 1, 1, 3, 5, -5])
l = list(t)
print(t)
print(l)  # [4, 1, 1, 3, 5, -5]

# 段位筛选 2
# 扫描列表，只要满足条件就从可迭代对象中返回元素，直到不满足条件为止，原型如下：
# takewhile(predicate, iterable)
t = takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])
l = list(t)
print(t)
print(l)  # [1, 4]

# 次品筛选
# 扫描列表，只要不满足条件都保留，原型如下：
# dropwhile(predicate, iterable)
t = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
l = list(t)
print(t)
print(l)  # [1, 3, 5]



``