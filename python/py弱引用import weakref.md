
```
import sys
import weakref


def t1():
	class A():
		pass

	def P(a):
		# print(a)
		print("gggccc")

	a = A()

	print(sys.getrefcount(a))

	r = weakref.ref(a)
	r2 = weakref.ref(a)
	print(sys.getrefcount(a))
	print(r)

	print(weakref.getweakrefcount(a))
	print(weakref.getweakrefcount(r))
	print(weakref.getweakrefs(a))
	# print(r() == c)
	# del a
	# del c
	# print(r)
	print(r())

	p = weakref.proxy(a, P)
	print(p)
	# del p
	del a


def t2():
	# -*- coding:utf-8 -*-
	import weakref
	import gc
	from pprint import pprint
	class Graph(object):
		def __init__(self, name):
			self.name = name
			self.other = None

		def set_next(self, other):
			print("%s.set_next(%r)" % (self.name, other))
			self.other = other

		def all_nodes(self):
			yield self
			n = self.other
			while n and n.name != self.name:
				yield n
				n = n.other
			if n is self:
				yield n
			return

		def __str__(self):
			return "->".join(n.name for n in self.all_nodes())

		def __repr__(self):
			return "<%s at 0x%x name=%s>" % (self.__class__.__name__, id(self), self.name)

		def __del__(self):
			print("(Deleting %s)" % self.name)

	def collect_and_show_garbage():
		print("Collecting...")
		n = gc.collect()
		print("unreachable objects:", n)
		print("garbage:", )
		pprint(gc.garbage)

	def demo(graph_factory):
		print("Set up graph:")
		one = graph_factory("one")
		two = graph_factory("two")
		three = graph_factory("three")
		one.set_next(two)
		two.set_next(three)
		three.set_next(one)

		print("Graph:")
		print(str(one))
		collect_and_show_garbage()

		print(three=None)
		two = None
		print("After 2 references removed")
		print(str(one))
		collect_and_show_garbage()

		print()
		print("removeing last reference")
		one = None
		collect_and_show_garbage()

	gc.set_debug(gc.DEBUG_LEAK)
	print("Setting up the cycle")
	print(demo(Graph))
	print()
	print("breaking the cycle and cleaning up garbage")
	print(gc.garbage[0].set_next(None))

	while gc.garbage:
		del gc.garbage[0]
	print(collect_and_show_garbage())

def t3():
	class A():
		def p(selfs):
			print(1231213414)

	v = A()
	# a = weakref.WeakValueDictionary()
	a = weakref.WeakKeyDictionary()
	# a = {}
	t = "aasfasflkjaf"
	a[v] = t
	print(a.data)
	del t
	print(a.data)
t3()

```
