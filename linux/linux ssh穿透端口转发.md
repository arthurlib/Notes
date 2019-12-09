


```shell
#-L (-Local) 正向隧道
ssh -L [<bindHost>:]<sourcePort>:<forwardToHost>:<onPort> <connectToHost>
#ssh -L 127.0.0.1:8080:127.0.0.1:8080 root@47.102.125.88

# * connectToHost: 远程设备
# * bindHost: 绑定的来源ip，省略时表示所有 （对当前机器）
# * sourcePort: 发往的本机端口 （对当前机器）
# * forwardToHost: 转发的ip （对远程设备）
# * onPort: 转发的端口 （对远程设备）


#-R (-Remote) 反向隧道
ssh -R [<bindHost>:]<sourcePort>:<forwardToHost>:<onPort> <connectToHost>
#ssh -R 127.0.0.1:8088:127.0.0.1:8888 root@47.102.125.88\

# * connectToHost: 远程设备
# * bindHost: 绑定的来源ip，省略时表示所有 （对远程设备）
# * sourcePort: 发往的本机端口 （对远程设备）
# * forwardToHost: 转发的ip （对当前机器）
# * onPort: 转发的端口 （对当前机器）



# * -f：使 SSH 在建立连接之后保持在后台运行。
# * -N：告诉 SSH，我们只希望建立隧道，而不会在远程主机上执行任何指令。
# * -T：告诉 SSH，我们只希望建立隧道，因而不需要创建虚拟终端。
# * -C：允许 SSH 压缩数据。
```

```shell
# 穿透示例

# 内网机
ssh -R 2121:127.0.0.1:22 my
# 跳板机
ssh -L :2345:127.0.0.1:2121 localhost

ssh -p 2345 user@ip
```
