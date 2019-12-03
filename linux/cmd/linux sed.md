> Linux sed 命令是利用脚本来处理文本文件。  
sed 可依照脚本的指令来处理、编辑文本文件。  
Sed 主要用来自动编辑一个或多个文件、简化对文件的反复操作、编写转换程序等

语法:
sed [-hnV][-e<script>][-f<script文件>][文本文件]

> gsed -n '/a/p' a

参数说明:
* -e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件。  
（-e : 可以在同一行里执行多条命令,不加的话写了多个只执行第一个）
* -f<script文件>或--file=<script文件> 以选项中指定的script文件来处理输入的文本文件。
* -h或--help 显示帮助。
* -n或--quiet或--silent 仅显示script处理后的结果。
* -V或--version 显示版本信息。


动作说明:
* a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)
* c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行
* d ：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；
* i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；
* p ：打印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～
* s ：取代，可以直接进行取代的工作,通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g


```
删除行
# 将 /etc/passwd 的内容列出并且列印行号，同时，请将第 2~5 行删除
nl /etc/passwd | sed '2,5d'
#只要删除第 2 行
nl /etc/passwd | sed '2d'
#要删除第 3 到最后一行
nl /etc/passwd | sed '3,$d'


添加行
#在第二行后(亦即是加在第三行)加上『drink tea?』字样
nl /etc/passwd | sed '2a drink tea'
#那如果是要在第二行前
nl /etc/passwd | sed '2i drink tea' 
#增加两行以上，每一行之间都必须要以反斜杠'\'来进行新行的添加
nl /etc/passwd | sed '2a Drink tea or ......\
> drink beer ?'


替换与显示(以行为单位)
#将第2-5行的内容取代成为『No 2-5 number』
nl /etc/passwd | sed '2,5c No 2-5 number'
#仅列出 /etc/passwd 文件内的第 5-7 行
nl /etc/passwd | sed -n '5,7p'


数据的搜索并显示
#搜索 /etc/passwd有root关键字的行
nl /etc/passwd | sed '/root/p'
#如果root找到，除了输出所有行，还会输出匹配行
#使用-n的时候将只打印包含模板的行
nl /etc/passwd | sed -n '/root/p'


数据的搜寻并删除
#删除/etc/passwd所有包含root的行，其他行输出
nl /etc/passwd | sed  '/root/d'


数据的搜寻并执行命令
#搜索/etc/passwd,找到root对应的行，
#执行后面花括号中的一组命令，每个命令之间用分号分隔，
#这里把bash替换为blueshell，再输出这行,s替换;结尾，最后的q是退出
nl /etc/passwd | sed -n '/root/{s/bash/blueshell/;p;q;}'

# 加上 g 表示全部完全匹配
# sed 's/要被取代的字串/新的字串/g'
/sbin/ifconfig eth0 | grep 'inet addr' | sed 's/^.*addr://g' | sed 's/Bcast.*$//g'


多点编辑,-e表示多点编辑
# 一条sed命令，删除/etc/passwd第三行到末尾的数据，并把bash替换为blueshell
nl /etc/passwd | sed -e '3,$d' -e 's/bash/blueshell/'


直接修改文件内容，-i 选项
sed -i '$a # This is a test' regular_express.txt
```

> 报错：command a expects \ followed by text

```
参数“i”的用途是直接在文件中进行替换。
为防止误操作带来灾难性的后果，sed在替换前可以自动对文件进行备份，前提是需要提供一个后缀名。
从上面对参数“i”的详细说明中可以看到，mac osx下是强制要求备份的（当然也可以使用空字符串来取消备份），
但centos下是可选的。

如果不需要备份文件，mac osx下可以使用如下命令完成替换操作：

sed -i '' 's/oldstring/newstring/g' full-path-file
```


> 报错：command a expects \ followed by text

```
原因: macos 用sed命令做插入等命令会爆这个错，主要是因为mac的sed命令有点老

解决方法1：
在你敲完sed -n '5a  之后 敲一个反斜杠 换行然后输入其余的命令

解决方法2(推荐)：
brew install gnu-sed   用gnu的sed（centos版本的sed）
安装下来后为指令为 gsed
```

