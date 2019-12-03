
```python
# coding: utf8
"""
装饰器模式： 无需子类化实现扩展对象功能问题
"""

from functools import wraps


def memoize(fn):
    known = dict()

    # wraps 则可以将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,或者通过参数选择
    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

```
