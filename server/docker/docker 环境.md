官方文档：https://docs.docker-cn.com/

------------

*docker 容器应该被视为一个进程，这个是理解和定义docker的一条基本原则；别把docker看成一个虚拟机*


环境

> 内核需要3.10+

```
# 查看信息
uname -r
uname -a
```

安装  
（不建议在正式部署时使用，这里只是学习，有风险）
```
wget -qO- https://get.docker.com/ | sh
```

> 当要以非root用户可以直接运行docker时，需要执行 sudo usermod -aG docker username 命令，然后重新登陆

```
sudo usermod -aG docker username
```

启动docker后台服务

```
sudo service docker start
```

测试运行hello-world

```
docker run hello-world
```

镜像加速

```
鉴于国内网络问题，后续拉取 Docker 镜像十分缓慢，我们可以需要配置加速器来解决，
这里使用的是网易的镜像地址：http://hub-mirror.c.163.com。

新版的 Docker 使用 /etc/docker/daemon.json（Linux） 
或者%programdata%\docker\config\daemon.json（Windows） 来配置 Daemon。

请在该配置文件中加入（没有该文件的话，请先建一个）：

{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
```
