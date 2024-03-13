
> collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类

> https://docs.python.org/zh-cn/3/library/collections.html


OrderedDict类：排序字典，是字典的子类。
namedtuple()函数：命名元组，是一个工厂函数。
Counter类：为hashable对象计数，是字典的子类。
deque：双向队列。
defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。


```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
```

> collections.deque 双向队列
```python

```
