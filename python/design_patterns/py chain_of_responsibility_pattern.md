
```python
# coding: utf8
"""
责任链模式:创建链式对象用来接收广播消息
开始介绍行为型设计模式，行为型设计模式处理对象之间的交互和算法问题。
在责任连模式中，我们把消息发送给一系列对象的首个节点，
对象可以选择处理消息或者向下一个对象传递,只有对消息感兴趣的节点处理。

"""


class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    """Docstring for Widget. """

    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow: Default {}'.format(event))


class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    # 注册责任人
    mw = MainWindow()
    sd = SendDialog(mw)  # parent是mw
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)
        print("\n")


if __name__ == "__main__":
    main()

```
