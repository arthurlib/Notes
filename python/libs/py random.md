使用python random模块的choice方法随机选择某个元素

```python
foo = ['a', 'b', 'c', 'd', 'e']
from random import choice
print(choice(foo))
```

使用python random模块的sample函数从列表中随机选择一组元素

```python
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#从list中随机获取5个元素，作为一个片断返回
slice = random.sample(list, 5)
#原有序列并没有改变。
print(slice)
print(list)
```
