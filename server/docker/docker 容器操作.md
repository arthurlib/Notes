#### 容器操作

container 容器文件, image文件生成的实例本身也是一个文件,成为容器文件  
也即是说,一旦容器生成,就会存在两个文件:一个image文件,一个容器文件.而且关闭容器并不会删除容器文件,只是容器停止运行而已

> 回到主机，但是不想容器退出

```
ctrl+p,ctrl+q
```

> 运行容器

```
docker run httpd
docker container run hello-world

# 输出Hello world
docker run ubuntu:15.10 /bin/echo "Hello world"

# 运行交互式的容器
docker run -i -t ubuntu:15.10 /bin/bash
# 说明
-t:在新容器内指定一个伪终端或终端。
-i:允许你对容器内的标准输入 (STDIN) 进行交互。
ubuntu:15.10 - 使用 ubuntu 基础镜像 15.10
/bin/bash - 运行命令 bash shell
注: ubuntu 会有多个版本，通过指定 tag 来启动特定的版本 [image]:[tag]


# 启动容器（后台模式） -d
docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"

# 命令 --rm 参数,在容器终止运行后自动删除容器文件.
docker container run --rm -p 8000:3000 -it koa-demo /bin/bash

# 用 nginx 镜像启动一个容器，命名为 webserver，并且映射了 80 端口。
docker run --name webserver -d -p 80:80 nginx

```

> 启动已终止容器

```
docker start 
docker container start ID/name # 接将一个已经终止的容器启动运行
```

> 重启容器

```
docker restart ID/name
docker container restart ID/name
```

> 停止容器

```
docker stop ID/name
docker container stop ID/name
# 终止容器，直接杀死会丢失数据
docker container kill [container_id]
# 前面的docker container kill命令终止容器的运行,相当于向容器的主进程发送SIGKILL信号,
# 而docker container stop也是用来终止容器的运行,相当于向容器的主进程发送SIGTERM信号
# 然后过一段时间在发送SIGKILL信号.
```

> 移除容器

```
docker rm ID/name
docker container rm [container_id]
如果要删除一个运行中的容器，可以添加 -f 参数。Docker 会发送 SIGKILL 信号给容器。

清理所有处于终止状态的容器
用 docker container ls -a 命令可以查看所有已经创建的包括终止状态的容器，
如果数量太多要一个个删除可能会很麻烦，用下面的命令可以清理掉所有处于终止状态的容器。
docker container prune
```

> 重命名一个容器

```
docker rename old_name new_name 
```

> 查看正在运行的容器

```
docker ps
CONTAINER ID:容器ID
NAMES:自动分配的容器名称

# 查看已经启动的容器
docker ps -s 

# 查看已经创建的容器，包括已经停止的容器
docker ps -a

# 查询最后一次创建的容器：
docker ps -l 
```

> 查看指定容器的标准输出

```
docker logs ID/name
docker container logs ID/name
# 用来查看容器的输出,即容器里shell的标准输出.
# 比如: 如果docker run命令运行容器的时候,没有使用-it参数,就要使用这个命令查看输出.
```

> 查看容器的进程

```
docker top ID/name
```

> 令容器执行指令

```
docker exec [container_id] command
docker container exec [container_id] command
# 用于进行一个正在运行的容器.如果docker container run命令运行容器的时候,
# 没有使用-it参数,就要使用这个命令进入进入容器,一旦进入容器,就可以在容器的shell执行命令了.
```

> 从主机进入容器

```
docker exec -it 7054aa92bf8e /bin/bash

exec 命令: -i -t 参数
只用 -i 参数时，由于没有分配伪终端，界面没有我们熟悉的 Linux 命令提示符，但命令执行结果仍然可以返回。
当 -i -t 参数一起使用时，则可以看到我们熟悉的 Linux 命令提示符。


docker attach 7054aa92bf8e （回车）  # 不推荐，避免

使用attach该命令有问题。
1. 当多个窗口同时使用该命令进入该容器时，所有的窗口都会同步显示。
如果有一个窗口阻塞了，那么其他窗口也无法再进行操作。
2. 当用exit退出时，会把这个容器退出
所以docker attach命令不太适合于生产环境，平时自己开发应用时可以使用该命令。
```

> 从容器中复制文件

```
docker cp [container_id]:[/path/to/file] .
docker container cp [container_id]:[/path/to/file] .
# docker container cp命令用于从正在运行的容器里,将文件拷贝到本机.下面是拷贝当前 目录的写法:
```

> 命令看到具体的改动

```
docker diff Id/Name
```

> 从容器拷贝文件

```
docker cp  02d50df3a6d1:/bin/bash .
```