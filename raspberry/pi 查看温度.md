> 方法一

```shell
pi@RaspberryPi:~ $ /opt/vc/bin/vcgencmd measure_temp
 #temp=51.5'C 1 2 
```

> 方法二

```shell
pi@RaspberryPi:~ $ cat /sys/class/thermal/thermal_zone0/temp 
# 50464 1 2 此处，除以1000，单位是℃。 1
```