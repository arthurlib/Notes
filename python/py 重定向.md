重定向写入文件内容

```python
f = open('test.txt',"w")
print("sfasf", file=f)
print("1234", file=f)
f.close()
```

改变文件描述符
```python
import os
import sys


def freopen(f, mode, stream):
    oldf = open(f, mode)
    oldfd = oldf.fileno()
    newfd = stream.fileno()
    os.close(newfd)
    os.dup2(oldfd, newfd)
    # print("")

freopen("t00.py", 'a', sys.stdout)
freopen("t00.py", 'a', sys.stderr)
print("fsfajsfjklasf")


```
