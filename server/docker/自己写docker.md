简介

Docker是一个开源工具，它可以将你的应用打包成一个标准格式的镜像，并且以容器的方式运行。Docker容器将一系列软件包装在一个完整的文件系统中，这个文件系统包含应用程序运行所需要的一切：代码、运行时工具、系统工具、系统依赖，几乎有任何可以安装在服务器上的东西。这些策略保证了容器内应用程序运行环境的稳定性，不会被容器外的系统环境所影响

容器跟虚拟机比较

[虚拟机模型](https://imgconvert.csdnimg.cn/aHR0cHM6Ly93d3cuYmFja2JsYXplLmNvbS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDE4LzA2L3Ztcy5wbmc?x-oss-process=image/format,png)

[容器模型](https://imgconvert.csdnimg.cn/aHR0cHM6Ly93d3cuYmFja2JsYXplLmNvbS9ibG9nL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDE4LzA2L2NvbnRhaW5lcnMucG5n?x-oss-process=image/format,png)

1.1.3容器加速升发效率

Docker容器可以帮助开发者跳过设置冗杂的开发环境，专注于开发软件的新功能，具体有如下3项。
0加速开发：再也不用等待数小时设置开发环境，可以很方便地使生产环境的代码在本地跑起来。
0赋能创造力： Docker容器的隔离特性可以让开发者摆脱限制。开发者可以为自己的应用选择最好的语言和工具，再也不用担心产生内部工具的冲突。
0消除环境不一致：将应用程序的配置和所有依赖打包成一个镜像在容器中，可以保证应用在任何环境中都可以按照预期来运行，再也不用担心不得不在不同环境中安装相同软件和配置的问题。

1.1.4 利用容器合作开发

Docker 镜像可以存储到Docker Hub中，团队成员可以通过 Docker Store、Docker Hub管 理分享镜像。所有的变化和历史都可以在整个组织间查看。
而且，你可以很简单地分享你的容器，不需要担心环境依赖产生的不一致问题，其他团队也可以很简单地引用你的容器，而不需要去关心它是如何工作的。

1.1.5 利用容器快速扩容

Docker 允许动态地改变应用程序，可以通过扩容快速提高应用程序的能力并及时修复缺陷。Docker容器可以秒级启动和停止，因此，它可以在需要的时候快速扩容出大量的应用程序，扛住并发的压力。

***

Linux Namespace 介绍

2.1.1概念

Linux Namespace是Kernel的一个功能，它可以隔离一系列的系统资源，比如PID （ProcessID） 、 User ID. Network等。一般看到这里，很多人会想到一个命令chroot，就像chroot t许把当前目录变成根目录一样（被隔离开来的） ， Namespace也可以在一些资源上，将进程隔离起来，这些资源包括进程树、网络接口、挂载点等。

当前Linux一共实现了6种不同类型的Namespace.

UTS Namespace IPC Namespace PID Narnespace Network Namespace User Namespace

系统调用参数CLONE NEWNS CLONE NEWUTS CLONE NEWIPCCLONE NEWPID CLONE NEWNET CLONE NEWUSER

内核版本2.4.192.6.192.6.192.6.2426.293.8

| Namespace类型       | 系统调用参数         | 内核版本   |
| ----------------- | -------------- | ------ |
| Mount Namespace   | CLONE\_NEWNS   | 2.4.19 |
| UTS Namespace     | CLONE\_NEWUTS  | 2.6.19 |
| IPC Namespace     | CLONE\_NEWIPC  | 2.6.19 |
| PID Narnespace    | CLONE\_NEWPID  | 2.6.24 |
| Network Namespace | CLONE\_NEWNET  | 2.6.29 |
| User Namespace    | CLONE\_NEWUSER | 3.8    |

Namespace的API主要使用如下3个系统调用

*   clone() 创建新进程。根据系统调用参数来判断哪些类型的Namespace被创建，而且它们的子进程也会被包含到这些Namespace中。
*   unshare() 将进程移出某个Namespace。
*   setns() 将进程加入到Namespace中。

linux Veth网络
```bash
# 创建两个网络 namespace
sudo ip netns add ns1 sudo ip netns add ns2

# 创建一对Veth
sudo ip link add veth0 type veth peer name veth1

# 分别将两个 Veth 移到两个 Name space 
sudo ip link set vethO netns nsl sudo ip link set vethl netns ns2

# 去 nsl names pace 中查看网络设备 
sudo ip netns exec nsl ip link

# 如图，再ns1和ns2的Namespace中， 除了loopback 设备 以外就只看到了一个网络设备。 当请求发送到这个虚拟网络设备 ，都会原封不动地从另一个网 Namespace 的网络接口出来。例如，给两端分别配置不同的地址后 ，向虚拟网络设备的一端发送请求 就能到达这个虚拟网络设备对应的另一端。

# 配置每个 veth 的网络地址和 Namespace 的路由 
sudo ip netns exec nsl ifconfig vethO 172.18.0.2/24 up 
sudo ip netns exec ns2 ifconfig vethl 172.18.0.3/24 up 
sudo ip netns exec nsl route add default dev vethO 
sudo ip netns exec ns2 route add default dev vethl

# 通过 veth 端出去的包，另外 端能够直接接收到 sudo ip netns exec nsl ping -c 1 172.18.0.3
```

Linux Bridge

```bash
创建 veth设备并将一端移入 Namespace
sudo ip netns add nsl
sudo ip link add vethO type veth peer name vethl 
sudo ip link vethl setns nsl 

创建网桥
sudo brctl addbr brO

挂载网络设备
sudo brctl addif brO ethO 
sudo brctl addif brO vethO 


Linux路由表

路由表是 Linux 内核的 个模块，通过定义路由表来决定在某个网络 Namespace 中包的流向，从而定义请求会到哪个网络设备上


启动虚拟网络设备，并设置它在 Net Namespace 中的 IP 地址
sudo ip link set vethO up 
sudo ip link set brO up 
sudo ip netns exec nsl ifconfig vethl 172.18.0.2/24 up


分别设置 nsl 网络空间的路由和宿主机上的路由
default 代表 0.0.0.0/0 即在 Net Namespace 中所有流量都经过 vethl 网络设备流出
sudo ip netns exec nsl route add default dev vethl 

在宿主机上将 172.18.0.0/24 的网段请求路由 brO 网桥
sudo route add -net 172.18.0.0/24 dev br O


通过设置路由， 对IP地址的请求就能正确被路由到对应的网络设备，从而实现通信

查看宿主机的 IP 地址
sudo ifconfig ethO

从 Namespace 中访问宿主机的地址
sudo ip netns exec nsl ping -c 1 10.0.2.15 

从宿主机访问 Namespace 中的网络地址
ping -c 1 172.18.0.2



Linux iptables

iptables 是对 Linux 内核的 netfilter 模块进行操作和展示的工具，用来管理包的流动和转送。 iptables 定义了一套链式处理的结构，在网络包传输的各个阶段可以使用不同的策略对包进行加工、传送或丢弃。在容器虚拟化的技术中，经常会用到两种策略 MASQUERADE和DNAT ，用于容器和宿主机外部的网络通信。


MASQUERADE

iptables 中的 MASQUERADE 策略可以将请求包中的源地址转换成 个网络设备的地址，比如 6.1.2 小节介绍的那个 Namespace 中网络设备的地址是 172.18.0.2 ，这个地址虽然在宿主机上可以路由到 brO 网桥，但是到达宿主机外部之后，是不知道如何路由到这个 IP 地址的，所以如果请求外部地址的话，需要先通过 MASQUERADE 策略将这个 IP 转换成宿主机出口网卡的 IP ，如下。

打开 IP 转发
sudo sysctl -w net.ipv4.conf.all.forwarding=l 

对 Name space 中发出的包添加网络地址转换
sudo iptables -t nat -A POSTROUTING -s 172 . 18.0.0/24 -o ethO -j MASQUERADE

在 Namespace 中请求宿主机外部地址时，将 Namespace 中的源地址转换成宿主机的地址作为源地址，就可以在 Namespace 中访问宿主机外的网络了。




DNAT

iptables 中的 DNAT 策略也是做网络地址的转换，不过它是要更换目标地址，经常用于将内部网络地址的端口映射到外部去 比如，上面那个例子中的 Namespace 如果需要提供服务给宿主机之外的应用去请求要怎么办呢？外部应用没办法直接路由到 172.18.0.2 这个地址，这时候就可以用到 DNAT 策略。


将到宿主机上 80 端口的请求转发到 Namespace的IP上
sudo iptables -t nat -A PREROUTING -p tcp -m tcp --dport 80 -j DNAT --to-destination 172.18.0.2:80 


这样就可以把宿主机上 80 端口的 TCP 请求转发到 Namespace 中的地址 172.18.0.2:80 ，从而实现外部的应用调用。


```

| Namespace类型       | 系统调用参数         | 内核版本   | 作用                                                                                                                     |
| ----------------- | -------------- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| Mount Namespace   | CLONE\_NEWNS   | 2.4.19 | 隔离各个进程看到额挂载点视图。在不同 Namespace 的进程中看到的文件系统层次是不一样的                                                                        |
| UTS Namespace     | CLONE\_NEWUTS  | 2.6.19 | 隔离nodename和domainname两个系统标识，在UTS Namespace里面，每个Namespace允许有自己的hostname                                                 |
| IPC Namespace     | CLONE\_NEWIPC  | 2.6.19 | 隔离 System V IPC 和 POSIX message queues.每一个 IPC Namespace 都有自己的 System V IPC 和 POSIX message queue                      |
| PID Narnespace    | CLONE\_NEWPID  | 2.6.24 | 隔离进程                                                                                                                   |
| Network Namespace | CLONE\_NEWNET  | 2.6.29 | 隔离网络设备、 IP 地址端口等网络栈的 Namespace。 Network Namespace 可以让每个容器拥有自己独立的（虚拟的）网络设备，而且容器内的应用可以绑定 到自己的端口，每个 Namespace 内的端口都不会互相冲突 |
| User Namespace    | CLONE\_NEWUSER | 3.8    | 隔离用户的用户组ID。就是说 一个进程的 User ID 和Group ID在User Namespace 内外是不同                                                            |

