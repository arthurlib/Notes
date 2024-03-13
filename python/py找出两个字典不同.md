
```
def dict_sync(base, head):
	if id(base) == id(head):
		return {}, {}, {}
	newD, updD, delD = {}, {}, {}
	# for k, v in head.iteritems():
	for k, v in head.items():
		if k in base:
			vb = base[k]
			if isinstance(v, dict):
				_newD, _updD, _delD = dict_sync(vb, v)
				if _newD:
					newD[k] = _newD
				if _updD:
					updD[k] = _updD
				if _delD:
					delD[k] = _delD
			elif v != vb:
				if v is None:
					# None对Lua而言就是nil
					delD[k] = False
				else:
					updD[k] = v
					if isinstance(v, (list, tuple)):
						newD[k] = True
		else:
			updD[k] = v
			newD[k] = True
	# for k, v in base.iteritems():
	for k, v in base.items():
		if k not in head:
			delD[k] = False
	return newD, updD, delD


b = {'a': 1, 'b': 2, 'd': [1, 2, 3, {'1': 1, '2': 2}], 'e': {'1': 1, '2': 2}}
h = {'a': 2, 'c': 3, 'd': [1, 2, 3, {'1': 4, '3': 3}], 'e': {'1': 1, '3': 3}}

r = dict_sync(b, h)

print(r)

```
