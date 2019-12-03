
```python
# coding: utf8
"""
策略模式：动态选择算法策略
现实中往往解决问题的方式不止一种，我们可能需要根据问题的特征选择最优的实现策略
函数在python里是一等公民，可以简化策略模式的实现。
"""

threshold_value = 10


def f1(seq):
    pass


def f2(seq):
    pass


def f(seq):
    if len(seq) >= threshold_value:  # 大于某个阈值
        f1(seq)  # 在数量较多时候具有良好的效率
    else:
        f2(seq)

```
