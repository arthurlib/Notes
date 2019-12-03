
```shell
# pi的配置工具
sudo raspi-config

# 语言->时区->local
# 去掉 en_GB.UTF-8 UTF-8
# 勾上“en_US.UTF-8 UTF-8”“zh_CN.UTF-8 UTF-8”“zh_CN.GBK GBK”
# 下一屏幕默认语言选zh_CN.UTF-8


# 之后 下载中文库终端输入：

sudo apt-get install ttf-wqy-zenhei

# 最多再重启一下

```

pi 安装py lxml包

```shell
apt install libxml2 libxml2-dev libxslt libxslt-dev

# 错误： src/lxml/includes/etree_defs.h:14:31: fatal error: libxml/xmlversion.h: No such file or directory

export C_INCLUDE_PATH=/usr/include/libxml2/

```

```shell
# 更换软件源
# 默认的软件源速度比较慢，官网有一个镜像列表 http://www.raspbian.org/RaspbianMirrors
# 这里推荐中科大的 https://lug.ustc.edu.cn/wiki/mirrors/help/raspbian 
# 感觉他们的主页做的不错，像有在用心维护的感觉。

# 方法如下。
# 编辑/etc/apt/sources.list文件。删除原文件所有内容，用以下内容取代

deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
```

```shell
# 那个1.0.36版本的，这个版本执行adb install的时候会有执行进度提示。
# 地址：  https://github.com/NetEaseGame/AutomatorX/releases/tag/1.0.12

# 搞下来之后，把adb放到 /usr/local/bin这个目录下，因为adb运行的时候需要root权限，
# 所以需要给这个文件添加一下特权模式，这样普通用户也就可以用了。

sudo chown root:root /usr/local/bin/adb
sudo chmod 0755 /usr/local/bin/adb
sudo chmod +s /usr/local/bin/adb
```
