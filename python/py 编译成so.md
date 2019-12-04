环境


```
pip install cython
yum install python-devel
yum install gcc
```

编写测试文件a.py

```
class A:
    def say(self):
        print 'hello'
```

编写setup文件

```
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["a.py"]))
```

编译

```
python3 setup.py build_ext
python3 setup.py build_ext --inplace # 在当前目录生成目标文件

# win=>pyd, linux=>so
```

使用

进入 /root/tmp/build/lib.linux-x86_64-3.5

```
from a import A
A().say()
```

注意

1. 内置变量__name__之类可能会有问题
2. 要用同版本py才能运行
