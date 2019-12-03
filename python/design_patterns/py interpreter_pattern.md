
```python
# coding: utf8
"""
解释器模式：用来实现Domain Specific Language(DSL)

给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

当有一个语言需要解释执行, 并且你可将该语言中的句子表示为一个抽象语法树时，
可使用解释器模式。而当存在以下情况时该模式效果最好：

该文法简单对于复杂的文法, 文法的类层次变得庞大而无法管理。此时语法分析程序生成器这样的工具是更好的选择。
它们无需构建抽象语法树即可解释表达式, 这样可以节省空间而且还可能节省时间。

效率不是一个关键问题，最高效的解释器通常不是通过直接解释语法分析树实现的, 而是首先将它们转换成另一种形式。
例如，正则表达式通常被转换成状态机。但即使在这种情况下, 转换器仍可用解释器模式实现, 该模式仍是有用的。
"""
from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


def main():
    # 首先定义我们的DSL格式，我们这里最简单的控制语法就是   "open -> gate"
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    gate = Gate()
    cmds = ['open -> gate', 'close -> gate']  # 两个自定义的命令
    open_actions = {'gate': gate.open}
    close_actions = {'gate': gate.close}

    for cmd in cmds:
        print(event.parseString(cmd))  # [['open'], ['gate']]
        cmd, dev = event.parseString(cmd)
        cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
        print(cmd_str, dev_str)
        if 'open' in cmd_str:
            open_actions[dev_str]()
        elif 'close' in cmd_str:
            close_actions[dev_str]()


if __name__ == "__main__":
    main()

```
