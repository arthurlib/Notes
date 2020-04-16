中文文档: https://www.rddoc.com/doc/Supervisor/3.3.1/zh/

官方文档: http://supervisord.org/


> 安装

1. pip 安装(需安装有pip ,推荐):

```shell script
pip install supervisor
```

Debian / Ubuntu可以直接通过apt安装:

```shell script
apt-get install supervisor
```

> 配置文件

通过pip安装后 ,需要生成配置文件

```shell script
mkdir -p /root/etc/supervisor/supervisord.d
mkdir -p /root/etc/supervisor/log
echo_supervisord_conf > /root/etc/supervisor/supervisord.conf
```

使用apt-get安装后 ,supervisor的主配置文件在:

```shell script
/etc/supervisor/supervisord.conf 
```

> 主配置文件修改

修改supervisord.conf

```shell script
# 配置 子配置文件目录,可以是相对于主配置文件的相对路径
[include]
files = /root/etc/supervisor/supervisord.d/*.ini

# 配置 supervisord日志位置,可以是相对于主配置文件的相对路径
[supervisord]
logfile=/root/etc/supervisor/supervisord.log  ; (main log file;default $CWD/supervisord.log)
```

> 启动

```shell script
supervisord 
# supervisor 默认在以下路径查找配置文件:
# /usr/etc/supervisord.conf, 
# /usr/supervisord.conf,
# supervisord.conf, 
# etc/supervisord.conf, 
# /etc/supervisord.conf, 
# /etc/supervisor/supervisord.conf

# 指定主配置文件
supervisord -c /root/etc/supervisor/supervisord.conf
```



> supervisord

```shell script
supervisord -h

# -c/--configuration FILENAME ;指定配置文件
# -n/--nodaemon               ;运行在前台(调试用)
# -v/--version                ;打印版本信息
# -u/--user USER              ;以指定用户(或用户ID)运行
# -m/--umask UMASK            ;指定子进程的umask ,默认是022
# -l/--logfile FILENAME       ;指定日志文件
# -e/--loglevel LEVEL         ;指定日志级别
```

> supervisorctl

supervisorctl 管理

```shell script
# 同样需要读取主配置,所以:
cd /root/etc/supervisor
# 或者
supervisorctl -c /root/etc/supervisor/supervisord.conf
```

```shell script
supervisorctl  help

# reload         ;重新加载配置文件
# update         ;将配置文件里新增的子进程加入进程组 ,如果设置了autostart=true则会启动新增的子进程
# status         ;查看所有进程状态
# status <name>  ;查看指定进程状态
# start all      ;启动所有子进程
# start <name>   ;启动指定子进程
# restart all    ;重启所有子进程
# restart <name> ;重启指定子进程
# stop all       ;停止所有子进程
# stop <name>    ;停止指定子进程
# reload         ;重启supervisord
# add <name>     ;添加子进程到进程组
# reomve <name>  ;从进程组移除子进程 ,需要先stop。移除后 ,需要使用reread和update才能重新运行该进程
```

> 主配置文件

```shell script
[unix_http_server]
file=/tmp/supervisor.sock   ;UNIX socket 文件 ,supervisorctl 会使用
;chmod=0700                 ;socket文件的mode ,默认是0700
;chown=nobody:nogroup       ;socket文件的owner ,格式:uid:gid
 
;[inet_http_server]         ;HTTP服务器 ,提供web管理界面
;port=127.0.0.1:9001        ;Web管理后台运行的IP和端口 ,如果开放到公网 ,需要注意安全性
;username=user              ;登录管理后台的用户名
;password=123               ;登录管理后台的密码
 
[supervisord]
logfile=/tmp/supervisord.log ;日志文件 ,默认是 $CWD/supervisord.log
logfile_maxbytes=50MB        ;日志文件大小 ,超出会rotate ,默认 50MB ,如果设成0 ,表示不限制大小
logfile_backups=10           ;日志文件保留备份数量默认10 ,设为0表示不备份
loglevel=info                ;日志级别 ,默认info ,其它: debug,warn,trace
pidfile=/tmp/supervisord.pid ;pid 文件
nodaemon=false               ;是否在前台启动 ,默认是false ,即以 daemon 的方式启动
minfds=1024                  ;可以打开的文件描述符的最小值 ,默认 1024
minprocs=200                 ;可以打开的进程数的最小值 ,默认 200
 
[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ;通过UNIX socket连接supervisord ,路径与unix_http_server部分的file一致
;serverurl=http://127.0.0.1:9001 ; 通过HTTP的方式连接supervisord
 
; [program:xx]是被管理的进程配置参数 ,xx是进程的名称
[program:xx]
command=/opt/apache-tomcat-8.0.35/bin/catalina.sh run  ; 程序启动命令
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出 ,就表示进程正常启动了 ,默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值:[unexpected,true,false] ,默认为unexpected ,表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数 ,默认是3
user=tomcat          ; 用哪个用户启动进程 ,默认是root
priority=999         ; 进程启动优先级 ,默认999 ,值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout ,默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小 ,默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数 ,默认是10
; stdout 日志文件 ,需要注意当指定目录不存在时无法正常启动 ,所以需要手动创建目录(supervisord 会自动创建日志文件)
stdout_logfile=/opt/apache-tomcat-8.0.35/logs/catalina.out
stopasgroup=false     ;默认为false,进程被杀死时 ,是否向这个进程组发送stop信号 ,包括子进程
killasgroup=false     ;默认为false ,向进程组发送kill信号 ,包括子进程
 
;包含其它配置文件
[include]
files = relative/directory/*.ini    ;可以指定一个或多个以.ini结束的配置文件
```

```shell script
# 设置进程的log目录
[supervisord]
childlogdir=%(here)s/childlog    ; ('AUTO' child log dir, default $TEMP)
```
更多的看官网

> 子配置文件

编写一个配置文件,放在/root/etc/supervisor/supervisord.d/目录下,以.ini作为扩展名

示例

```shell script
[program:py_server]  ; 项目名
directory = /home    ; 程序的启动目录

; 启动命令,与命令行启动的命令是一样的
command = python3 -m http.server 8888
autostart = false    ; 在 supervisord 启动的时候也自动启动
startsecs = 5        ; 启动 5 秒后没有异常退出,就当作已经正常启动了
autorestart = false  ; 程序异常退出后自动重启
startretries = 3     ; 启动失败自动重试次数,默认是 3

user=root        ; 用哪个用户启动
priority=101     ; 优先级,越大越靠后

redirect_stderr = true         ; 把 stderr 重定向到 stdout,默认 false
stdout_logfile_maxbytes = 20MB ; stdout 日志文件大小,默认 50MB
stdout_logfile_backups = 20    ; stdout 日志文件备份数

; stdout 日志文件,需要手动创建目录,也可相对主配置文件的路径
stdout_logfile = /etc/supervisord.d/log/confd.log   

;重定向了就不需要了
; stderr 日志文件,需要手动创建目录,也可相对主配置文件的路径
;stderr_logfile = /etc/supervisord.d/log/confd.log
```
