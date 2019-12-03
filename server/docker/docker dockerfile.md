参考：  
https://yeasy.gitbooks.io/docker_practice/

包括：   
FROM、MAINTAINER、RUN、ENV、COPY、ADD、EXPOSE、CMD、  
ENTRYPORINT、VOLUME、USER、WORKDIR、ONBUILD、LABEL、  
STOPSIGNAL、HEALTHCHECK、SHELL

---------------
示例

```
# docker file

MAINTAINER zhuzhenyuan<zhenyuanzhu@outlook.com>
FROM node:8.4
COPY . /app
WORKDIR /app
RUN npm install --registry=https://registry.npm.taobao.org
EXPOSE 3000
CMD node demos/01.js

# 说明
From node:8.4 : 该image继承自官方的node image,冒号表示标签,这里表示8.4,即8.4版本的node.
COPY . /app :将当前目录下的所有文件都拷贝到image文件的 /app 目录.
WORKDIR /app : 指定接下来的工作目录为 /app .
RUN npm install：在/app目录下，运行npm install命令安装依赖。注意，安装后所有的依赖，都将打包进入 image 文件。
EXPOSE 3000 : 将容器的3000 端口暴露出来,允许外部连接这个端口.

```

> USER 指定当前用户

```
格式：USER <用户名>[:<用户组>]

USER 指令和 WORKDIR 相似，都是改变环境状态并影响以后的层。
WORKDIR 是改变工作目录，USER 则是改变之后层的执行 RUN, CMD 以及 ENTRYPOINT 这类命令的身份。

当然，和 WORKDIR 一样，USER 只是帮助你切换到指定用户而已，这个用户必须是事先建立好的，否则无法切换。
示例：
RUN groupadd -r redis && useradd -r -g redis redis
USER redis
RUN [ "redis-server" ]
如果以 root 执行的脚本，在执行期间希望改变身份，
比如希望以某个已经建立好的用户来运行某个服务进程，不要使用 su 或者 sudo，
这些都需要比较麻烦的配置，而且在 TTY 缺失的环境下经常出错。建议使用 gosu
```

> FROM

```
FROM 指令用于设置在新映像创建过程期间将使用的容器映像。
格式：FROM 
示例：
FROM nginx
FROM microsoft/dotnet:2.1-aspnetcore-runtime
```

> RUN

```
RUN 指令指定将要运行并捕获到新容器映像中的命令。 这些命令包括安装软件、创建文件和目录，以及创建环境配置等。
格式：
RUN ["", "", ""]
RUN cmd
示例：
RUN apt-get update
RUN mkdir -p /usr/src/redis
RUN apt-get update && apt-get install -y libgdiplus
RUN ["apt-get","install","-y","nginx"]
# 注意：每一个指令都会创建一层，并构成新的镜像。
# 当运行多个RUN指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。
# 因此，在很多情况下，我们可以合并指令并运行，
# 例如：RUN apt-get update && apt-get install -y libgdiplus。
# 在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。
# 使用换行符时，可能会遇到一些问题，具体可以参阅下节的转义字符。
```

> COPY

```
COPY 指令将文件和目录复制到容器的文件系统。文件和目录需位于相对于 Dockerfile 的路径中。
格式：
COPY <源路径> <目标路径>
如果源或目标包含空格，请将路径括在方括号和双引号中。
COPY ["", ""]
示例：
COPY . .
COPY nginx.conf /etc/nginx/nginx.conf
COPY . /usr/share/nginx/html
COPY hom* /mydir/
```

> ADD不推荐使用

```
ADD 指令与 COPY 指令非常类似，但它包含更多功能。
除了将文件从主机复制到容器映像，ADD 指令还可以使用 URL 规范从远程位置复制文件。
如果 <源路径> 为一个 tar 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，
ADD 指令将会自动解压缩这个压缩文件到 <目标路径> 去。
格式：
ADD <source> <destination>
示例：
ADD https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe /temp/python-3.5.1.exe
ADD Itaest.tar.gz /var/www/
此示例会将 Python for Windows下载到容器映像的 c:\temp 目录。
ADD 指令会令镜像构建缓存失效，从而可能会令镜像构建变得比较缓慢。
因此在 COPY 和 ADD 指令中选择的时候，可以遵循这样的原则，
所有的文件复制均使用 COPY 指令，仅在需要自动解压缩的场合使用 ADD
```

