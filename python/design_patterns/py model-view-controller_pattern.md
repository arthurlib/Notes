
```python
# coding: utf8
"""
mvc模式：解耦展示逻辑和业务逻辑
"""

quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    def get_quote(self, n):
        try:
            return quotes[n]
        except IndexError:
            return 'Not found'


class QuoteTerminalView:

    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError:
                self.view.error("Incorrect index '{}'".format(n))
            else:
                valid_input = True
                quote = self.model.get_quote(n)
                self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

```
