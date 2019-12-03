官网： http://memcached.org/

# 安装
参考： https://github.com/memcached/memcached/wiki/Install

linux

```
# 必须
# Linux系统安装memcached，首先要先安装libevent库。

sudo apt-get install libevent ibevent-dev         自动下载安装（Ubuntu/Debian）

yum install libevent libevent-devel                    自动下载安装（Redhat/Fedora/Centos）

# 官网 http://libevent.org/ 选择源码安装
wget https://github.com/libevent/libevent/rele ases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz
tar -zxvf libevent-2.1.8-stable.tar.gz
cd libevent-2.1.8-stable
./configure --prefix=/usr/local/libevent
make && make install
ln -s /usr/local/lib/libevent-2.0.so.5 /usr/lib/libevent-2.1.so.6

# 安装 Memcached

# Ubuntu/Debian
sudo apt-get install memcached

# Redhat/Fedora/Centos
yum install memcached

# FreeBSD
portmaster databases/memcached

源码安装
官网： http://memcached.org

wget http://memcached.org/latest                    下载最新版本
tar -zxvf latest                                    解压源码
cd memcached-1.x.x                                  进入目录
./configure --prefix=/usr/local/memcached           配置
make && make test                                   编译
sudo make install                                   安装

```

运行

```
$ /usr/local/memcached/bin/memcached -h                           命令帮助

# 注意：如果使用自动安装 memcached 命令位于 /usr/local/bin/memcached。

启动选项：

-d是启动一个守护进程；
-m是分配给Memcache使用的内存数量，单位是MB；
-u是运行Memcache的用户；
-l是监听的服务器IP地址，可以有多个地址；
-p是设置Memcache监听的端口，，最好是1024以上的端口；
-c是最大运行的并发连接数，默认是1024；
-P是设置保存Memcache的pid文件。
```

（1）作为前台程序运行：

root用户运行要带  -u root  参数

```
/usr/local/memcached/bin/memcached -p 11211 -m 64m -vv
```
（2）作为后台服务程序运行

```
/usr/local/memcached/bin/memcached -p 11211 -m 64m -d

#或者

/usr/local/memcached/bin/memcached -d -m 64M -u root -l 192.168.0.200 -p 11211 -c 256 -P /tmp/memcached.pid
```

windows

参考： https://www.runoob.com/memcached/window-install-memcached.html



# 连接

```
# 命令中的 HOST 和 PORT 为运行 Memcached 服务的 IP 和 端口
telnet HOST PORT

# 例子

set foo 0 0 3 
bar
get bar
quit
```

# Memcached 存储命令

###### Memcached set 命令

> Memcached set 命令用于将 value(数据值) 存储在指定的 key(键) 中。

> 如果set的key已经存在，该命令可以更新该key所对应的原来的数据，也就是实现更新的作用。

语法：
> set 命令的基本语法格式如下：

```
set key flags exptime bytes [noreply] 
value 
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
bytes：在缓存中存储的字节数
noreply（可选）： 该参数告知服务器不需要返回数据
value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）
```

实例
> 以下实例中我们设置：

* key → runoob
* flag → 0
* exptime → 900 (以秒为单位)
* bytes → 9 (数据存储的字节数)
* value → memcached

```
set runoob 0 900 9
memcached
STORED

get runoob
VALUE runoob 0 9
memcached

END
输出
如果数据设置成功，则输出：

STORED
输出信息说明：

STORED：保存成功后输出。
ERROR：在保存失败后输出。
```

###### Memcached add 命令

> Memcached add 命令用于将 value(数据值) 存储在指定的 key(键) 中。

> 如果 add 的 key 已经存在，则不会更新数据(过期的 key 会更新)，之前的值将仍然保持相同，并且您将获得响应 NOT_STORED。

语法：
> add 命令的基本语法格式如下：

```
add key flags exptime bytes [noreply]
value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
bytes：在缓存中存储的字节数
noreply（可选）： 该参数告知服务器不需要返回数据
value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）


输出信息说明：
STORED：保存成功后输出。
NOT_STORED ：在保存失败后输出。
```

###### Memcached replace 命令

> Memcached replace 命令用于替换已存在的 key(键) 的 value(数据值)。

> 如果 key 不存在，则替换失败，并且您将获得响应 NOT_STORED。