> WORKDIR

```
WORKDIR 指令用于为其他 Dockerfile 指令（如 RUN、CMD）设置一个工作目录，并且还设置用于运行容器映像实例的工作目录。
格式：
WORKDIR
示例：
WORKDIR /app
格式为 WORKDIR <工作目录路径>。

使用 WORKDIR 指令可以来指定工作目录（或者称为当前目录），
以后各层的当前目录就被改为指定的目录，如该目录不存在，WORKDIR 会帮你建立目录。
```

> CMD

```
CMD指令用于设置部署容器映像的实例时要运行的默认命令。
例如，如果该容器将承载 NGINX Web 服务器，则 CMD 可能包括用于启动Web服务器的指令，如 nginx.exe。 
如果 Dockerfile 中指定了多个CMD 指令，只会计算最后一个指令。
在运行时可以指定新的命令来替代镜像设置中的这个默认命令，run的时候
格式：
CMD ["可执行文件", "参数1", "参数2"...]
CMD <命令>
参数列表格式：CMD ["参数1", "参数2"...]。在指定了 ENTRYPOINT 指令后，用 CMD 指定具体的参数
示例：
CMD ["c:\\Apache24\\bin\\httpd.exe", "-w"]
CMD c:\\Apache24\\bin\\httpd.exe -w
```

> ENTRYPOINT

```
配置容器启动后执行的命令，并且不可被 docker run 提供的参数覆盖。
每个 Dockerfile 中只能有一个ENTRYPOINT，当指定多个时，只有最后一个起效。
ENTRYPOINT 的目的和 CMD 一样，都是在指定容器启动程序及参数。ENTRYPOINT 在运行时也可以替代，不过比 CMD 要略显繁琐，需要通过 docker run 的参数 --entrypoint 来指定。
当指定了 ENTRYPOINT 后，CMD 的含义就发生了改变，不再是直接的运行其命令，而是将 CMD 的内容作为参数传给 ENTRYPOINT 指令，换句话说实际执行时，将变为：<ENTRYPOINT> "<CMD>"
格式：
ENTRYPOINT ["", ""]
示例：
ENTRYPOINT ["dotnet", "Magicodes.Admin.Web.Host.dll"]

总结：
一般还是会用entrypoint的中括号形式作为docker 容器启动以后的默认执行命令，
里面放的是不变的部分，可变部分比如命令参数可以使用cmd的形式提供默认版本，
也就是run里面没有任何参数时使用的默认参数。
如果我们想用默认参数，就直接run，否则想用其他参数，就run 里面加参数。
```

> ENV

```
ENV命令用于设置环境变量。
这些变量以”key=value”的形式存在，并可以在容器内被脚本或者程序调用。
这个机制给在容器中运行应用带来了极大的便利。
格式：
ENV <key> <value>
ENV <key1>=<value1> <key2>=<value2>...
示例：
ENV VERSION=1.0 DEBUG=on \
NAME="Happy Feet"
```

> ARG 构建参数

```
格式：ARG <参数名>[=<默认值>]

构建参数和 ENV 的效果一样，都是设置环境变量。
所不同的是，ARG 所设置的构建环境的环境变量，在将来容器运行时是不会存在这些环境变量的。
但是不要因此就使用 ARG 保存密码之类的信息，因为 docker history 还是可以看到所有值的。

Dockerfile 中的 ARG 指令是定义参数名称，以及定义其默认值。
该默认值可以在构建命令 docker build 中用 --build-arg <参数名>=<值> 来覆盖。

在 1.13 之前的版本，要求 --build-arg 中的参数名，必须在 Dockerfile 中用 ARG 定义过了，
换句话说，就是 --build-arg 指定的参数，必须在 Dockerfile 中使用了。
如果对应参数没有被使用，则会报错退出构建。从 1.13 开始，这种严格的限制被放开，不再报错退出，而是显示警告信息，并继续构建。
这对于使用 CI 系统，用同样的构建流程构建不同的 Dockerfile 的时候比较有帮助，
避免构建命令必须根据每个 Dockerfile 的内容修改。
```

> EXPOSE

