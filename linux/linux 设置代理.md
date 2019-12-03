设置代理
```
export http_proxy=http://proxyAddress:port
export https_proxy=http://127.0.0.1:12333
export http_proxy="socks5://127.0.0.1:1080"
export https_proxy="socks5://127.0.0.1:1080"
# 或者干脆直接设置ALL_PROXY
export ALL_PROXY=socks5://127.0.0.1:1080

# =================

改相应工具的配置，比如apt的配置
sudo vim /etc/apt/apt.conf
在文件末尾加入下面这行
Acquire::http::Proxy "http://proxyAddress:port"

# ==============

# 如果说经常使用git对于其他方面都不是经常使用，可以直接配置git的命令。
# 使用ss/ssr来加快git的速度
# 直接输入这个命令就好了

git config --global http.proxy 'socks5://127.0.0.1:1080' 
git config --global https.proxy 'socks5://127.0.0.1:1080'

```
