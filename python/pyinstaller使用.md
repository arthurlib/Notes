# pyinstaller使用


> pyinstaller将py文件打包为可执行文件  
改可执行文件自包含不需要安装py，就是执行速度比较慢  
win 生成exe文件, 支持linux，mac  

## 安装

```
pip install pyinstaller
```
## 使用

```
# 以win为例

pyinstaller -F -w -i manage.ico t.py

# -F：打包为单文件
# -w：Windows程序，不显示命令行窗口
# -i：是程序图标，
# t.py 要打包的py文件
```
# 注意

> 如果打包的代码中涉及目录操作，  
打包出可执行文件后如果不是在文件所在目录执行的会出现未预期的结果  
或者路径都用绝对路径


可参考下面代码 在运行时得到相对于执行文件的路径
```
import sys
import os
print(sys.path[0])
print(sys.argv[0])
print(os.path.dirname(os.path.realpath(sys.executable)))
print(os.path.dirname(os.path.realpath(sys.argv[0])))
```


## pyinstaller将py文件打包mac

> 在mac上使用时会有依赖包的问题，参考如下

```
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' run.py

```
