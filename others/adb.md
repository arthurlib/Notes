列出设备

```
adb devices
```
启动关闭adb服务
```
adb start-server
adb kill-server
```


安装apk
```
adb -s 选择设备名 
adb -s emulator-5554 install taobao.apk
adb install -r apk.apk
```

无线连接

```bash
# 先用usb线连接android手机，然后输入如下指令：adb tcpip 端口号,端口号默认为5555
adb tcpip 5555

# 通过adb连接ip地址
adb connect ip地址
```

获取文件
```
adb -s device pull src_path to_path
```

开启关闭adb服务

```
adb kill-server
在关闭adb服务后，要使用如下的命令启动adb服务。
adb start-server
```


