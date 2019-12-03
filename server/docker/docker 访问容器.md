参考：  
https://github.com/yeasy/docker_practice

#### 外部访问容器

容器中可以运行一些网络应用，要让外部也可以访问这些应用，可以通过 -P 或 -p 参数来指定端口映射。

> 当使用 -P 标记时，Docker 会随机映射一个 49000~49900 的端口到内部容器开放的网络端口。

> -p 则可以指定要映射的端口，并且，在一个指定端口上只可以绑定一个容器。  
> 支持的格式有 ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort。

```
使用 docker container ls 可以看到，本地主机的 49155 被映射到了容器的 5000 端口。此时访问本机的 49155 端口即可访问容器内 web 应用提供的界面。

$ docker run -d -P training/webapp python app.py

同样的，可以通过 docker logs 命令来查看应用的信息。

$ docker logs -f nostalgic_morse
```

> 映射所有接口地址

```
使用 hostPort:containerPort 格式本地的 5000 端口映射到容器的 5000 端口，可以执行

$ docker run -d -p 5000:5000 training/webapp python app.py
此时默认会绑定本地所有接口上的所有地址。
```

> 映射到指定地址的指定端口

```
可以使用 ip:hostPort:containerPort 格式指定映射使用一个特定地址，比如 localhost 地址 127.0.0.1

$ docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py
```

> 映射到指定地址的任意端口

```
使用 ip::containerPort 绑定 localhost 的任意端口到容器的 5000 端口，本地主机会自动分配一个端口。

$ docker run -d -p 127.0.0.1::5000 training/webapp python app.py
还可以使用 udp 标记来指定 udp 端口

$ docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
```

> 查看映射端口配置

```
使用 docker port 来查看当前映射的端口配置，也可以查看到绑定的地址

docker port nostalgic_morse 5000

注意：
容器有自己的内部网络和 ip 地址（使用 docker inspect 可以获取所有的变量，Docker 还可以有一个可变的网络配置。）

-p 标记可以多次使用来绑定多个端口
例如:
$ docker run -d \
    -p 5000:5000 \
    -p 3000:80 \
    training/webapp \
    python app.py
```



#### 更多

运行web应用（需要端口的例子）

```
# 载入镜像
docker pull training/webapp

#运行
docker run -d -P training/webapp python app.py
-d:让容器在后台运行。
-P:将容器内部使用的网络端口映射到我们使用的主机上。

# 通过 -p 参数来设置不一样的端口：
docker run -d -p 5000:5000 training/webapp python app.py

# 查看网络端口的快捷方式
docker port bf08b7f2cd89
docker port wizardly_chandrasekhar

查看 WEB 应用程序日志
docker logs [ID或者名字] 可以查看容器内部的标准输出
docker logs -f bf08b7f2cd89
-f: 让 docker logs 像使用 tail -f 一样来输出容器内部的标准输出。

# 检查 WEB 应用程序
使用 docker inspect 来查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

# Docker容器 暴露多个端口
# 1、创建容器时指定
docker run -p <host_port1>:<container_port1> -p <host_port2>:<container_port2>

# 2、修改dockerfile expose所需要的端口，这样可以免去-p参数。

# 按范围暴露指定端口
EXPOSE 7000-8000
# 或Docker run命令：
docker run –expose = 7000-8000
# 或者，您可以通过Docker run命令将一系列端口发布到主机：
docker run -p 7000-8000:7000-8000

# 指定端口随机映射到宿主机
docker run -P 80 -it ubuntu /bin/bash

# 将容器ip和端口，指定映射到宿主机上
docker run -p 192.168.0.100:8000:80 -it ubuntu /bin/bash


# 端口映射支持的格式
# 参考： https://www.jianshu.com/p/b92d4b845ed6
ip:hostport:containerport #指定ip、指定宿主机port、指定容器port
ip::containerport #指定ip、未指定宿主机port（随机）、指定容器port
hostport:containerport #未指定ip、指定宿主机port、指定容器port
```
