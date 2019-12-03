kubernetes 指南： https://kubernetes.feisky.xyz/setup/cluster/kubeadm  
参考：   
https://zhuanlan.zhihu.com/p/46341911  
https://juejin.im/post/5c9a49ace51d456c9d78dbef  
https://www.kubernetes.org.cn/2059.html  
https://ieevee.com/tech/2018/09/01/kubeadm.html#%E6%8B%89%E5%8F%96k8s%E7%9A%84%E5%8C%85%E5%B9%B6tag  
https://kubernetes.feisky.xyz/  (*)  

官方单机集群部署： https://v1-12.docs.kubernetes.io/zh/docs/setup/independent/create-cluster-kubeadm/




master节点服务器要求 阿里云 2G2核


> kubernetes的国外安装其实非常简单，国内安装的主要问题在于kubernetes部件所需的官方镜像在 http://gcr.io(Google Cloud Container Registry)上，很不幸，这个网站被墙了。所以解决了这个问题，国内环境的安装也就简单了

1. 关闭swap
1. 安装docker环境（参考其他）
1. 增加kubernetes aliyun镜像源
1. 安装kubeadm/kubelet/kubectl
1. 拉取k8s的镜像并tag
1. 开始安装master
1. 添加网络插件，部署weave网络，其他网络还不懂
1. 准备计算资源
1. 安装weave scope

> k8s对master和worker节点的端口开放有要求(关闭防火墙)

![k8s对master和worker节点的端口开放有要求](https://i.loli.net/2019/09/26/6oKOwGp15aekrfZ.png)

关闭swap

> 如果不关闭kubernetes运行会出现错误， 即使安装成功了，node重启后也会出现kubernetes server运行错误。

```
sudo swapoff -a #暂时关闭
同时把/etc/fstab包含swap那行记录删掉
```

添加源

```
apt-get update && apt-get install -y apt-transport-https curl

# 阿里云（测试过）
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF

# 或中科大
cat <<EOF > /etc/apt/sources.list.d/kubernetes.list
deb http://mirrors.ustc.edu.cn/kubernetes/apt kubernetes-xenial main
EOF
```

开始安装

```
apt update && apt install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl  # 设置不自动更新
# 如果你有多台机器，非master节点不需要安装kubeadm/kubectl。当然装了也没啥坏处。
```

```
apt-mark 用来标记安装软件包的状态. 
有时一个软件的仓库出了问题, 用 apt-get 安装后无法使用, 
这时就可以利用 apt-mark hold package 标记该软件包不被自动更新.

Commands:
auto - Mark the given packages as automatically installed
manual - Mark the given packages as manually installed
hold - Mark a package as held back
unhold - Unset a package set as held back
showauto - Print the list of automatically installed packages
showmanual - Print the list of manually installed packages
showhold - Print the list of package on hold
```


获取k8s镜像列表并tag

> 由于官方镜像地址被墙，所以我们需要首先获取所需镜像以及它们的版本。然后从国内镜像站获取。


```
# 阿里云
kubeadm config images list  # 经测试也可以，获取最新版本

# kubeadm config images list --kubernetes-version v1.16.0
# 必须要指定版本，这样kubeadm才不会去连k8s.io。kubeadm init同理


# 获取镜像列表后可以通过下面的脚本从阿里云获取

images=(  # 下面的镜像应该去除"k8s.gcr.io/"的前缀，版本换成上面获取到的版本
    kube-apiserver:v1.16.0
    kube-controller-manager:v1.16.0
    kube-scheduler:v1.16.0
    kube-proxy:v1.16.0
    pause:3.1
    etcd:3.3.15-0
    coredns:1.6.2
)

for imageName in ${images[@]} ; do
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
done
```

初始化环境 开始安装master
这个就很简单了，只需要简单的一个命令：

```
kubeadm init
kubeadm init --kubernetes-version v1.16.0  # 指定版本
```


配置授权信息

> 所需的命令在init成功后也会有提示，主要是为了保存相关的配置信息在用户目录下，这样不用每次都输入相关的认证信息。

```
# KUBECONFIG 这个环境变量必须要设置，应该被写入.bash_profile中

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

或？
sudo cp /etc/kubernetes/admin.conf $HOME/
sudo chown $(id -u):$(id -g) $HOME/admin.conf
export KUBECONFIG=$HOME/admin.conf
或？
export KUBECONFIG=/etc/kubernetes/admin.conf
```

添加网络插件

>部署weave网络

```
sysctl net.bridge.bridge-nf-call-iptables=1 -w
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

准备计算资源

> 因为我只有1个节点，要“计算资源”的话，就只能将master节点的taint去掉，否则普通的Pod默认不会调度上来。

```
kubectl taint nodes --all node-role.kubernetes.io/master-
```

> 如果你有多个节点的话，不需要去掉master的taint。其他节点参照上面的准备阶段在各个节点上做好准备工作以后，只要再Join一下就行了。Join命令在kubeadm init的输出信息里有。

```
kubeadm join --token={token} {master ip:6443}
```


安装weave scope

```
kubectl apply -f "https://cloud.weave.works/k8s/scope.yaml?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

查看是否安装成功

```
kubectl get pods -n kube-system
```

WARNING solve
```
[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver

# [警告IsDockerSystemdCheck]：检测到“cgroupfs”作为Docker cgroup驱动程序。 推荐的驱动程序是“systemd”。
# 参考： https://blog.csdn.net/m82_a1/article/details/97626309

在/etc/docker下创建daemon.json并编辑：
mkdir /etc/docker/daemon.json

加入以下内容：
{
 "exec-opts":["native.cgroupdriver=systemd"]
}

重启docker
systemctl restart docker
systemctl status docker

```

token
```
如果您没有令牌，可以通过在主节点上运行以下命令来获取它
kubeadm token list

默认情况下，令牌在24小时后过期。 如果需要在当前令牌过期后将节点加入集群，可以通过在主节点上运行以下命令来创建新令牌
kubeadm token create
```
