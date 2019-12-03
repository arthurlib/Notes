
[博客参考](https://blog.csdn.net/liuchunming033/article/details/51455663)

doctest的编写过程就像你在一个交互式shell中导入了一个被测试模块，  
然后一条一条执行被测试模块里面的函数一样。


这里只记录doctest独立文件的方式（另一个方式是嵌入到源代码中）
```python
# file: test.py
def get_sum(a, b):
    return str(a) + str(b)
```

```python
file:doc_test

>>> from test import get_sum
>>> get_sum(3, 4)
'34'
>>> get_sum('a', 3)
'a3'
```

执行下面的命令
```python
python -m doctest -v doc_test
```