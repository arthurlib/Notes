
- FROM scratch: (空镜像)
- FROM busybox: (空镜像 + busybox)
- FROM alpine:  (空镜像 + busybox + apk)apk,包管理工具

例如： python:3.7-alpine

ldd：打印共享的依赖库

用 ldd 查出所需的 .so 文件
将所有依赖压缩成 rootfs.tar 或 rootfs.tar.gz，之后打进 scratch 基础镜像
 
 
 