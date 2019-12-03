更多参考： https://yeasy.gitbooks.io/docker_practice/install/ubuntu.html

0. 卸载旧版本

> 旧版本的 Docker 称为 docker 或者 docker-engine，使用以下命令卸载旧版本

```
sudo apt-get remove docker docker-engine docker.io -y
```

1. 安装docker

```
apt-get update
apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# 添加 GPG 密钥，国内中科大
# 鉴于国内网络问题，建议使用国内源，官方源请在注释中查看。
# 为了确认所下载软件包的合法性，需要添加软件源的 GPG 密钥。
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
# 添加源，国内
add-apt-repository "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu $(lsb_release -cs) stable"


# 添加 GPG 密钥，官方
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 添加源
# add-apt-repository "deb https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"

# 删除 PPA 源
# 删除 PPA 源的命令格式则为：sudo add-apt-repository -r ppa:user/ppa-name
# 然后进入 /etc/apt/sources.list.d 目录，将相应 ppa 源的保存文件删除。
# 最后同样更新一下：sudo apt-get update


#开始安装
apt-get update && sudo apt-get install docker-ce -y
# apt-get update && apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')
```

2. 启动 Docker CE

```
systemctl enable docker
systemctl start docker
```


3. 建立 docker 用户组

> 默认情况下，docker 命令会使用 Unix socket 与 Docker 引擎通讯。而只有 root 用户和 docker 组的用户才可以访问 Docker 引擎的 Unix socket。出于安全考虑，一般 Linux 系统上不会直接使用 root 用户。因此，更好地做法是将需要使用 docker 的用户加入 docker 用户组。

```
# 只有root的话要新建用户并切换到该用户，新建用户，useradd,adduser
# 参考： https://segmentfault.com/a/1190000007316406
# useradd -d /home/username -m -s /bin/bash username
# 改密码
# passwd username
# 建立 docker 组：
sudo groupadd docker
# 将当前用户加入 docker 组：
sudo usermod -aG docker $USER
# 退出当前终端并重新登录，进行如下测试
# 测试 Docker 是否安装正确
docker run hello-world
```

4. 配置docker mirror

```
# 创建（或修改）/etc/docker/daemon.json。官方中国镜像速度还行。

vim /etc/docker/daemon.json
{
"registry-mirrors": ["https://registry.docker-cn.com"]
}
# 或者
Azure 中国镜像 https://dockerhub.azk8s.cn
阿里云加速器(需登录账号获取)https://cr.console.aliyun.com/cn-hangzhou/mirrors
七牛云加速器 https://reg-mirror.qiniu.com
{
  "registry-mirrors": [
    "https://dockerhub.azk8s.cn",
    "https://reg-mirror.qiniu.com"
  ]
}

# 重启docker服务
systemctl restart docker
```

检查加速器是否生效

```
执行 $ docker info，如果从结果中看到了如下内容，说明配置成功。

Registry Mirrors:
 https://dockerhub.azk8s.cn/
```
 
 gcr.io 镜像

```
国内无法直接获取 gcr.io/* 镜像，我们可以将 gcr.io/<repo-name>/<image-name>:<version> 替换为 gcr.azk8s.cn/<repo-name>/<image-name>:<version> ,例如

# $ docker pull gcr.io/google_containers/hyperkube-amd64:v1.9.2

$ docker pull gcr.azk8s.cn/google_containers/hyperkube-amd64:v1.9.2
```
