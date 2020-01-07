scp 是通过ssh协议传输数据，支持断点续传，命令如下：

```bash
rsync -P --rsh=ssh home.tar 192.168.0.34:/home/home.tar

#-P: 是包含了 “–partial –progress”， 部分传送和显示进度
#-rsh=ssh 表示使用ssh协议传送数据

#如果不想每次都使用 rsync -P rsh=ssh 之类的，可以写成
alias scpr="rsync -P --rsh=ssh"
#那么下次就可以直接使用 scpr home.tar 192.168.0.34:/home/home.tar 来拷贝数据了。
```

在传输过程中，目标文件会以.home.tar.xxxx文件也隐藏，可以用la -a来显示出来。  
如果scpr中断了，那么该文件会变成用户指定的目标文件"home.tar",下次传的时候又会改成.home.tar.xxxx文件。
