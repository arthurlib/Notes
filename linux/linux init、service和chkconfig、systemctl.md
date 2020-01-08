[[Linux]systemd和sysV](https://www.cnblogs.com/aaronLinux/p/10654523.html)

[init 维基](https://zh.wikipedia.org/wiki/Init)

### service

> service命令用于对系统服务进行管理，比如启动（start）、停止（stop）、重启（restart）、重新加载配置（reload）、查看状态（status）等。

> service 命令实际上是调用了/etc/init.d 目录下的shell脚本

```bash
# 例子
service nginx start
service nginx stop
service nginx restart 
```

[LBS风格](https://www.cnblogs.com/boodoog/p/5844827.html)

```bash
# LBS风格示例
#!/bin/bash  
### BEGIN INIT INFO
# Provides:          zhuzhenyuan.cn
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: nginix service
# Description:       nginix service daemon
### END INIT INFO 
# LSB tags规范，上面这段内容有，就可以支持 systemctl enable nginx.service，或者直接 apt-get remove insserv

DAEMON=/usr/local/nginx/sbin/nginx
case "$1" in
    start)
        echo "Starting nginx daemon..."
        $DAEMON && echo "NGINX RUN SUCCESS"
    ;;
    stop)
        echo "Stopping nginx daemon..."
        $DAEMON -s stop && echo "NGINX STOP SUCCESS"
    ;;
    quit)
        echo "Stopping nginx daemon..."
        $DAEMON -s quit && echo "NGINX QUIT SUCCESS"
    ;;
    reload)
        echo "Reloading nginx daemon..."
        $DAEMON -s reload && echo "NGINX RELOAD SUCCESS"
    ;;
    restart)
        echo "Restarting nginx daemon..."
        $DAEMON -s quit
        $DAEMON && echo "RESTARTING NGINX SUCCESS"

    ;;
    *)
        echo "Usage: dervice nginx{start|stop|quit|restart|reload}"
        exit 2
    ;;
esac
```

### chkconfig

> 提供了一个维护/etc/rc[0~6] d 文件夹的命令行工具，它减轻了系统直接管理这些文件夹中的符号连接的负担。

> chkconfig主要包括5个原始功能：
1. 为系统管理增加新的服务、  
1. 为系统管理移除服务、  
1. 列出单签服务的启动信息、  
1. 改变服务的启动信息和检查特殊服务的启动状态。  
1. 当单独运行chkconfig命令而不加任何参数时，他将显示服务的使用信息。  
> 必要参数 
- –add 开启指定的服务程序 
- –del 关闭指定的服务程序 
- –list 列出chkconfig所知道的所有服务

> 选择参数 
- –level<代号> 设置服务程序的等级代号，它是一串0~7的数字，如“-level35”代表指定运行等级3和5 
- –help 显示帮助信息 
- –version 显示版本信息


### systemctl(推荐)

systemd系统
1. systemd是一个取代了SysV和LSB的初始化系统；
1. 现在的大多数Linux发行版本都进行了这个更新；
1. systemd不仅仅只是个初始化系统，它还包括了还包括了管理系统各种的方面的 daemon；


> 可以把systemctl理解为systemd的一个工具。也可以认为systemctl命令将service和chkconfig命令结合在了一起

```bash
# 查看systemctl的相关信息
systemctl --version
whereis systemctl

# 列出所有可用单元
systemctl list-unit-files

# 列出所有运行中单元
systemctl list-units

# 列出所有失败的单元
systemctl --failed

# 检查某个单元是否启用
systemctl is-enabled mysqld.service

# 查看某个服务（单元）的状态
systemctl status firewalld.service

# 启动、重启、停止、重载服务
systemctl start httpd.service
systemctl restart httpd.service
systemctl stop httpd.service
systemctl reload httpd.service
systemctl status httpd.service


# 激活/禁止自动启动
systemctl enable httpd.service
systemctl disable httpd.service

# 杀死服务
systemctl kill httpd

# 注销/取消注销
systemctl mask nginx.service	#注销 unit,注销后就无法启动该unit
systemctl unmask nginx.service	#取消对 unit 的注销。
```
