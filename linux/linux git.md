### Git 多平台换行符问题(LF or CRLF)

```shell script
# 提交时转换为LF，检出时转换为CRLF
git config --global core.autocrlf true
# 提交时转换为LF，检出时不转换
git config --global core.autocrlf input
# 提交检出均不转换
git config --global core.autocrlf false


# 拒绝提交包含混合换行符的文件
git config --global core.safecrlf true
# 允许提交包含混合换行符的文件
git config --global core.safecrlf false
# 提交包含混合换行符的文件时给出警告
git config --global core.safecrlf warn  
```

dos2unix 将换行转换成unix风格

```shell script
#如果涉及到在多个系统平台上工作，推荐将 git 做如下配置：

$ git config --global core.autocrlf input
$ git config --global core.safecrlf true
```

### 保存用户名密码

操作之前输入过一次密码

```
1、设置记住密码（默认15分钟）：
git config --global credential.helper cache

2、如果想自己设置时间，可以这样做：
git config credential.helper 'cache --timeout=3600'
这样就设置一个小时之后失效

3、长期存储密码：
git config --global credential.helper store

4、增加远程地址的时候带上密码也是可以的。(推荐)，这个可以直接设置
http://yourname:password@git.oschina.net/name/project.git

或者这样操作
切换到项目目录下  
cd projectfile/
移除远程ssh方式的仓库地址  
git remote rm origin
增加https远程仓库地址
git remote add origin http://yourname:password@git.oschina.net/name/project.git
```

HTTPS协议如何保存凭证信息
HTTPS认证方式虽然需要输入账户密码，但现在也不需要每次都输入。这个凭据保存需要依赖一个凭据管理器，每个操作系统平台都有自己的凭据管理器。可以参考github官方提供的教程来配置

> 建立凭据文件

```
$ touch ~/.git-credentials
$ vim ~/.git-credentials
在文件中加入带凭据的url信息:

https://{username}:{passwd}@github.com
然后告诉git使用这个凭据管理器:

$ git config --global credential.helper store
上面命令会在git配置文件 ～/.gitconfig 中设置上一个凭据地址:

[credential]
    helper = store
```
