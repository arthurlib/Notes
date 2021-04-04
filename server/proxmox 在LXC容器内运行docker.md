登录web面板，选择需要

添加权限的容器=>选项=>签名=>打开嵌套，

重启后容器运行Docker不会再报错

---
如果没有效果 手动编辑容器配置文件重启容器即可
```
cd /etc/pve/lxc
vi 机器号.conf
添加三行

lxc.apparmor.profile: unconfined
lxc.cgroup.devices.allow: a
lxc.cap.drop:

```