语法：
> replace 命令的基本语法格式如下：

```
replace key flags exptime bytes [noreply]
value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
bytes：在缓存中存储的字节数
noreply（可选）： 该参数告知服务器不需要返回数据
value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）


输出信息说明：
STORED：保存成功后输出。
NOT_STORED：执行替换失败后输出。
```

###### Memcached append 命令

> Memcached append 命令用于向已存在 key(键) 的 value(数据值) 后面追加数据 。

语法：
> append 命令的基本语法格式如下：

```
append key flags exptime bytes [noreply]
value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
bytes：在缓存中存储的字节数
noreply（可选）： 该参数告知服务器不需要返回数据
value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）

输出信息说明：
STORED：保存成功后输出。
NOT_STORED：该键在 Memcached 上不存在。
CLIENT_ERROR：执行错误。
```

###### Memcached prepend 命令

> Memcached prepend 命令用于向已存在 key(键) 的 value(数据值) 前面追加数据 。

语法：
> prepend 命令的基本语法格式如下：

```
prepend key flags exptime bytes [noreply]
value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
bytes：在缓存中存储的字节数
noreply（可选）： 该参数告知服务器不需要返回数据
value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）


输出信息说明：
STORED：保存成功后输出。
NOT_STORED：该键在 Memcached 上不存在。
CLIENT_ERROR：执行错误。
```

###### Memcached CAS 命令
> 
Memcached CAS（Check-And-Set 或 Compare-And-Swap） 命令用于执行一个"检查并设置"的操作

> 它仅在当前客户端最后一次取值后，该key 对应的值没有被其他客户端修改的情况下， 才能够将值写入。

> 检查是通过cas_token参数进行的， 这个参数是Memcach指定给已经存在的元素的一个唯一的64位值。

语法：
> CAS 命令的基本语法格式如下：

```
cas key flags exptime bytes unique_cas_token [noreply]
value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
exptime：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）
bytes：在缓存中存储的字节数
unique_cas_token通过 gets 命令获取的一个唯一的64位值。
noreply（可选）： 该参数告知服务器不需要返回数据
value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）
```

实例
> 要在 Memcached 上使用 CAS 命令，你需要从 Memcached 服务商通过 gets 命令获取令牌（token）。

> gets 命令的功能类似于基本的 get 命令。两个命令之间的差异在于，gets 返回的信息稍微多一些：64 位的整型值非常像名称/值对的 "版本" 标识符。

实例步骤如下：

- 如果没有设置唯一令牌，则 CAS 命令执行错误。
- 如果键 key 不存在，执行失败。
- 添加键值对。
- 通过 gets 命令获取唯一令牌。
- 使用 cas 命令更新数据
- 使用 get 命令查看数据是否更新

```
cas tp 0 900 9
ERROR             <− 缺少 token

cas tp 0 900 9 2
memcached
NOT_FOUND         <− 键 tp 不存在

set tp 0 900 9
memcached
STORED

gets tp
VALUE tp 0 9 1
memcached
END

cas tp 0 900 5 1
redis
STORED

get tp
VALUE tp 0 5
redis
END


输出
如果数据添加成功，则输出：

STORED
输出信息说明：

STORED：保存成功后输出。
ERROR：保存出错或语法错误。
EXISTS：在最后一次取值后另外一个用户也在更新该数据。
NOT_FOUND：Memcached 服务上不存在该键值。
```

# Memcached 查找命令

###### Memcached get 命令

> Memcached get 命令获取存储在 key(键) 中的 value(数据值) ，如果 key 不存在，则返回空。

语法：
```
get 命令的基本语法格式如下：
get key

多个 key 使用空格隔开，如下:
get key1 key2 key3

参数说明如下：
key：键值 key-value 结构中的 key，用于查找缓存值。
```

###### Memcached gets 命令

> Memcached gets 命令获取带有 CAS 令牌存 的 value(数据值) ，如果 key 不存在，则返回空。

语法：

```
gets 命令的基本语法格式如下：
gets key

多个 key 使用空格隔开，如下:
gets key1 key2 key3

参数说明如下：
key：键值 key-value 结构中的 key，用于查找缓存值。
```

###### Memcached delete 命令

> Memcached delete 命令用于删除已存在的 key(键)。

语法：

