
```python
# coding: utf8
"""
模板模式：抽象出算法公共部分从而实现代码复用
模板模式中，我们可以把代码中重复的部分抽出来作为一个新的函数，把可变的部分作为函数参数，从而消除代码冗余。
一次性实现一个算法的不变的部分，并将可变的行为留给子类来实现。

控制子类扩展。模板方法只在特定点调用“hook ”操作，这样就只允许在这些点进行扩展。
"""

ingredients = "spam eggs apple"
line = '-' * 10


# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items"""
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter()[::-1]:
        action(element)
        print(line)

    # Getters


def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


# Makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""

    def template():
        skeleton(getter, action)

    return template


# Create our template functions
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]

# Execute them
for template in templates:
    template()

```
