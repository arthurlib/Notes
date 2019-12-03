[https://www.cnblogs.com/kaiye/p/6275207.html](https://www.cnblogs.com/kaiye/p/6275207.html)

[http://louiszhai.github.io/2017/09/30/tmux/](http://louiszhai.github.io/2017/09/30/tmux/)

> 会话操作

```
tmux [new -s 会话名 -n 窗口名]  #启动新会话
tmux at [-t 会话名]  #恢复会话
tmux ls  #列出所有会话
tmux kill-session -t 会话名  #关闭会话
tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1  #关闭所有会话

```

进入tmux后

>会话操作
```
ctrl+b,
:new<回车>  # 启动新会话
ctrl+b,s    # 列出所有会话
ctrl+b,$    # 重命名当前会话
ctrl+b,d   #退出 tmux（tmux 仍在后台运行）
ctrl+b,t   #窗口中央显示一个数字时钟
ctrl+b,?   #列出所有快捷键
ctrl+b,:   #命令提示符
```

> 窗口操作

```
ctrl+b,c  创建新窗口
ctrl+b,w  列出所有窗口
ctrl+b,n  后一个窗口
ctrl+b,p  前一个窗口
ctrl+b,f  查找窗口
ctrl+b,,  重命名当前窗口
ctrl+b,&  关闭当前窗口

# 调整窗口排序
:swap-window -s 3 -t 1  #交换3号和1 号窗口
:swap-window -t 1   #交换当前和 1 号窗口
:move-window -t 1   #移动当前窗口到 1 号

# 同步窗格
:setw synchronize-panes  
```

> 窗格操作

```
# 分割窗口
ctrl+b,%  #  垂直分割
ctrl+b,"  #  水平分割
ctrl+b,o  #  交换窗格
ctrl+b,x  #  关闭窗格
ctrl+b,⍽  #  左边这个符号代表空格键 - 切换布局
ctrl+b,q  # 显示每个窗格是第几个，当数字出现的时候按数字几就选中第几个窗格
ctrl+b,{  # 与上一个窗格交换位置
ctrl+b,}  # 与下一个窗格交换位置
ctrl+b,z  # 切换窗格最大化/最小化

# 同步窗格
:setw synchronize-panes

# 调整窗格尺寸，PREFIX == ctrl+b
PREFIX : resize-pane -D          #当前窗格向下扩大 1 格
PREFIX : resize-pane -U          #当前窗格向上扩大 1 格
PREFIX : resize-pane -L          #当前窗格向左扩大 1 格
PREFIX : resize-pane -R          #当前窗格向右扩大 1 格
PREFIX : resize-pane -D 20       #当前窗格向下扩大 20 格
PREFIX : resize-pane -t 2 -L 20  #编号为 2 的窗格向左扩大 20 格
```

> 文本复制模式

```
PREFIX-[  #进入文本复制模式
PREFIX-]  #粘贴文本

按下 PREFIX-[ 进入文本复制模式。可以使用方向键在屏幕中移动光标。
默认情况下，方向键是启用的。在配置文件中启用 Vim 键盘布局来切换窗口、调整窗格大小。Tmux 也支持 Vi 模式。
要是想启用 Vi 模式，只需要把下面这一行添加到 .tmux.conf 中：

setw -g mode-keys vi

启用这条配置后，就可以使用 h、j、k、l 来移动光标了。

想要退出文本复制模式的话，按下回车键就可以了。
然后按下 PREFIX-] 粘贴刚才复制的文本。

一次移动一格效率低下，在 Vi 模式启用的情况下，
可以辅助一些别的快捷键高效工作。

例如，可以使用 w 键逐词移动，使用 b 键逐词回退。
使用 f 键加上任意字符跳转到当前行第一次出现该字符的位置，使用 F 键达到相反的效果。

vi             emacs        功能
^              M-m          反缩进
Escape         C-g          清除选定内容
Enter          M-w          复制选定内容
j              Down         光标下移
h              Left         光标左移
l              Right        光标右移
L                           光标移到尾行
M              M-r          光标移到中间行
H              M-R          光标移到首行
k              Up           光标上移
d              C-u          删除整行
D              C-k          删除到行末
$              C-e          移到行尾
:              g            前往指定行
C-d            M-Down       向下滚动半屏
C-u            M-Up         向上滚动半屏
C-f            Page down    下一页
w              M-f          下一个词
p              C-y          粘贴
C-b            Page up      上一页
b              M-b          上一个词
q              Escape       退出
C-Down or J    C-Down       向下翻
C-Up or K      C-Up         向下翻
n              n            继续搜索
?              C-r          向前搜索
/              C-s          向后搜索
0              C-a          移到行首
Space          C-Space      开始选中
               C-t          字符调序
```