```
delete 命令的基本语法格式如下：
delete key [noreply]

参数说明如下：
key：键值 key-value 结构中的 key，用于查找缓存值。
noreply（可选）： 该参数告知服务器不需要返回数据

输出信息说明：
DELETED：删除成功。
ERROR：语法错误或删除失败。
NOT_FOUND：key 不存在。
```

###### Memcached incr 与 decr 命令

> Memcached incr 与 decr 命令用于对已存在的 key(键) 的数字值进行自增或自减操作。

> incr 与 decr 命令操作的数据必须是十进制的32位无符号整数。

> 如果 key 不存在返回 NOT_FOUND，如果键的值不为数字，则返回 CLIENT_ERROR，其他错误返回 ERROR。

```
incr 命令
语法：
incr 命令的基本语法格式如下：

incr key increment_value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
increment_value： 增加的数值。


输出信息说明：
NOT_FOUND：key 不存在。
CLIENT_ERROR：自增值不是对象。
ERROR其他错误，如语法错误等。
```


```
decr 命令
decr 命令的基本语法格式如下：

decr key decrement_value
参数说明如下：

key：键值 key-value 结构中的 key，用于查找缓存值。
decrement_value： 减少的数值。

输出信息说明：
NOT_FOUND：key 不存在。
CLIENT_ERROR：自增值不是对象。
ERROR其他错误，如语法错误等。
```

# Memcached 统计命令

###### Memcached stats 命令

> Memcached stats 命令用于返回统计信息例如 PID(进程号)、版本号、连接数等。

语法：
> stats 命令的基本语法格式如下：

```
stats
```

这里显示了很多状态信息，下边详细解释每个状态项：

* pid：	memcache服务器进程ID
* uptime：服务器已运行秒数
* time：服务器当前Unix时间戳
* version：memcache版本
* pointer_size：操作系统指针大小
* rusage_user：进程累计用户时间
* rusage_system：进程累计系统时间
* curr_connections：当前连接数量
* total_connections：Memcached运行以来连接总数
* connection_structures：Memcached分配的连接结构数量
* cmd_get：get命令请求次数
* cmd_set：set命令请求次数
* cmd_flush：flush命令请求次数
* get_hits：get命令命中次数
* get_misses：get命令未命中次数
* delete_misses：delete命令未命中次数
* delete_hits：delete命令命中次数
* incr_misses：incr命令未命中次数
* incr_hits：incr命令命中次数
* decr_misses：decr命令未命中次数
* decr_hits：decr命令命中次数
* cas_misses：cas命令未命中次数
* cas_hits：cas命令命中次数
* cas_badval：使用擦拭次数
* auth_cmds：认证命令处理的次数
* auth_errors：认证失败数目
* bytes_read：读取总字节数
* bytes_written：发送总字节数
* limit_maxbytes：分配的内存总大小（字节）
* accepting_conns：服务器是否达到过最大连接（0/1）
* listen_disabled_num：失效的监听数
* threads：当前线程数
* conn_yields：连接操作主动放弃数目
* bytes：当前存储占用的字节数
* curr_items：当前存储的数据总数
* total_items：启动以来存储的数据总数
* evictions：LRU释放的对象数目
* reclaimed：已过期的数据条目来存储新数据的数目


###### Memcached stats items 命令

> Memcached stats items 命令用于显示各个 slab 中 item 的数目和存储时长(最后一次访问距离现在的秒数)。

语法：
> stats items 命令的基本语法格式如下：

```
stats items
```

###### Memcached stats slabs 命令

> Memcached stats slabs 命令用于显示各个slab的信息，包括chunk的大小、数目、使用情况等。

语法：
> stats slabs 命令的基本语法格式如下：

```
stats slabs
```

###### Memcached stats sizes 命令

> Memcached stats sizes 命令用于显示所有item的大小和个数。

> 该信息返回两列，第一列是 item 的大小，第二列是 item 的个数。

语法：
> stats sizes 命令的基本语法格式如下：

```
stats sizes
```

###### Memcached flush_all 命令

> Memcached flush_all 命令用于清理缓存中的所有 key=>value(键=>值) 对。

> 该命令提供了一个可选参数 time，用于在制定的时间后执行清理缓存操作。

语法：
> flush_all 命令的基本语法格式如下：

```
flush_all [time] [noreply]
```



