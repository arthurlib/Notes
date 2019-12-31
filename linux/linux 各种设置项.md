
以下可以在终端设置,也可在.bashrc文件中写入使每次登陆自动配置.立即生效 `source .bashrc`

http_proxy

> 为http网站设置代理

```bash
# 为http站点设置http代理（默认）
export http_proxy=10.0.0.52:8080
# 为http站点设置sock4、sock5代理
# 设置 socks 代理，自动识别socks版本
export http_proxy=socks://10.0.0.52:1080
# 设置 socks4 代理
export http_proxy=socks4://10.0.0.52:1080
# 设置 socks5 代理
export http_proxy=socks5://10.0.0.52:1080

# 代理使用用户名密码认证
export http_proxy=user:pass@192.158.8.8:8080
```

https_proxy

> 为https网站设置代理

```bash
export https_proxy=10.0.0.52:8080
export https_proxy=user:pass@192.158.8.8:8080
export https_proxy=socks://10.0.0.52:1080
export https_proxy=socks4://10.0.0.52:1080
export https_proxy=socks5://10.0.0.52:1080
```

ftp_proxy

> 为ftp协议设置代理


```bash

```

no_proxy

> 无需代理的主机或域名；可以使用通配符；多个时使用“,”号分隔；

```bash
export no_proxy="*.aiezu.com,10.*.*.*,192.168.*.*,*.local,localhost,127.0.0.1"
```

设置ALL_PROXY

> 全部生效

```bash
export ALL_PROXY=socks5://127.0.0.1:1080
```


改相应工具的配置，比如apt的配置

```bash
sudo vim /etc/apt/apt.conf
在文件末尾加入下面这行
Acquire::http::Proxy "http://proxyAddress:port"
```

如果说经常使用git对于其他方面都不是经常使用，可以直接配置git的命令。

```bash
# 使用ss/ssr来加快git的速度
# 直接输入这个命令就好了
git config --global http.proxy 'socks5://127.0.0.1:1080' 
git config --global https.proxy 'socks5://127.0.0.1:1080'
```

gsettings

> 可用于桌面版linux修改代理配置

参考： [https://linux.cn/article-5673-1.html](https://linux.cn/article-5673-1.html)

> 在桌面版 Ubuntu 中，它的桌面环境设置，包括系统代理设置，都存储在 DConf 数据库，  
这是简单的键值对存储。如果你想通过系统设置菜单修改桌面属性，更改会持久保存在后端的  
DConf 数据库。在 Ubuntu 中更改 DConf 数据库有基于图像用户界面和非图形用户界面的两种方式。  
系统设置或者 dconf-editor 是访问 DConf 数据库的图形方法，  
而 gsettings 或 dconf 就是能更改数据库的命令行工具。


mac 设置代理工具

> networksetup
