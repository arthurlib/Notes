
# \_\_main__文件

> '__main__' 是顶层代码执行的作用域的名称。模块的 __name__ 在通过标准输入、脚本文件或是交互式命令读入的时候会等于 '__main__'。

> 模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行一些代码，而在被 import 时不会执行。

> 当通过python -m package 语句执行时，python 会先执行 __init__.py ，然后执行__main__.py

```
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

    
> **对软件包来说，通过加入 __main__.py 模块可以达到同样的效果，当使用 -m 运行模块时，其中的代码会被执行。**


# \_\_init__文件

> 在导入一个包时，实际上是导入了它的__init__.py文件。这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入


```
# package
# __init__.py
import re
import urllib
import sys
import os
# a.py
import package
print(package.re, package.urllib, package.sys, package.os)
```

> init.py中还有一个重要的变量，all, 它用来将模块全部导入

> 当使用 from package import *语句时，主程序只能获得__all__中的属性

> 如果想在__all__列表中填写下几级的包（或者模块、模块中的属性），需要先在__init__.py将该包（或者模块、模块中的属性）导入才能使用

> 如果没有定义__all__，通过 from package import * 语句导入时，主程序可以获得在__init__.py定义的属性

```
# __init__.py
__all__ = ['os', 'sys', 're', 'urllib']
# a.py
from package import *
```


> 可以被import语句导入的对象是以下类型：

- 模块文件（.py文件）
- C或C++扩展（已编译为共享库或DLL文件）
- 包（包含多个模块）
- 内建模块（使用C编写并已链接到Python解释器中）

> 关于.pyc 文件 与 .pyo 文件  
> py文件的汇编,只有在import语句执行时进行，当.py文件第一次被导入时，它会被汇编为字节代码，并将字节码写入同名的.pyc文件中。后来每次导入操作都会直接执行.pyc 文件（当.py文件的修改时间发生改变，这样会生成新的.pyc文件），在解释器使用-O选项时，将使用同名的.pyo文件，这个文件去掉了断言（assert）、断行号以及其他调试信息，体积更小，运行更快。（使用-OO选项，生成的.pyo文件会忽略文档信息）

> 导入模块  

模块通常为单独的.py文件，可以用import直接引用，可以作为模块的文件类型有.py、.pyo、.pyc、.pyd、.so、.dll
