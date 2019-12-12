#### Linux 设置开机启动项的几种方法

> 方法一：编辑rc.loacl脚本

```
Ubuntu开机之后会执行/etc/rc.local文件中的脚本。

所以我们可以直接在/etc/rc.local中添加启动脚本。

$ vim /etc/rc.local
```

> 方法二：添加一个开机启动服务。

```
# 将你的启动脚本复制到 /etc/init.d目录下，并设置脚本权限, 假设脚本为test

mv test /etc/init.d/test
sudo chmod 755 /etc/init.d/test

# 将该脚本放倒启动列表中去

cd /etc/init.d
sudo update-rc.d test defaults 95

# 注：其中数字95是脚本启动的顺序号，按照自己的需要相应修改即可。
# 在你有多个启动脚本，而它们之间又有先后启动的依赖关系时你就知道这个数字的具体作用了。

# 将该脚本从启动列表中剔除
$ cd /etc/init.d
$ sudo update-rc.d -f test remove
```

> 方法三

```
# crontab 也可以设置开机自启
crontab -e 
@reboot /home/user/test.sh
```


#### 每次登录自动执行

也可以设置每次登录自动执行脚本，在/etc/profile.d/目录下新建sh脚本,  
/etc/profile会遍历/etc/profile.d/*.sh

另外，几个脚本的区别： 

> 系统级别

* /etc/profile 是所有用户的环境变量
* /etc/enviroment是系统的环境变量

1. /etc/profile: 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行. 并从/etc/profile.d目录的配置文件中搜集shell的设置。
2. /etc/bashrc 或 /etc/bash.bashrc: 为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取（即每次新开一个终端，都会执行bashrc）。

> 用户级别

1. \~/.bash_profile 或 \~/.profile: 每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该文件仅仅执行一次。默认情况下,设置一些环境变量,执行用户的.bashrc文件。
2. \~/.bashrc: 该文件包含专用于你的bash shell的bash信息,当登录时以及每次打开新的shell时,该该文件被读取。
3. \~/.bash_logout: 当每次退出系统(退出bash shell)时,执行该文件. 另外,/etc/profile中设定的变量(全局)的可以作用于任何用户,而\~/.bashrc等中设定的变量(局部)只能继承 /etc/profile中的变量,他们是”父子”关系。

> 补充

1. \~/.bash_profile: 是交互式、login 方式进入 bash 运行的
2. \~/.bashrc 是交互式 non-login 方式进入 bash 
> 通常二者设置大致相同，所以通常前者会调用后者

#### 登录linux时的执行顺序

在登录Linux时

1. 首先启动 /etc/profile 文件，

2. 然后再启动用户目录下的 \~/.bash_profile、 \~/.bash_login或 \~/.profile文件中的其中一个  
(根据不同的linux操作系统的不同，命名不一样),  
执行的顺序为：\~/.bash_profile、 \~/.bash_login、 \~/.profile。  
\~/.profile 或者 \~/.bash_profile 还会执行 \~/.bashrc，\~/.bashrc 一般还会 调用 /etc/bashrc

3. 在退出shell时，还会执行 \~/.bash_logout文件

* /etc/profile ->/etc/enviroment -->$HOME/.profile -->$HOME/.env

> 重新加载 .sh 文件

```
. t.sh
source t.sh
```
