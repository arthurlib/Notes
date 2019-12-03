> 启用ssh,默认关机

```
刻录系统完成后在/boot分区（根目录）新建  ssh 文件即可
```
> 还没连接到树莓派，配置wifi,wifi配置 wpa_supplicant

在 boot 分区，也就是树莓派的 /boot 目录下新建 wpa_supplicant.conf 文件

```
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
	ssid="301301"
	psk="18367116191"
	key_mgmt=WPA-PSK
	priority=1
}
 
network={
	ssid="TP-LINK_954D"
	psk="vvcn1101"
	key_mgmt=WPA-PSK
	priority=2
}

#如果你的 WiFi 没有密码
network={
    ssid="你的无线网络名称（ssid）"
    key_mgmt=NONE
}

#如果你的 WiFi 使用WEP加密
network={
    ssid="你的无线网络名称（ssid）"
    key_mgmt=NONE
    wep_key0="你的wifi密码"
}

#如果你的 WiFi 使用WPA/WPA2加密
network={
    ssid="你的无线网络名称（ssid）"
    key_mgmt=WPA-PSK
    psk="你的wifi密码"
}
```
说明：
* ssid:网络的ssid
* psk:密码
* priority:连接优先级，数字越大优先级越高（不可以是负数）
* scan_ssid:连接隐藏WiFi时需要指定该值为1

如果你不清楚 WiFi 的加密模式，可以在安卓手机上用 root explorer 打开 /data/misc/wifi/wpa/wpa_supplicant.conf，查看 WiFi 的信息。

> 有线连接,已经ssh连上的情况

```
iwlist scan  # 查看wifi信息



方法一：
配置连接到某个热点:
# 编辑wifi文件
sudo vim /etc/wpa_supplicant/wpa_supplicant.conf
# 在该文件最后添加下面的话
network={
    ssid="WIFINAME"
    psk="password"
}
# 引号部分分别为wifi的名字和密码
# 保存文件后几秒钟应该就会自动连接到该wifi
# 查看是否连接成功
ifconfigwlan0


方法二：
配置树梅派3无线wifi连接

修改/etc/network/interface文件
auto lo
iface lo inet loopback
iface eth0 inet dhcp
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-ssid  接入AP的名字
wpa－psk  接入AP的密码

保存文件，然后运行如下命令重新启动网络！

sudo /etc/init.d/networking restart

```

获取ip


```
命令行输入 arp -a
可以看到同局域网的设备的 ip和mac地址
一般树莓派的mac地址是b开头的

```


设置静态ip

一、使用路由器设置

二、修改/etc/network/interfaces文件设置

```
终端下输入
pi@raspberrypi:~ $ sudo nano /etc/network/interfaces

原先网卡IP是从DHCP服务器获取的，找到下面这一句
iface eth0 inet dhcp
我们需要改为静态IP，将这一句替换为如下内容,
如果找不到这一句就直接填写下面的内容到文件最后
---
iface eth0 inet static
#固定IP地址
address 192.168.1.201
#掩码，可以登录路由器查看
netmask 255.255.255.0
#网关，可以登录路由器查看
gateway 192.168.1.1
#DNS服务器
dns-nameservers 114.114.114.114
---

eth0是有线网卡，如果连接的是无线网络，把eth0改成wlan0
---
iface wlan0 inet static
address 192.168.1.202
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 114.114.114.114
---
```