```
EXPOSE用来指定端口，使容器内的应用可以通过端口和外界交互。（可以写多个）
格式：
EXPOSE
示例：
EXPOSE 80
格式为 EXPOSE <端口1> [<端口2>...]。

EXPOSE 指令是声明运行时容器提供服务端口，这只是一个声明，在运行时并不会因为这个声明应用就会开启这个端口的服务
。在 Dockerfile 中写入这样的声明有两个好处，
一个是帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射；
另一个用处则是在运行时使用随机端口映射时，也就是 docker run -P 时，会自动随机映射 EXPOSE 的端口。

要将 EXPOSE 和在运行时使用 -p <宿主端口>:<容器端口> 区分开来。-p，是映射宿主端口和容器端口，
换句话说，就是将容器的对应端口服务公开给外界访问，
而 EXPOSE 仅仅是声明容器打算使用什么端口而已，并不会自动在宿主进行端口映射。
```

> MAINTAINER

```
设置维护者信息
格式：
MAINTAINER Name <Email>
```

> VOLUME

```
基于镜像创建容器添加数据卷，即在容器中设置一个挂载点，
可以让其他容器挂载或让宿主机访问，
以实现数据共享或对容器数据的备份、恢复或迁移
格式：
VOLUME ["/data", "/data2"]
VOLUME /data
说明：
之前我们说过，容器运行时应该尽量保持容器存储层不发生写操作，
对于数据库类需要保存动态数据的应用，其数据库文件应该保存于卷(volume)中，
为了防止运行时用户忘记将动态文件所保存目录挂载为卷，在 Dockerfile 中，
我们可以事先指定某些目录挂载为匿名卷，这样在运行时如果用户不指定挂载，
其应用也可以正常运行，不会向容器存储层写入大量数据。

VOLUME /data
这里的 /data 目录就会在运行时自动挂载为匿名卷，
任何向 /data 中写入的信息都不会记录进容器存储层，从而保证了容器存储层的无状态化。
当然，运行时可以覆盖这个挂载设置。比如：

docker run -d -v mydata:/data xxxx
在这行命令中，就使用了 mydata 这个命名卷挂载到了 /data 这个位置，
替代了 Dockerfile 中定义的匿名卷的挂载配置。
```

> 转义字符

```
在许多情况下，Dockerfile 指令需要跨多个行；这可通过转义字符完成。
默认 Dockerfile 转义字符是反斜杠 \。 
由于反斜杠在 Windows 中也是一个文件路径分隔符，这可能导致出现问题。

要修改转义字符，必须在 Dockerfile 最开始的行上放置一个转义分析程序指令。 如以下示例所示：

# escape=`

注意，只有两个值可用作转义字符：\ 和 ` 。
```


> HEALTHCHECK 健康检查

