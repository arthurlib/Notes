> 向指定登录用户终端上发送信息

```shell
# 指定用户
write user
# 指定终端
write pts/1
# 指定用户某个终端
write user pts/1
# Ctrl+C结束

# 发一次
write user << EOF
    mag
EOF
```

> 不接收消息

```shell
mesg y    #允许其他用户将信息直接显示在你的屏幕上。
mesg n    #不允许其他用户将信息直接显示在你的屏幕上
```
