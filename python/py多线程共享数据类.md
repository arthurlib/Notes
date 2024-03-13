
```
# 共享数据类
import threading


class _State(threading.local):
	def __init__(self):
		self.contexts = (tuple(), None)


# 共享单例
_state = _State()
cap_contexts = [_state.contexts]
try:
	current_state = _state.contexts
	_state.contexts = cap_contexts[0]
finally:
	_state.contexts = current_state


print(_state.contexts)
```
