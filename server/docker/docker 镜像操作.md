
```
docker inspect ID/Name 查看镜像或者容器的信息信息
```


#### 镜像操作

Docker把应用程序及其依赖打包在一个image文件里面,可以理解为一个容器的说明书. 通过这个image文件可以生成容器的实例.同一个image文件可以生成同时运行的多个实例.

image文件是一个二进制文件,实际上,一个image文件往往继承自另外一个image文件,加上一些个性化设置而成.举例来说:你可以在ubuntu的image基础上加上Apache服务器,形成你自己的image.
kj

> 查找image

```
docker search ubuntu

# 说明 查找镜像Docker Hub 网址为： https://hub.docker.com/
NAME: 镜像仓库源的名称
DESCRIPTION: 镜像的描述
OFFICIAL: 是否docker官方发布
```

> 查看当前镜像列表

```
docker image ls
docker images

# 说明
REPOSITORY：表示镜像的仓库源
TAG：镜像的标签
IMAGE ID：镜像ID
CREATED：镜像创建时间
SIZE：镜像大小

# 中间层镜像
docker image ls -a

根据仓库名列出镜像
docker image ls ubuntu

列出特定的某个镜像，也就是说指定仓库名和标签
docker image ls ubuntu:18.04

只显示id
docker image ls -q
docker image ls -q redis
```

> 获取镜像

```
docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
# Docker 镜像仓库地址：地址的格式一般是 <域名/IP>[:端口号]。默认地址是 Docker Hub。
# 仓库名：如之前所说，这里的仓库名是两段式名称，即 <用户名>/<软件名>。
# 对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像。

docker pull ubuntu
docker pull library/hello-world
docker image pull library/hello-world
```

> 删除镜像

```
docker rmi [imageName]
docker image rm [imageName]

# 删除全部
docker image rm $(docker image ls -q)
docker image rm $(docker image ls -q redis)
```

> 更新镜像,提交版本

```
docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2

# 说明
-m:提交的描述信息
-a:指定镜像作者
e218edb10161：容器ID
runoob/ubuntu:v2:指定要创建的目标镜像名
```

> 镜像体积

```
# 查看镜像、容器、数据卷所占用的空间
docker system df
```

> 虚悬镜像

```
# 被同名镜像覆盖后，原镜像失去了name和tag就是虚悬镜像
docker image ls -f dangling=true

# 一般来说，虚悬镜像已经失去了存在的价值，是可以随意删除的，可以用下面的命令删除。
$ docker image prune
```

> 查看提交历史

```
docker history 183dbef8eba6
```