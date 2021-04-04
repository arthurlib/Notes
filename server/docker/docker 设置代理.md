```
# 重启docker
$ sudo systemctl restart docker
# 对应的旧的命令，其实现在还是支持，效果和上一句一样。
$ sudo service docker restart
# 设置开机启动
$ sudo systemctl enable docker
```

默认情况下这个配置文件夹并不存在，我们要创建它
```
$ mkdir -p /etc/systemd/system/docker.service.d
```

创建一个文件 /etc/systemd/system/docker.service.d/http-proxy.conf
```
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:80/"
```

如果有局域网或者国内的registry，我们还需要使用 NO_PROXY 变量声明一下，比如你可以能国内的daocloud.io放有镜像:
```
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:80/" "NO_PROXY=localhost,127.0.0.1,daocloud.io"
```

刷新systemd配置:
```
$ sudo systemctl daemon-reload
```

用系统命令验证环境变量加上去没
```
$ systemctl show --property=Environment docker
Environment=HTTP_PROXY=http://proxy.example.com:80/
```

重启docker
```
$ sudo systemctl restart docker
```

