
连接保持


> 方案一：在客户端设置

> 方法很简单，只需在客户端电脑上编辑（需要root权限）/etc/ssh/ssh_config或~/.ssh/config，并添加如下一行：

```
ServerAliveInterval 60
```
这样ssh会每60秒发送一个KeepAlive请求，保证终端不会因为超时空闲而断开连接。


> 方案二：在服务器端设置

> 如果有相应的权限，也可以在服务器端设置，即编辑/etc/ssh/sshd_config，并添加：

```
TCPKeepAlive yes # 必须打开,表示TCP保持连接不断开
ClientAliveInterval 60  # ClientAliveInterval设置的值要小于各层防火墙的最小值，不然，也就没用了。）
```

> 重启SSH服务器后该项设置会生效。每一个连接到此服务器上的客户端都会受其影响。应注意启用该功能后，安全性会有一定下降（比如忘记登出时...）

重启
```shell script
sudo /etc/init.d/ssh restart
```

重用

> ssh提供了连接重用功能，这个功能的原理很简单，开一个ssh连接放在后台，以后再需要用ssh到同样的远程主机时，ssh会直接用这 个连接的socket文件，不再创建新的连接了只需要新建文件~/.ssh/config并输 入如下命令即可：

```
Host *
ControlMaster auto
ControlPath ~/.ssh/master-%r@%h:%p
```
