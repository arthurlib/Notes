参考：
[daoCloud平台](https://account.daocloud.io/signin)使用


----------------

#### 从容器构建image

1. 先对已经运行的(存在)容器进行一些修改，例如 apt update，更新一下软件包

```
docker run -i -t ubuntu:14.04 /bin/bash
apt update && apt install -y vim
# 重新进入容器
# docker container exec -it 7054aa92bf8e /bin/bash
# docker attact 7054aa92bf8e
```


2. commit命令用来将容器转化为镜像，运行下面的命令，我们可以讲刚刚的容器转换为镜像:

```
# docker commit 的语法格式为：
# docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]

sudo docker commit -m "Added nginx from ubuntu14.04" -a "saymagic" 79c761f627f3 saymagic/ubuntu-nginx:v1

说明
-m: 参数用来来指定提交的说明信息
-a: 可以指定用户信息的
79c761f627f3: 代表的是容器的id
saymagic/ubuntu-nginx:v1: 指定目标镜像的用户名、仓库名和tag信息。创建成功后会返回这个镜像的ID信息。

# 还可以用 docker history 具体查看镜像内的历史记录
docker history nginx:v2

# 示例，手动构建完镜像之后要进行清理，以此来减小镜像体积
FROM debian:stretch
RUN buildDeps='gcc libc6-dev make wget' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && mkdir -p /usr/src/redis \
    && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
    && make -C /usr/src/redis \
    && make -C /usr/src/redis install \
    && rm -rf /var/lib/apt/lists/* \
    && rm redis.tar.gz \
    && rm -r /usr/src/redis \
    && apt-get purge -y --auto-remove $buildDeps
```


#### 从dockerfile构建image

1. 进入一个目录，新建目录 www,在其中添加index.html文件


2. 编写Dockerfile文件
```
# filename: Dockerfile
FROM ubuntu:14.04
MAINTAINER zhuzhenyuan<zhenyuanzhu@outlook.com>
RUN apt-get update && apt-get install -y nginx
COPY ./www /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# 说明
第一行是用来声明我们的镜像是基于什么构建的，这里我们指定为ubuntu14.04 
第二行的作用在于说明维护者。
第三行和第四行的RUN命令用来在容器内部的shell里执行命令。
第五行将当前系统的www文件夹拷贝到容器的/usr/share/nginx/html目录下
第六行声明当前需要对外开放80端口
最后一行表示运行容器时开启nginx。
```

> 为什么daemon off;  
docker 容器默认会把容器内部第一个进程，也就是pid=1的程序作为docker容器是否正在运行的依据，如果docker 容器pid挂了，那么docker容器便会直接退出

> docker run的时候把command作为容器内部命令，如果你使用nginx，那么nginx程序将后台运行，这个时候nginx并不是pid为1的程序，而是执行的bash，这个bash执行了nginx指令后就挂了，所以容器也就退出了，和你这个一样的道理，pm2 start 过后，bash 的pid为1，那么此时bash执行完以后会退出，所以容器也就退出了。


3. 构建
```
# 指令
docker build [选项] <上下文路径/URL/->

# docker build
# docker image build

示例 Dockerfile在当前目录
docker build -t zhuzhenyuan/ubuntu:test.0.0.2 .
docker build -t="zhuzhenyuan/ubuntu:test.0.0.2" .
docker image build -t ubuntu .
docker image build -t ubuntu:test.0.0.2 .

-f: 可以指定docker file

镜像构建上下文（Context）
docker build 命令最后有一个 .。. 表示当前目录，而 Dockerfile 就在当前目录
Docker 在运行时分为 Docker 引擎（也就是服务端守护进程）和客户端工具，构建是在服务端守护进程执行

当构建的时候，用户会指定构建镜像上下文的路径，docker build 命令得知这个路径后，会将路径下的所有内容打包，然后上传给 Docker 引擎。
这样 Docker 引擎收到这个上下文包后，展开就会获得构建镜像所需的一切文件。

如果在 Dockerfile 中这么写：

COPY ./package.json /app/
这并不是要复制执行 docker build 命令所在的目录下的 package.json，也不是复制 Dockerfile 所在目录下的 package.json，而是复制 上下文（context） 目录下的 package.json

.dockerignore
如果目录下有些东西确实不希望构建时传给 Docker 引擎，那么可以用 .gitignore 一样的语法写一个，该文件是用于剔除不需要作为上下文传递给 Docker 引擎的。


这只是默认行为，实际上 Dockerfile 的文件名并不要求必须为 Dockerfile，而且并不要求必须位于上下文目录中，比如可以用 -f ../Dockerfile.php 参数指定某个文件作为 Dockerfile。

一般习惯性的会使用默认的文件名 Dockerfile，以及会将其置于镜像构建上下文目录中
```
> 上面代码中,-t参数用来指定image文件的名字,后面还可以用冒号指定标签,如果不指定,默认标签就是latest,最后那个.表示Dockerfile文件所在的路径.这个例子Dockerfile文件在当前路径,所以就是一个.

生成容器
```
# 上面的例子运行
docker run -p 8000:80 -d zhuzhenyuan/ubuntu:test.0.0.2

# 或者
docker container run -p 8000:80 -it zhuzhenyuan/ubuntu:test.0.0.2 /bin/bash
```


> 上传image

发布image文件  
首先，去 hub.docker.com 或 cloud.docker.com注册一个账户。然后，用下面的命令登录

```
docker login
docker logout # 退出登录
```

接着，为本地的 image 标注用户名和版本。
```
# 设置镜像标签
docker tag [imageName] [username]/[repository]:[tag]
docker image tag [imageName] [username]/[repository]:[tag]

# 实例
docker tag 860c279d2fec runoob/centos:dev
docker image tag koa-demos:0.0.1 ruanyf/koa-demos:0.0.1
```

也可以不标注用户名，重新构建一下 image 文件。重新构建
```
$ docker image build -t [username]/[repository]:[tag] .
```


最后，发布 image 文件。
```
# docker push
docker image push [username]/[repository]:[tag]
```


#### 其它 docker build 的用法

> 直接用 Git repo 进行构建

docker build 还支持从 URL 构建，比如可以直接从 Git repo 中构建：

```
docker build https://github.com/twang2218/gitlab-ce-zh.git#:11.1
# 这行命令指定了构建所需的 Git repo，并且指定默认的 master 分支，构建目录为 /11.1/，
# 然后 Docker 就会自己去 git clone 这个项目、切换到指定分支、并进入到指定目录后开始构建。
```

> 用给定的 tar 压缩包构建

```
docker build http://server/context.tar.gz
# 如果所给出的 URL 不是个 Git repo，而是个 tar 压缩包，
# 那么 Docker 引擎会下载这个包，并自动解压缩，以其作为上下文，开始构建。
```

> 从标准输入中读取 Dockerfile 进行构建

```
docker build - < Dockerfile
或
cat Dockerfile | docker build -
# 如果标准输入传入的是文本文件，则将其视为 Dockerfile，
# 并开始构建。这种形式由于直接从标准输入中读取 Dockerfile 的内容，
# 它没有上下文，因此不可以像其他方法那样可以将本地文件 COPY 进镜像之类的事情。
```


> 从标准输入中读取上下文压缩包进行构建

```
docker build - < context.tar.gz
# 如果发现标准输入的文件格式是 gzip、bzip2 以及 xz 的话，
# 将会使其为上下文压缩包，直接将其展开，将里面视为上下文，并开始构建。
```

#### 其它制作镜像的方式

> 从 rootfs 压缩包导入

```
格式：docker import [选项] <文件>|<URL>|- [<仓库名>[:<标签>]]

# 压缩包可以是本地文件、远程 Web 文件，甚至是从标准输入中得到。
# 压缩包将会在镜像 / 目录展开，并直接作为镜像第一层提交。

比如我们想要创建一个 OpenVZ 的 Ubuntu 16.04 模板的镜像：

docker import \
    http://download.openvz.org/template/precreated/ubuntu-16.04-x86_64.tar.gz \
    openvz/ubuntu:16.04
```

> docker save 和 docker load

```
Docker 还提供了 docker save 和 docker load 命令，用以将镜像保存为一个文件，然后传输到另一个位置上，再加载进来。
这是在没有 Docker Registry 时的做法，
现在已经不推荐，镜像迁移应该直接使用 Docker Registry，
无论是直接使用 Docker Hub 还是使用内网私有 Registry 都可以。

保存镜像
使用 docker save 命令可以将镜像保存为归档文件。
保存镜像的命令为：
$ docker save alpine -o filename
$ file filename
filename: POSIX tar archive

这里的 filename 可以为任意名称甚至任意后缀名，但文件的本质都是归档文件
注意：如果同名则会覆盖（没有警告）


若使用 gzip 压缩：
docker save alpine | gzip > alpine-latest.tar.gz
然后我们将 alpine-latest.tar.gz 文件复制到了到了另一个机器上，可以用下面这个命令加载镜像：

docker load -i alpine-latest.tar.gz
```


#### 导出和导入容器

```
导出容器
docker export 7691a814370e > ubuntu.tar
这样将导出容器快照到本地文件。

导入容器快照
可以使用 docker import 从容器快照文件中再导入为镜像，例如

cat ubuntu.tar | docker import - test/ubuntu:v1.0

此外，也可以通过指定 URL 或者某个目录来导入，例如

docker import http://example.com/exampleimage.tgz example/imagerepo

注：用户既可以使用 docker load 来导入镜像存储文件到本地镜像库，也可以使用 docker import 来导入一个容器快照到本地镜像库。
这两者的区别在于容器快照文件将丢弃所有的历史记录和元数据信息（即仅保存容器当时的快照状态），
而镜像存储文件将保存完整记录，体积也要大。
此外，从容器快照文件导入时可以重新指定标签等元数据信息。
```
