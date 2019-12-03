> 生成

```
ssh-keygen -t rsa -C "yourmail@gmail.com"

# ssh-keygen -f othername # 来生成指定的文件名，或者生成之后
# 但是ssh命令默认只会读取 id_rsa这个私钥，所以如果 是其它 的名字需要添加配置文件 ~/.ssh/config也可以两个改名
```

> 在服务器上安装公钥

```
[root@host ~]$ cd .ssh
[root@host .ssh]$ cat id_rsa.pub >> authorized_keys
```

> 如此便完成了公钥的安装。为了确保连接成功，请保证以下文件权限正确：

```
[root@host .ssh]$ chmod 600 authorized_keys
[root@host .ssh]$ chmod 700 ~/.ssh
```

> 设置 SSH，打开密钥登录功能

```
#编辑 /etc/ssh/sshd_config 文件，进行如下设置：
RSAAuthentication yes
PubkeyAuthentication yes

#另外，请留意 root 用户能否通过 SSH 登录：
PermitRootLogin yes

#当你完成全部设置，并以密钥方式登录成功后，再禁用密码登录：
PasswordAuthentication no

#最后，重启 SSH 服务：
[root@host .ssh]$ service sshd restart
```

> 本地配置

```
# 修改 .ssh/cofnig 文件，添加示例如下
Host 别名
	hostName 192.168.1.2
	Port 22
	User root
```

> 重置服务器后

```
ssh-keygen -R 你要访问的IP地址
```
