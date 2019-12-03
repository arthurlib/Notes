
```
"""
defaultdict()defaultdict和namedtuple()是collections模块里面2个很实用的扩展类型。
一个继承自dict系统内置类型，
一个继承自tuple系统内置类型。
在扩展的同时都添加了额外的的特性，而且在特定的场合都很实用。
"""
from collections import defaultdict, namedtuple


def test_defaultdict():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

    # 设置value默认类型
    d = defaultdict(list)
    # 会有默认值，所以可以append
    for k, v in s:
        d[k].append(v)

    print(list(d.items()))

    d_2 = {}
    for k, v in s:
        # 可以设置默认值
        d_2.setdefault(k, []).append(v)
    print(list(d_2.items()))

    d_3 = {}
    for k, v in s:
        # 没有默认值，会报错
        d_3[k].append(v)
    print(d_3.items())


def test_namedtuple():
    TPoint = namedtuple('TPoint', ['x', 'y'])

    # 生成对象
    t = [10, 20]
    p = TPoint._make(t)
    print(p)

    p = TPoint(x=11, y=22)
    print(p)

    # 替换值
    p = p._replace(x=44, y=33)
    print(p)

    # 将字典数据转换成namedtuple类型
    d = {'x': 44, 'y': 55}
    p = TPoint(**d)
    print(p)

    # 常用使用示例
    # CityRecord = namedtuple('City', 'Name, Country, Dsitrict, Population')
    # for city in map(CityRecord._make, cur.fetchall()):
    #     print(city.Name, city.Population)

```
