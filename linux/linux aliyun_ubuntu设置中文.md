https://blog.csdn.net/zhangchao19890805/article/details/52743380

1.安装之前检测当前语言环境

```
echo $LANG
# 屏幕显示：en_US.UTF-8
# 说明现在是英语环境，需要切换到中文环境。
```

2、安装中文语言包

```
apt-get update && apt-get install language-pack-zh-hans -y
```

3、vim /etc/default/locale

> 把原来英语 US 的都换成如下的内容，并且注意配置文件中不能有多余的空格

```
LANG="zh_CN.UTF-8"
LANGUAGE="zh_CN:zh"
LC_NUMERIC="zh_CN"
LC_TIME="zh_CN"
LC_MONETARY="zh_CN"
LC_PAPER="zh_CN"
LC_NAME="zh_CN"
LC_ADDRESS="zh_CN"
LC_TELEPHONE="zh_CN"
LC_MEASUREMENT="zh_CN"
LC_IDENTIFICATION="zh_CN"
LC_ALL="zh_CN.UTF-8"
```


4、vim /etc/environment

> 原来有一行 PATH=.. 不要动这一行  
> 另起一行，复制粘贴以下内容，并且注意配置文件中不能有多余的空格：

```
LANG="zh_CN.UTF-8"
LANGUAGE="zh_CN:zh"
LC_NUMERIC="zh_CN"
LC_TIME="zh_CN"
LC_MONETARY="zh_CN"
LC_PAPER="zh_CN"
LC_NAME="zh_CN"
LC_ADDRESS="zh_CN"
LC_TELEPHONE="zh_CN"
LC_MEASUREMENT="zh_CN"
LC_IDENTIFICATION="zh_CN"
LC_ALL="zh_CN.UTF-8"
```

5、重启机器

```
reboot
```
