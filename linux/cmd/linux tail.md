> tail本身的功能是显示文件的后多少行

```shell
# 显示filename后十行
tail filename
# 显示filename后n行
tail -n filename 
# 通过添加-f选项可以监控文件变化,文件有更新就会打印出来
tail -f filename

# 而且watch的原理就是重复的执行后面的命令,默认的时间间隔是2秒.如
watch -d -n 10 cat /etc/syslog.conf
# 每10秒打印一下/etc/syslog.conf文件,-d表示高亮变化的部分

# 这两个命令在监控日志文件的时候相当有用,有点注意的是经测试不能在后台运行
```
