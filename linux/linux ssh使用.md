[ssh-keygen 中文手册](http://www.jinbuguo.com/openssh/ssh-keygen.html)

生成密钥对

```
ssh-keygen -t rsa -C "yourmail@gmail.com" -f name

-f : filename
-C : 备注

```


利用 SSH 的用户配置文件 Config 管理 SSH 会话

> SSH 程序可以从以下途径获取配置参数：

* 用户配置文件 (~/.ssh/config)
* 系统配置文件 (/etc/ssh/ssh_config)

> 文件权限  
> chmod 644 ~/.ssh/config

```bash
# SSH配置项参数值可以使用通配符：
# '*' 代表 0～n 个非空白字符。
# '?' 代表一个非空白字符。
# '!' 表示例外通配。
Host 别名

# 指定远程主机名，可以直接使用数字IP地址。如果主机名中包含 ‘%h’ ，则实际使用时会被命令行中的主机名替换
HostName 主机名

Port 端口
User 用户名

# 指定密钥认证使用的私钥文件路径。
# 默认为~/.ssh/id_dsa, ~/.ssh/id_ecdsa, ~/.ssh/id_ed25519 或 ~/.ssh/id_rsa 中的一个。
# 文件名称可以使用以下转义符
# '%d' 本地用户目录
# '%u' 本地用户名称
# '%l' 本地主机名
# '%h' 远程主机名
# '%r' 远程用户名
# 可以指定多个密钥文件，在连接的过程中会依次尝试这些密钥文件
IdentityFile 密钥文件的路径
IdentitiesOnly 只接受SSH key 登录
PreferredAuthentications 强制使用Public Key验证

# SSH客户端的StrictHostKeyChecking配置指令，
# StrictHostKeyChecking=no时可以实现当第一次连接服务器时自动接受新的公钥。不再有任何警告出现了
StrictHostKeyChecking



```

```bash
# 别名
Host www
    HostName www.hi-linux.com
    Port 22
    User root
    IdentityFile  ~/.ssh/id_rsa
    IdentitiesOnly yes
   
 Host my
	hostName 47.102.124.78
	Port 22
	User user

# 不同主机公用私钥
Host github.com git.coding.net
    HostName %h
    Port 22
    User git
    IdentityFile  ~/.ssh/id_rsa_blog
    IdentitiesOnly yes

# ssh -T git@git.coding.net
# ssh -vT git@github.com
# -v 是输出编译信息
```
