
```
import json
import msgpack

a = {'a': 1, 'b': "1", 'c': {'a': 1, 'b': 1}}
print(len(json.dumps(a)))
print((msgpack.packb(a)))
print(len(msgpack.packb(a)))

b1 = {'a': 'a', 'b': 'b'}
b2 = (1, 2)
b3 = [1, 2]
b4 = "aa"
print(msgpack.packb(b1))
print(len(msgpack.packb(b1)))
print(len(msgpack.packb(b2)))
print(len(msgpack.packb(b3)))
print(len(msgpack.packb(b4)))

print("***********")
c1 = [0] * 32
c2 = {1: {'status': 0},2: {'status': 0},3: {'status': 0},4: {'status': 0},5: {'status': 0},6: {'status': 0},7: {'status': 0},}
print(len(msgpack.packb(c1)))
print(len(msgpack.packb(c2)))


```
