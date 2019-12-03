

生成单个pyc文件
```shell
python -m foo.py
```

通过代码来生成pyc文件。
```python
import py_compile
py_compile.compile('/path/to/foo.py')
```

批量生成pyc文件,针对一个目录下所有的py文件进行编译。
```python
import compileall
compileall.compile_dir(r'/path')
```

-------

反编译
```shell
pip install uncompyle
```

使用方法
我使用pip在mac os上安装好后的可执行文件名叫uncompyle6，很奇葩有没有
```
# 查看帮助
uncompyle6 --help 
# 将models.pyc反编译成py文件
uncompyle6 models.pyc > models.py 
# 将当前文件夹中所有的pyc文件反编译成后缀名为.pyc_dis的源文件
uncompile -o . *.pyc 
```
