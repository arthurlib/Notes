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
```



使用客户端也可以存储密码的。
如果你正在使用ssh而且想体验https带来的高速，那么你可以这样做
```
1、切换到项目目录下  
    cd projectfile/
2、移除远程ssh方式的仓库地址  
    git remote rm origin
3、增加https远程仓库地址
    git remote add origin http://yourname:password@git.oschina.net/name/project.git
```



HTTPS协议如何保存凭证信息
HTTPS认证方式虽然需要输入账户密码，但现在也不需要每次都输入。这个凭据保存需要依赖一个凭据管理器，每个操作系统平台都有自己的凭据管理器。可以参考github官方提供的教程来配置

我这里介绍一个git的凭据管理方式:

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
