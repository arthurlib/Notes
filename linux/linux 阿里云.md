* 阿里云ECS服务器 git clone 速度慢

解决方案
```bash
vim /etc/ssh/ssh_config

# 编辑 /etc/ssh/ssh_config，找到 GSSAPIAuthentication no 这行，删掉前面的注释，然后保存退出
```


* 卸载阿里云盾（安骑士）

卸载方法很简单，执行下面三段命令即可：

```shell
wget http://update.aegis.aliyun.com/download/uninstall.sh
chmod +x uninstall.sh
./uninstall.sh
wget http://update.aegis.aliyun.com/download/quartz_uninstall.sh
chmod +x quartz_uninstall.sh
./quartz_uninstall.sh
```

删除残留：

```shell
pkill aliyun-service
rm -fr /etc/init.d/agentwatch /usr/sbin/aliyun-service
rm -rf /usr/local/aegis*
```



2、屏蔽云盾IP

执行下面命令通过“iptables”防火墙来屏蔽云盾IP：

```shell
iptables -I INPUT -s 140.205.201.0/28 -j DROP
iptables -I INPUT -s 140.205.201.16/29 -j DROP
iptables -I INPUT -s 140.205.201.32/28 -j DROP
iptables -I INPUT -s 140.205.225.192/29 -j DROP
iptables -I INPUT -s 140.205.225.200/30 -j DROP
iptables -I INPUT -s 140.205.225.184/29 -j DROP
iptables -I INPUT -s 140.205.225.183/32 -j DROP
iptables -I INPUT -s 140.205.225.206/32 -j DROP
iptables -I INPUT -s 140.205.225.205/32 -j DROP
iptables -I INPUT -s 140.205.225.195/32 -j DROP
iptables -I INPUT -s 140.205.225.204/32 -j DROP
```

https://blog.csdn.net/qjc_501165091/article/details/51225984
