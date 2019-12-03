[https://www.ibm.com/developerworks/cn/linux/l-cn-screen/index.html](https://www.ibm.com/developerworks/cn/linux/l-cn-screen/index.html)

> 会话操作

```
screen  # 创建会话，直接键入screen,启动默认shell
screen -S yourname   # 新建叫yourname的session
screen -r yourname   # 恢复离线的screen作业.
screen -d yourname   # 离线某个screen作业.
screen -d -r test  # 强制将这个会话从它所在的终端分离，转移到新的终端上来
screen vi test  # 创建会话，Screen命令后跟你要执行的程序，退出vi时同时退出screen会话
screnn -d -m  # 启动一个开始就处于断开模式的会话,可以跟 -S 参数
-m  # 即使目前已在作业中的screen作业，仍强制建立新的screen作业。
-x  # 恢复之前离线的screen作业
screen -d -r yourname #  结束当前session并回到yourname这个session
screen -ls    # 查看会话列表
screen -r id  # 重新连接

kill id  # 直接杀死会话
kill -9 id  # 杀死会话，会话状态变dead
screen -wipe  # 清除状态为dead的会话


```

> 窗口操作

```
ctrl+a,c  # 创建一个新的运行shell的窗口并切换到该窗口
ctrl+a,d    # 暂时断开当前会话
Ctrl+a,?	# 显示所有键绑定信息
Ctrl+a,w	# 显示所有窗口列表
Ctrl+a,Ctrl-a	# 切换到之前显示的窗口
Ctrl+a,n	# 切换到下一个窗口
Ctrl+a,p	# 切换到前一个窗口(与C-a n相对)
Ctrl+a [Space] #  由视窗0循序切换到视窗9
Ctrl+a,0..9	# 切换到窗口0..9
Ctrl+a,a	# 发送 C-a到当前窗口
Ctrl+a,k	# 杀掉当前窗口
Ctrl+a,[	# 进入拷贝/回滚模式
Ctrl+a,]   # 粘贴screen剪贴板中的内容
Ctrl+a,x   # 锁住当前的 window, 需用用户密码解锁
1. 忘记screen会话密码;要么想起来密码，要么kill掉该会话吧；
2. 想换screen会话密码;按下 Ctrl-a 然后再输入 :password 命令，连续输入2次新密码,重新进入即可
Ctrl+a,s  # 锁定会话。锁定以后，再进行任何输入屏幕都不会再有反应了。但是要注意虽然屏幕上看不到反应，但你的输入都会被Screen中的进程接收到。
Ctrl+a,q可以解锁一个会话。
Ctrl+a,A    #为当前窗口重命名
Ctrl+a,C    #Clear the screen.
Ctrl+a,S    # 水平分割窗口(分为上下两块).
Ctrl+a,|    # 竖直分割窗口(分为左右两块)
# 新分割出的块跳转过来后需要用Ctrl+a,c来创建新shell.
    Ctrl+a,<Tab>   # 在分割的各块中跳转. 
    Ctrl+a,X       # 关闭分割的块.

C-a t # Time，显示当前时间，和系统的 load 


复制模式

C-a [ : 进入 copy mode，在 copy mode 下可以回滚、搜索、复制就像用使用 vim 一样
    C-b   : Backward，PageUp 
    C-f   : Forward，PageDown 
    H     : (大写) High，将光标移至左上角 
    L     : Low，将光标移至左下角 
    0     : 移到行首 
    $     : 行末 
    w     : forward one word，以字为单位往前移 
    b     : backward one word，以字为单位往后移 
    Space : 第一次按为标记区起点，第二次按为终点 (类似于vim的v选择)
    Esc   : 结束 copy mode 
C-a ] : Paste，把刚刚在 copy mode 选定的内容贴上

```

> 窗格操作

```
CTRL+a,|  # 纵向分割
CTRL+a,S  #  横向分割
CTRL+a，c，#，分割后要，创建新的窗口才能使用
CTRL+a,TAB  # 切换窗格
Ctrl+a,X  #关闭当前焦点所在的屏幕区块
Ctrl+a,Q  #关闭除当前区块之外其他的所有区块

```

> 会话共享

```
screen -x name/id  # 创建一个screen会话，另一个终端上输入

启用共享，不同用户
在当前screen会话窗口按Ctrl + a ,输入冒号：，在冒号后输入multiuser on,回车，就打开了多用户共享开关
授权
授权用户B能够连接A共享的会话：在当前screen会话窗口按Ctrl + a ,输入冒号：，在冒号后输入acladd B,回车即可
```

> 脚本

```
向screen中正在运行的程序发送按键消息
比如screen中正在运行程序top，此时我想从另一个终端中向此screen中的top程序发送终止命令q
# 新建一个名为top的screen并在其中运行top命令
[root@localhost ~]# screen -S top
[root@localhost ~]# top

# 在另一个终端中运行下列指令，然后发现上述top进程终止了
[root@localhost ~]# screen -S top -X stuff "q"
# or
[root@localhost ~]# screen -S top -X stuff "^C"
# 当然也可以发送回车键
[root@localhost ~]# screen -S top -X stuff "^M"



在screen中启动程序
比如，我想在脚本中在某个screen中启动top进程
# 一定要带$，一定要使用单引号
[root@localhost ~]# screen -S top -X stuff $'top\n'
# or
[root@localhost ~]# screen -S top -X stuff "top^M"


如果我们直接在脚本里写 screen -S my_screen, 会导致脚本无法继续执行。为了使脚本执行下去，创建screen的具体代码如下：

screen_name=$"my_screen"
screen -dmS $screen_name
现在，我们就已经创建了一个名为 my_screen 的窗口。然后，我们需要向其发送具体的命令。我们用如下命令：
cmd=$"java Test";
screen -x -S $screen_name -p 0 -X stuff "$cmd"
screen -x -S $screen_name -p 0 -X stuff $'\n'

6.3 发送命令到screen会话

在Screen会话之外，可以通过screen命令操作一个Screen会话，这也为使用Screen作为脚本程序增加了便利。关于Screen在脚本中的应用超出了入门的范围，这里只看一个例子，体会一下在会话之外对Screen的操作：

[root@TS-DEV ~]# screen -S sandy -X screen ping www.baidu.com
这个命令在一个叫做sandy的screen会话中创建一个新窗口，并在其中运行ping命令。
```
