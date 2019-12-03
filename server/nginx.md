# 简介

* Apache  
Apache(Apache HTTP Server ）是目前广泛流行的Web 服务器软件，具有开放源代码、跨平台、安全稳定等特点。Apache 是伴随五联网的兴起共同成长的，经过多年的技术沉淀和积累，已经非常成熟和稳定，具备了大量的功能模块和扩展。但由于Apache 在设计之初对性能和资源的消耗没有过多的关注，导致在应对高并发的业务场景时，被一些轻量级的高性能Web 服务器赶超。


* Tomcat  
Tomcat(Apache Tomcat ）主要用于Java Web 环境，是一个运行Serviet 和JSP 的容器
（即运行Java 语言的服务器端程序） 。Tomcat 和Apache 都是由Apache 软件基金会运作的开源项目， Tomcat 本身可作为一个单独的Web 服务器使用，主要用于处理动态请求， 但在静态资源和高并发方面的性能较弱，因此经常和Apache 等软件搭配，实现动静态请求分离。


* Nginx  
Nginx （读作engine x ）是一个轻量级开源Web 服务器软件，可以作为反向代理、负载均衡与缓存服务器使用。Nginx 和Lighttpd 都是为高并发网站的应用场景而设计的。随着技术发展和业务需要， Nginx 逐渐受到关注，在国内如百度、淘宝、腾讯、新浪、网易等网站都开始使用Nginx 来满足一些高并发访问的需求。


* Lighttpd
* Microsoft IIS

# 安装
***系统环境*：阿里云 ubuntu16**

## 1、下载
> 下载地址  
[nginx_down](http://nginx.org/en/download.html)

目前Nginx 发布了3 种类型的版本，分别为  
Mainline version （开发版）  
Stable version（稳定版）  
Legacy versions （早期版本）  
每种类型的版本中又提供了Linux 版本和Windows 版本


> 下载解压后，目录结构如下
* src 目录：存放Nginx 的源代码。
* man 目录：存放Nginx 的帮助文档。
* html 目录：存放默认网站文件。
* contrib 目录：存放其他机构或组织贡献的文档资料。
* conf 目录：存放Nginx 服务器的配置文件。
* auto 目录：存放大量的脚本文件,和configure 脚本程序相关。
* configure 文件： Nginx 自动安装脚本，用于检查环境，生成编译代码需要的makefile文件。
* CHANGES 、CHANGES.ru 、LICENSE 和README 都是Nginx 服务器的相关文档资料。

## 2、安装依赖
> nginx编译安装依赖包

软件包 | 说明
---|---
pcre-devel|为Nginx 模块（如rewrite ）提供正则表达式库
zlib-devel|为Nginx 模块（如gzip ） 提供数据压缩用的共享库
openssl-dlevel|为Nginx 模块（如ssD 提供密码~法、证书以及SSL 协议等功能

> Linux 中的某些软件包具有devel 包和非devel 包两种形式，如zlib 和zlib-devel。非devel 包就是普通的软件包，而devel 包则一般会包括头文件、静态库甚至源码。若仅仅使用这些软件，则仅安装非devel 包即可，但若在开发时常妥用到这些软件包中的共享库，就需要安装devel 包。

## 3、编译安装
> 安装脚本
```bash
#!/bin/bash

apt update
# 安装依赖
# centos
# yum -y install pcre-devel openssl-devel
# ubuntu
apt install openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev

#下载
wget http://nginx.org/download/nginx-1.14.2.tar.gz
#解压
tar -zxvf nginx-1.14.2.tar.gz
cd nginx-1.14.2

# 设置编译选项
./configure --prefix=/usr/local/nginx --with-http_ssl_module
#编译安装
make && make install
```

## 4、启动和停止

> 启动
```bash
cd /usr/local/nginx/sbin
./nginx

# 查看运行装态
ps aux | grep nginx
```

> 停止


```bash
# 快速关闭，不管有没有正在处理的请求
./nginx -s stop
# 优雅的关闭方式，Nginx在退出前完成已经接受的连接请求
./nginx -s quit

# 或者 杀进程
kill Nginx主进程PID（以root运行的进程） # 1
killall nginx  # 2
```


命令 | 说明
---|---
nginx -s reload| 在Nginx 已经启动的情况下重新加载配置文件（平滑重启）
nginx -s reopen| 重新打开日志文件
nginx -c /特定目录/nginx.conf | 以特定目录下的配置文件启动Nginx
nginx -t | 检测当前配置文件是否正确
nginx - t -c /特定日录/nginx.conf | 检测特定目录下的Nginx 配置文件是否正确
nginx - v | 显示版本信息
nginx -V | 显示版本信息和编译选项

> Nginx 的进程设计思想  
Nginx 由一个主进程和多个工作进程组成，主进程接收容户端请求，转交给工作进程处理，从而很好地利用多核心CPU 的计算能力。当管理员执行reload 命令重新加载配置时，主进程会等待工作进程完成工作后再结束工作进程，然后基于新的配直重新创建工作进程，避免了工作过程中被打断的情况。由于整个过程中主进程没有停止，因此也不会发生漏掉客户端请求的情况。


> 查看端口占用
```bash
# t 、l 、n 、p分别表示查看tcp协议、查看监昕服务、不解析名称以及显示进程名和PID
 netstat -tlnp
 ```
 
 > 防火墙开放80端口(不同系统可能不一样,此处centos,一个参考)
 
```bash
iptables -I INPUT -p tcp --dport 80 -j ACCEPT
# 查看端口状态
service iptables status
#保存，可以重启生效
service iptables save
# 重启
service iptables restart
```

参数 | 说明
---|---
-I INPUT | 表示在INPUTC 外部访问规则）中插入一条规则
-p tcp | 指定数据包匹配的协议(tcp 、udp 、icmp 等)，这里指定tcp 协议
--dport 80 | 用于指定数据包匹配的目标端口号，这里指定80 端口
-j ACCEPT | 指定对数据包的处理操作（ACCEPT、DROP、REJECt、REDIRECT等），这里指定ACCEPT 操作


# 5、其他操作

## 创建软链接
```bash
# 查看当前环境变量
echo $PATH
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
# 其中
# /bin 和 /sbin 放置常用程序， sbin 表示需要管理员权限
# /usr/bin 和 /usr/sbin 放置一些工具软件的可执行程序
# /usr/local/bin 和/usr/local/sbin 放置用户自行安装的可执行程序
# 因此，推荐将Nginx 放入/usr/local/sbin目录中。

# 利用软链接将nginx 程序链接到/usr/local/sbin 目录中，从而创建nginx命令
ln -s /usr/local/nginx/sbin/nginx /usr/local//sbin/nginx

```

## 添加到系统服务  
> 许多Linux 系统服务都可以通过service命令进行控制，service 命令实际上是调用了/etc/init.d 目录下的shell脚本


```bash
#例子
#直接执行脚本
/etc/init.d/network restart
#等价于 通过service 命令执行脚本
service network restart
```

> 接下来执行/etc/init.d/nginx 编写一个shell 脚本实现Nginx 服务管理，提供start 、stop 、quit、reload 、restart 5 个参数，具体代码如下。

参考： [LSB、服务](https://www.cnblogs.com/boodoog/p/5844827.html)
```bash
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

[systemctl、service、chkconfig]（https://blog.csdn.net/cds86333774/article/details/51165361
[服务systemctl 系统和服务管理器 参考](https://www.jb51.net/article/136559.htm)
```bash
# 添加权限
chmod u+x /etc/init.d/nginx

# unmask：取消对 unit 的注销。 
systemctl unmask nginx.service
# 添加服务到跟随系统启动，
systemctl enable nginx.service
```
> 现在就可以使用 service的方式执行了

> systemctl [command] [unit]

命令 | 说明
---|---
start|立刻启动后面接的 unit。
stop|立刻关闭后面接的 unit。
restart|立刻关闭后启动后面接的 unit，亦即执行 stop 再 start 的意思。
reload|不关闭 unit 的情况下，重新载入配置文件，让设置生效。
enable|设置下次开机时，后面接的 unit 会被启动。
disable|设置下次开机时，后面接的 unit 不会被启动。
status|目前后面接的这个 unit 的状态，会列出有没有正在执行、开机时是否启动等信息。
is-active|目前有没有正在运行中。
is-enable|开机时有没有默认要启用这个 unit。
kill |不要被 kill 这个名字吓着了，它其实是向运行 unit 的进程发送信号。
show|列出 unit 的配置。
mask|注销 unit，注销后你就无法启动这个 unit 了。
unmask|取消对 unit 的注销。

> linux 运行级别

* 运行级别0：系统停机状态，系统默认运行级别不能设为0，否则不能正常启动
* 运行级别1：单用户工作状态，root权限，用于系统维护，禁止远程登陆
* 运行级别2：多用户状态(没有NFS)
* 运行级别3：完全的多用户状态(有NFS)，登陆后进入控制台命令行模式
* 运行级别4：系统未使用，保留
* 运行级别5：X11控制台，登陆后进入图形GUI模式
* 运行级别6：系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动

运行级别的原理：
1. 在目录/etc/init.d下有许多服务器脚本程序，一般称为服务(service)
2. 在/etc下有7个名为rcN.d的目录，对应系统的7个运行级别, 存在rcS.d，为系统进入某个 runlevel 之前的 ) syetem init script
3. rcN.d目录下都是一些符号链接文件，这些链接文件都指向init.d目录下的service脚本文件，命名规则为K+nn+服务名或S+nn+服务名，其中nn为两位数字。
4. 系统会根据指定的运行级别进入对应的rcN.d目录，并按照文件名顺序检索目录下的链接文件
    * 对于以K开头的文件，系统将终止对应的服务
    * 对于以S开头的文件，系统将启动对应的服务
5. 查看运行级别用：runlevel
6. 进入其它运行级别用：init N
7. 另外init0为关机，init 6为重启系统



# 配置

打开conf下主配置文件查看
```bash
vim /usr/local/nginx/conf/nginx.conf
```
可看到主配置文件由5个块组成，如下
```bash
main
events{...}
http{
    server{
        location{...}
    }
}
```

块 | 说明
---|---
main |主要控制Nginx 子进程所属的用户和用户组、派生子进程数、错误日志位置与级别、pid 位置、子进程优先级、进程对应CPU 、进程能够打开的文件描述符数目等
events | 控制Nginx 处理连接的方式
http | Nginx 处理http 请求的主要配置块，大多数配置都在这里面进行
server | Nginx 中主机的配置块，可用于配置多个虚拟主机
location | server 中对应目录级别的控制块，可以有多个


> 查看默认的nginx.conf文件，去掉注释后

```bash
worker_processes  1;
events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;
        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;

        location = /50x.html {
            root   html;
        }

    }

}

```
> 默认配置指令


指令 | 说明
---|---
worker_processes |配置Nginx 的工作进程数， 一般设为CPU 总核数或者总核数的两倍
worker_connections |配置Nginx 允许单个进程并发连接的最大请求数
include |用于引人配置文件
default_type |设置默认文件类型
sendfile |默认值为on ，表示开启高效文件传输模式
keepalive_timeout |设置长连接超时时间（单位：秒）
listen |监听端口，默认监听80 端口
server_name |设置主机域名
root |设置主机站点根目录地址
index |指定默认索引文件
error_page |自定义错误页面


## 虚拟主机配置

### 基于端口号配置虚拟主机

查看nginx.conf文件，如下


``` bash
# another virtual host using mix of IP-, name-, and port-based configuration
# Nginx 中虚拟主机的配置可以基于IP地址、域名和端口号进行设置

#server {
#    listen       8000;  # 监昕端口，与下面一句二选一
#    listen       somename:8080;
#    server_name  somename  alias  another.alias;

#    location / {
#        root   html;
#        index  index.html index.htm;
#    }
#}
```

例子

```bash
# 配置监听8001 端口号的虚拟主机
server{
    listen 8001;
    server_name localhost;
    root html/html8001;
    index index.html index.htm;
}
# 配置监听8002 端口号的虚拟主机
server{
    listen 8002;
    server_name localhost;
    root html/html8002;
    index index.html index.htm;
}
```
平滑重启生效


### 基于域名配置虚拟主机

域名可以采用改host的方式进行测试

```
server{
    listen 80;
    server_name www.test.com;
    root htmlwwwtestcom;
    index index.html index.htm;
}
server{
    listen 80;
    server_name test.com;
    root htmltestcom;
    index index.html index.htm;
}
```

> server_name使用
```
# 以*通配符开始的字符串
server_name *.test.com;
# 以*通配符结束的字符串
server_name www.*;
# 匹配正则表达式
server_name ~^(?.+)\.domain\.com$;

# 优先级顺序依次为，精准匹自己〉以通配符开始的字符串〉〉正则表达式
```

## 反向代理、负载均衡配置

### 配置反向代理


```
#域名区分
server {
    listen 80;
    server_name www.test.com;
    # 域名www.test.com的请求全部转发到Web服务器192.168.78.128
    location / {
        proxy_pass http://192.168.11.12;
    }
}
server {
    listen 80;
    server_name test.com;
    # 域名www.test.com的请求全部转发到Web服务器192.168.78.128
    location / {
        proxy_pass http://192.168.11.11:8007;
    }
}
```

```
#端口区分
server {
    listen 801;
    server_name localhost;
    # 本地端口801的请求全部转发到Web服务器192.168.78.128
    location / {
        proxy_pass http://192.168.11.12;
    }
}
server {
    listen 802;
    server_name localhost;
    # 本地端口802的请求全部转发到Web服务器192.168.78.128
    location / {
        proxy_pass http://192.168.11.11:8007;
    }
}
```

其他常用指令

指令 | 说明
---|---
proxy_set_header | 在将客户端请求发送给后端服务器之前，更改来自客户端的请求头信息
proxy_connect_timeout |  配置Nginx与后端代理服务器尝试建立连接的超时时间
proxy_read_timeout | 配置Nginx向后端服务器组发出read请求后，等待响应的超时时间
proxy_send_timeout| 配置Nginx向后端服务器组发出write请求后，等待响应的超时时间
proxy_redirect |  用于修改后端服务器返回的响应头中的Location和Refresh

> proxy_set_header指令使用

```
# 配置实现将客户端IP 传递给后端服务器。
location / {
    proxy_pass http://192.168.78.200;
    proxy_set_header Host $host;  #第一个参数表示字段名称，第二个参数表示字段值
    proxy_set_header X-Real-p $ remote_addr;  #$remote_addr用于获取客户端真实的IP 地址
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # $proxy_add_x_forwarded_ for 用于在客户端请求头字段后添加客户端地址，使用逗号分隔，且当不存在客户端请求头字段时，该变量等同于变量$remote_addr 。
}
```

### 负载均衡配置

> 负载均衡（ load balance）就是将负载分摊到多个操作单元上执行,从而提高服务的可用性和响应速度，带给用户更好的体验。


通过使用upstream指令实现.

以下是4中典型的配置方式


配置方式 | 说明
---|---
轮询方式 | 负载均衡默认设置方式，每个请求按照时间顺序逐一分配到不同的后端服务器进行处理，如果有服务器宕机，会自动剔除
权重方式 | 利用weight 指定轮询的权重比率，与访问率成正比，用于后端服务器性能不均的情况
ip_hash 方式 | 每个请求按访问IP 的hash 结果分配，这样可以使每个访客固定访问一个后端服务器，可以解决Session 共享的问题
第三方模块 | 第三方模块采用fair 时，按照每台服务器的响应时间来分配请求，响应时间短的优先分配；若第三方模块采用url_hash 时，按照访问url 的hash 值来分配请求

#### 一般轮询负载均衡

例子

```
server {
    listen 80;
    server_name www.test.com;
    location / {
        proxy_pass http://web_server;  #指定代理的URL
    }
}
# 配置负载均衡服务器组
upstream web_server {  # web_server表示代理的服务器主机名,用于proxy_pass 指令执行反向代理时使用
    server 192.168.78.1;
    server 192.168.78.2;
}

# Nginx 检测到后端某台服务器看机，则会在负载均衡时自动剔除该服务器
```

#### 加权轮询负载均衡
```
upstream web_server {  # web_server表示代理的服务器主机名,用于proxy_pass 指令执行反向代理时使用
    server 192.168.78.1 weight=1;
    server 192.168.78.2 weight=3;
}
# weigth 参数表示权值，权值越高则被分配到的概率越大
# Nginx 检测到后端某台服务器看机，则会在负载均衡时自动剔除该服务器
```
除了 weight外，常用状态参数如下

配置方式 | 说明
---|---
max_fails | 允许请求失败的次数，默认为 1,当超过最大次数时，返回proxy_next_upstream指令定义的错误
fail_timeout |  在经历了max_fails次失败后，暂停服务的时间。且在实际应用中max_fails 一般与fail_timeout 一起使用
backup | 预留的备份机器
down | 表示当前的s e rv er 暂时不参与负载均衡

例子
```
upstream web_server {  # web_server表示代理的服务器主机名,用于proxy_pass 指令执行反向代理时使用
    server 192.168.78.1 weight=1 max_fails=2 fail_timeout=2;
    server 192.168.78.2 weight=3 max_fails=2 fail_timeout=2;
    server 193.168.78.3 backup;  # 当另外的非backup故障或者忙绿时，才会请求backup服务器
}
```

#### ip_hash 负载均衡

> 将每个请求按照访问IP 的hash 结果分配，这样就可以便来自同一个IP 的客户端用户固定访问一台Web 服务器，有效地解决了动态网页存在的Session 共享问题。

例子
```bash
upstream web_server {
    ip_hash;  # 使用ip_hash 方式处理负载均衡时，Web服务器在负载均衡列表中的状态不能使用weight 和l backup 设置。
    server 192.168.78.1;
    server 192.168.78.2;
    server 193.168.78.3 down;  # down 参数标识，在负载均衡时，会忽略该服务器的分配。(服务器宕机时)
}
```
> 由于ip_hash 方式为每一个用户IP 绑定一个Web 服务器处理，将会导致某些Web 服务器接收的请求多，某些Web 服务器接到的请求少，无法保证Web 服务器的负载均衡。因此，建议只在必要的情况下使用这种方式



# 其他配置

##### 设置用户和组

> 需要设置的用户和组已经创建

```
# 1 编译安装配置方式,在./configure编译安装Nginx时选项中，
# 添加如下,user用于指定用户名称，group 用于指定用户所在组的名称
--user=<user>
--group=<group>

# 2 修改配置文件方式
# 找到
# user nobody;
#修改为
user nuser ngroup;
# 重启服务
```

##### 自定义错误页

```bash
# error_page 指令用于自定义错误页面， 500 、502 、503 和504 指的就是HTTP 错误代码， /50x . html 用于表示当发生上述指定的任意一个错误时，都使用网站根目录下的50x. html 文件处理
error_page 500 502 503 504 /50x.html;

# error_page 指令还可以指定单个错误的处理页面、利用在线资源处理指定的错误，更改网站响应的状态码

# 为每种类型的错误设置单独的处理方式
error_page 403 /40x.html;
error_page 404 /404.jpg;

# 利用在线资源进行处理错误
error_page 403 http://example.com/forbidden.html;
error_page 500 502 503 504 http://example.com/notfound.html;

# 更改晌应状态码
# 出现404的时候，浏览器响应信息中会得到自定义的码值200
error_page 404 =200 /40x.html;
# 另外，更改响应状态码时还可以不指定确切的码值，而是由重定向后实际处理的真实结果来决定
error_page 404 = /40x.html;
```

##### 权限控制指令

```
allow  # 用于设置允许访问的权限
deny  # 用于设置禁止访问的权限
# 在使用时，权限指令后只需跟上允许或禁止的IP,IP 段或all 即可。其中， all 表示所有的
```
> 注意

* 单个IP 指定作用范围最小， all 指定作用范围最大。
* 同一块下，若同时存在多个权限指令（ deny 、allow ） ，则先出现的访问权限设置生效，并且会对后出现的设置进行覆盖，未覆盖的范围依然生效，否则以先出现的设置为准。
* 当多个块（如http 、server 、location ）中都出现了权限设置指令，则内层块中的权限级别要比外层块中设置的权限级别高。

例子
> 默认如下

```bash
server {
    listen       80;
    server_name  localhost;
    root   html;
    index  index.html index.htm;
}
```
> 禁止所有用户的访问
```bash
server {
    listen       80;
    server_name  localhost;
    root   html;
    index  index.html index.htm;
    deny all;
}
```

> 只允许指定用户访问
```bash
server {
    listen       80;
    server_name  localhost;
    root   html;
    index  index.html index.htm;
    allow 10.240.172.253;
    deny all;
}
```
> 不同块间的权限指令优先级
```bash
http {
    deny all;  # 对所有的server生效
    server {
        listen       80;
        server_name  localhost;
        root   html;
        index  index.html index.htm;
        allow all  # 优先级更高 
    }
}
```

##### 设置目录列表  
在找不到index.html时的会显示文件列表


```bash
autoindex on;
# 在http 块中，表示用于对所有站点都有效； 在server 块中，表示对指定站点有效；在location块中，表示对某个目录起作用

# 设置显示文件的时间格式与大
autoindex_exact_size  off;   #设置精准显示文件大小还是大概显示文件大小,以kB/ MB/ GB 为单位显示
autoindex_localtime on;  #令设置文件最后一次修改时间,示显示的时间为文件的服务器时间。

```

##### 自配置文件的引入


```
include file | mask;

# file 用于指定包含的文件名称， mask用于指定某一路径下的文件，其路径可以是相对路径，也可以是绝对路径
```
例子

```
# 第1 种方式： 单个个文件引入
include vhost/test.conf;
# 第2 种方式：利用通配符
include vhost/*.conf;
```

##### 访问控制典型应用

> location 语法

```
location [= | ~ | ~* | ^~] URI {...}
location @name {...}

# 其中 =、~、~*、^~、@ 都是location用于实现访问控制的前缀，且在使用时只能选择一种，也可不设置前缀
# URI表示URL地址中从域名到参数之间的部分，{...}表示指令块，用于满足location匹配条件后需要执行的指令
```


前缀 | 说明
---|---
=| 根据其后的指定模式进行精准匹配。例如，在访问时要与 /html/aaa/index. html 完全一致才会执行其后的指令块
~|使用正则表达式完成location 的匹配，区分大小写
~*|使用正则表达式完成location 的匹配，不区分大小写
^~|不使用正则表达式，完成以指定模式开头的location 匹配,遵循最大前缀匹配规则
@| 用于定义一个location 块，且该块不能被外部客户端所访问，只能被Ngin内部配置指令所访问

> 精准匹配  
用户访问的URI与指定的URI完全一致的情况，才会执行其后的指令块

```bash
server {
    listen       80;
    server_name  localhost;
    location =/index {
        root   html;
        index  index.html index.htm;
        allow 192.168.12.123  # 放通该ip
    }
    deny all;  # 禁止所有ip访问
}

```

> 正则匹配  
多个正则location之间按照正则location在配置文件中的书写顺序进行匹配，且只要匹配成功就不会继续匹配后面定义的正则location.
```bash
server {
    listen       80;
    server_name  localhost;
    location ~\.html$ {  # 匹配网站根目录下以. html 结尾的文件
        allow all;
    }
    location ~^/test/.*\.html$ {  # 匹配网站根目录下test目录中以.html 结尾的文件
        deny all;
    }
}

```

> 最大前缀匹配  
由于location可以同时定义多个，当一个配置文件中同时出现多个location 时，普通location 之间遵循“最大前缀匹配”原则。通俗地讲就是，匹配度最高的location 将会执行，示例如下

```bash
location /test {
    allow all;
}
location /test/log {
    deny all;
}
```
> 当最大前缀location与正则location同时存在时，如果正则location匹配成功，则不会执行最大前缀location

```bash
location / {  # 匹配当前网站根目录下的所有文件
    allow all;
}
location ~\.html$ {  # 正则匹配所有以.html结尾的URI
    deny all;
}
```

> location / {} 与location =/{} 的区别  
    1. location / {} 遵守普通location 的最大前缀匹配，由于任何URI 都必然以 "/"  根开头，所以对于一个URI，若配直文件中有更合适的匹配则会将其替代，否则返回location / {}  匹配到的结果，它相当于站点默认配直。  
    2. location =/{} 遵守的是精准匹配，也就是只能匹配改站点根目录，同时会禁止搜索正则location ，效率比location / {}要高，因此，芳在开发中能确定精准匹配的情况，可以采用 location =/{}的方式，提升匹配效率
    

> 禁用正则匹配  
利用 ＝ 精准匹配或 ^~ 非正则匹配可以在正则匹配之前优先匹配，从而禁止执行原有的正则匹配


```bash
location =/test/test.html {  # 精准匹配网站根目录下的 /test/test.html
    allow all;
}
location ^~/ {  # 非正则匹配网站根目录下的文件
    deny all;
}
location~\.html$ {  #于正则匹配网站根目录下以.html 为结尾的文件
    allow all;
}
```
> 当多种类型的location 匹配同时出现时，最终执行结果为“ ＝ ”匹配优先于“ ^~ ”匹配，“ ^~  ”匹配优先于正则匹配，正则匹配优先于普通的最大前缀匹配。只要优先的location 匹配成功，就不会执行其他的location

> location 中指定目录时 root 和 alias 区别

```
# 当收到＂/img/itheima.png＂请求时，将请求映射为“/var/www/image/itheima.png"
location /img/ {
    alias /var/www/image/;
}
# 当收到＂/img/itheima.png＂请求时，将请求映射为“/var/www/image/img/itheima.png"
location /img/ {
    root /var/www/image;
}

# alias 在映射路径时不会追加location 匹配到的部分，而root 追加了location 匹配到的部分
```


## 日志文件

> 访问日志  
log_format 和 access_log. (nginx.conf中找)


```bash
# 注意  
# Nginx 默认开启了访问日志的功能，且log_format 指令的配置仅可用在http块内，否则会出现警告信。
# log_format可以设置多个，access_log可以设置在server块中

# 设置访问日志的格式, main 表示访问日志格式名称
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';

# 第1 个参数logs/access.log用于指定相对于Nginx 的安装目录/usr/local/nginx的日志文件存放路径，并包含日志文件名称
# 第2 个参数表示由log_format指令定义的日志格式名称。
access_log  logs/access.log  main;

# buffer 参数用于设置内存缓存区的大小，flush 参数用于设置内容保存在缓存区中的最大时间
# 注意：手动创建test目录，保证当前nginx进程的用户和组有对该目录的创建access.log的权限，否则无法创建
access_log  logs/test/access.log  main buffer=2k flush=5s;  # 也可以这样配置

# 若在访问过程中需要记录子请求的日志记录，则可以将log_subrequest指令设置为on ，否则默认不记录。
log_subrequest on;

# 多次访问后，可在 /usr/local/nginx/logs/access.log 中查看日志

# 关闭访问日志
access_log off;

```

> 日志格式相关内置变量

内置变量 | 含义
---|---
$remote_addr | 客户端的IP地址
$remote_user | 客户端用户名，用于记录浏览者进行身份验证时提供的名称，如果没有登录则为空
$time_local | 访问的时间与时区，如21/Sep/2016:12:21:25 +0800 ，时间信息最后的+0800 表示服务器所处时区位于UTC之后的8小时
$request | 请求的URI和HTTP协议，如GET /HTTP/l.1
$status | 记录请求返回的HTTP状态码，如200(成功)
$body_bytes_sent | 发送给客户端的文件主体内容的大小，如899
$http_referer | 来路URL地址
$http_user_agent | 客户端浏览器信息
$http_x_forwarded_for | 客户端IP地址列表（包括中间经过的代理）


## 错误日志

> 在nginx.conf中找到error_log指令，如下


```bash
# 第1个参数，用于存放错误日志的路径
# 第2个参数，用于指定错误记录详细程度的等级，默认值为error， 共有<debug、info、notice、warn、error、crit> 日志记录详细程度依次递减，debug最详细，crit最简洁
error_log  logs/error.log;
error_log  logs/error.log  notice;
error_log  logs/error.log  info;

# 可通过访问不存在资源测试

# error_log 可以在main、http、server、location块中都可以进行设置，配置方式相同

# 关闭错误日志
error_log /dev/null;

```

## 日志文件切割

> 手动  
手动备份文件后，使用 nginx -s reopen 重新生成日志文件即可

> 自动，定时执行脚本（供参考，根据实际需求）

```bash
# file_name: cut_log.sh
# path: /usr/local/nginx/logs/test/cut_log.sh
#!/bin/bash
#当前Nginx日志文件存放目录
logs_path="/usr/local/nginx/logs/test"
#备份日志文件
mv $logs_path/access.log $logs_path/ `date -d yesterday +"%Y%m%d"`.log
#重新打开Nginx日志
/usr/local/nginx/sbin/nginx -s reopen
```

```bash
# 添加权限
chmod +x cut_log.sh
#定时任务
crontab -e
#写入，每天0点备份
0 0 * * * /usr/local/nginx/logs/test/cut_log.sh > /dev/null 2＞&1

# 每分钟执行一次
* * * * * /usr/local/nginx/logs/test/cut_log.sh > /dev/null 2＞&1

# /dev/null 2＞&1 指令用于屏蔽标准输出和标准出错的信息
```


## 缓存配置


#### 临时缓存配置

添加如下内容
```
# 代理临时目录
proxy_temp_path /usr/local/nginx/proxy_temp_dir;
# web缓存目录和参数设置
proxy_cache_path /usr/local/nginx/proxy_cache_dir levels=1:2 keys_zone=cache_one:50m inactive=1m max_size=500m;
```

* /usr/local/nginx/proxy_cache_dir 参数：表示用户自定义的缓存文件保存目录
* levels 参数：表示缓存目录下的层级目录结构，它是根据哈希后的请求URL 地址创建的，目录名称从晗希后的字符串结尾处开始截取。
(假设哈希后的请求链接地址为af7098al5e430326l97ee015l6fdace0 ，则levels = 1: 2表示，第1 层子目录的名称是长度为1 的字符0 ，第2 层子目录的名称是长度为2 的字符ce,)
* keys_zone 参数：指定缓存区名称及大小，例如， cache_one: 50 m 表示缓存区名称为cache_one ，在内存中的空间是50MB
* inactive 参数：表示主动清空在指定时间内未被访问的缓存。例如， lm 清空在1 分钟内未被访问过的缓存， lh 表示1 小时， ld 表示1 天等
* max_size 参数：表示指定磁盘空间大小。例如， 500m,10g


>注意  
Nginx 在进行缓存时，首先会被写人proxy_temp_path 指定的临时目录中，因此建议proxy_ cache_path 和proxy_temp_path 指令设置的目录应在同一个文件系统中，避免不同文件系统之间的磁盘I/ 0 消耗。


```bash
http {
    # 代理临时目录,当上游服务器的响应过大不能存储到配置的缓冲区域时，Nginx存储临时文件硬盘路径。
    proxy_temp_path proxy_temp_dir;
    # web缓存目录和参数设置
    proxy_cache_path proxy_cache_dir levels=1:2 keys_zone=cache_one:50m inactive=1m max_size=500m;
    
    server {
        listen 80 ;
        server_name www.test.com;
        #增加两个响应头信息，用于获知访问的服务帮地址与缓存是有成功
        add_header X-Via $server_addr;  # 表示服务器地址
        add_header X-Cache $upstream_cache_status;  # 表示资源缓存状态 
        location / {
            #设置缓存区域名称
            proxy_cache cache_one ;
            #以域名、URI、参数组合成Web 缓存的Key值， Nginx 根据Key 值哈希
            proxy_cache_key $host$uri$is_args$args;
            #对不同的HTTP 状态码设置不同的缓存时间
            proxy_cache_valid 200 10m;  #200缓存10分钟
            proxy_cache_valid 304 1m;  #304缓存1分钟
            proxy_cache_valid 301 302 1h;  #301 302缓存1小时
            proxy_cache_valid any 1m;  #其他未设置的状态码缓存1分钟
            # 设置反向代理
            proxy_pass http://10.240.171.42:8007;
        }
    }
}
```
proxy_cache_key 指令参数中使用的具体内置变量的说明如下。
* $host ： 服务器的域名，如www.test.com。
* $uri ：域名和参数之间的部分，如/index.html 。
* $is_args ： 有URL 参数时，则值为？，否则为空字符串。
* $args ： 保存URL 参数，如a=l&b=2 ，没有参数时为空字符串。
* 利用$is_args 和$args ，可以实现根据不同URL 参数缓存不同文件。


 $upstream_cache_status的返回值如下
 

返回值 | 说明
---|---
HIT | 缓存命中
MISS | 未命中，请求被传送到后端
EXPIRED | 缓存已经过期，请求被传送到后端
UPDATING | 正在更新缓存，将使用旧的应答
STALE | 无法从后端服务器更新缓存时，返回了旧的缓存内容（可通过proxy_cache_use_stale指令配置）
BYPASS | 缓存被绕过了（可通过proxy_cache_bypass 指令配置）
REV ALIDA TED | 启用proxy_cache_revalidate 指令后，当缓存内容过期时， Nginx 通过一次If-Modified-Since 的请求头去验证缓存内容是否过期，此时会返回该状态



指令 | 说明
---|---
proxy_cache_bypass | 用于配置Nginx 向客户端发送响应数据时，不从缓存中获取的条件
proxy_cache_lock | 用于设置是否开启缓存的锁功能
proxy_cache_lock_timeout | 用于设置缓存的锁功能开启以后锁的超时时间
proxy_no_cache | 配置在什么情况下不使用缓存功能
proxy_cache_min_uses | 当同一个URL 被重复请求达到指定的次数后，才对该URL 进行缓存
proxy_cache_revalidate | 用于当缓存内容过期时， Nginx 通过一次If-Modified-Since 的请求头去验证缓存内容是否过期
proxy_cache_use_stale | 设置状态，用于内容源Web 服务器处于这些状态时， Nginx 向客户端响应历史缓存数据


安装脚本（阿里云ubuntu）
```
#!/bin/bash
apt update

wget http://nginx.org/download/nginx-1.14.2.tar.gz
tar -zxvf nginx-1.14.2.tar.gz
#安装nginx依赖包
# centos使用下面这句
# echo y | apt install pcre-devel zlib-devel openssl-dlevel
# ubuntu使用下面这句
echo y | apt install openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev

cd nginx-1.14.2/
./configure --prefix=/usr/local/nginx --with-http_ssl_module
make && make install


# 创建软链接
ln -s /usr/local/nginx/sbin/nginx /usr/local//sbin/nginx

# n写入ginx.service文件
echo '#!/bin/bash
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
esac' > /etc/init.d/nginx

# 添加权限
chmod u+x /etc/init.d/nginx
# unmask：取消对 unit 的注销。 
systemctl unmask nginx.service

nginx

```