```
格式：

HEALTHCHECK [选项] CMD <命令>：设置检查容器健康状况的命令
HEALTHCHECK NONE：如果基础镜像有健康检查指令，使用这行可以屏蔽掉其健康检查指令
HEALTHCHECK 指令是告诉 Docker 应该如何进行判断容器的状态是否正常，这是 Docker 1.12 引入的新指令。

在没有 HEALTHCHECK 指令前，Docker 引擎只可以通过容器内主进程是否退出来判断容器是否状态异常。很多情况下这没问题，但是如果程序进入死锁状态，或者死循环状态，应用进程并不退出，但是该容器已经无法提供服务了。在 1.12 以前，Docker 不会检测到容器的这种状态，从而不会重新调度，导致可能会有部分容器已经无法提供服务了却还在接受用户请求。

而自 1.12 之后，Docker 提供了 HEALTHCHECK 指令，通过该指令指定一行命令，用这行命令来判断容器主进程的服务状态是否还正常，从而比较真实的反应容器实际状态。

当在一个镜像指定了 HEALTHCHECK 指令后，用其启动容器，初始状态会为 starting，在 HEALTHCHECK 指令检查成功后变为 healthy，如果连续一定次数失败，则会变为 unhealthy。

HEALTHCHECK 支持下列选项：

--interval=<间隔>：两次健康检查的间隔，默认为 30 秒；
--timeout=<时长>：健康检查命令运行超时时间，如果超过这个时间，本次健康检查就被视为失败，默认 30 秒；
--retries=<次数>：当连续失败指定次数后，则将容器状态视为 unhealthy，默认 3 次。
和 CMD, ENTRYPOINT 一样，HEALTHCHECK 只可以出现一次，如果写了多个，只有最后一个生效。

在 HEALTHCHECK [选项] CMD 后面的命令，格式和 ENTRYPOINT 一样，分为 shell 格式，和 exec 格式。命令的返回值决定了该次健康检查的成功与否：0：成功；1：失败；2：保留，不要使用这个值。

假设我们有个镜像是个最简单的 Web 服务，我们希望增加健康检查来判断其 Web 服务是否在正常工作，我们可以用 curl 来帮助判断，其 Dockerfile 的 HEALTHCHECK 可以这么写：

FROM nginx
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -fs http://localhost/ || exit 1
这里我们设置了每 5 秒检查一次（这里为了试验所以间隔非常短，实际应该相对较长），如果健康检查命令超过 3 秒没响应就视为失败，并且使用 curl -fs http://localhost/ || exit 1 作为健康检查命令。

使用 docker build 来构建这个镜像：

$ docker build -t myweb:v1 .
构建好了后，我们启动一个容器：

$ docker run -d --name web -p 80:80 myweb:v1
当运行该镜像后，可以通过 docker container ls 看到最初的状态为 (health: starting)：

$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                            PORTS               NAMES
03e28eb00bd0        myweb:v1            "nginx -g 'daemon off"   3 seconds ago       Up 2 seconds (health: starting)   80/tcp, 443/tcp     web
在等待几秒钟后，再次 docker container ls，就会看到健康状态变化为了 (healthy)：

$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                    PORTS               NAMES
03e28eb00bd0        myweb:v1            "nginx -g 'daemon off"   18 seconds ago      Up 16 seconds (healthy)   80/tcp, 443/tcp     web
如果健康检查连续失败超过了重试次数，状态就会变为 (unhealthy)。

为了帮助排障，健康检查命令的输出（包括 stdout 以及 stderr）都会被存储于健康状态里，可以用 docker inspect 来查看。

$ docker inspect --format '{{json .State.Health}}' web | python -m json.tool
```

> ONBUILD

```
FROM node:slim
RUN mkdir /app
WORKDIR /app
ONBUILD COPY ./package.json /app
ONBUILD RUN [ "npm", "install" ]
ONBUILD COPY . /app/
CMD [ "npm", "start" ]

说明：
使用该指令的行，只在当前构建的镜像作为另一个镜像的基础镜像时，才会执行，自身构建不会执行

参考：
https://yeasy.gitbooks.io/docker_practice/image/dockerfile/onbuild.html

```



**优化**

> 下面是一些优化的准则：

* 选择合适的基础镜像

一个合适的基础镜像是指能满足运行应用所需要的最小的镜像，理论上是能用小的就不要用大的，能用轻量的就不要用重量级的，能用性能好的就不要用性能差的。这里有时候还需要考虑那些能够减少我们构建层数的基础镜像。


* 优化指令顺序

Docker会缓存Dockerfile中尚未更改的所有步骤，但是，如果更改任何指令，将重做其后的所有步骤。也就是指令3有变动，那么4、5、6就会重做。因此，我们需要将最不可能产生更改的指令放在前面，按照这个顺序来编写dockerfile指令。这样，在构建过程中，就可以节省很多时间。比如，我们可以把WORKDIR、ENV等命令放前面，COPY、ADD放后面。


* 合并指令

前面我们说到了，每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，

例如：RUN apt-get update && apt-get install -y libgdiplus。

在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。

 

* 删除多余文件和清理没用的中间结果

这点很易于理解，通常来讲，体积更小，部署更快！因此在构建过程中，我们需要清理那些最终不需要的代码或文件。比如说，临时文件、源代码、缓存等等。

* 使用 .dockerignore

.dockerignore文件用于忽略那些镜像构建时非必须的文件，这些文件可以是开发文档、日志、其他无用的文件。例如

.dockerignore

> 下面的代码表示,这三个路径要排除,不要打包进image文件,如果你没有路径可以排除,这个文件也可以不用建立

```
.git
node_modules
npm-debug.log
```

