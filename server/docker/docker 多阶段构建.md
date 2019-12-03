#### 使用多阶段构建

为解决以上问题，Docker v17.05 开始支持多阶段构建 (multistage builds)。使用多阶段构建我们就可以很容易解决前面提到的问题，并且只需要编写一个 Dockerfile：

> 例如，编写 Dockerfile 文件

```
FROM golang:1.9-alpine as builder
RUN apk --no-cache add git
WORKDIR /go/src/github.com/go/helloworld/
RUN go get -d -v github.com/go-sql-driver/mysql
COPY app.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .
FROM alpine:latest as prod
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/go/helloworld/app .
CMD ["./app"]
```

> 构建镜像

```
$ docker build -t go/helloworld:3 .
```


> 只构建某一阶段的镜像

我们可以使用 as 来为某一阶段命名，例如

```
FROM golang:1.9-alpine as builder
```

例如当我们只想构建 builder 阶段的镜像时，增加 --target=builder 参数即可

```
$ docker build --target builder -t username/imagename:tag .
```

> 构建时从其他镜像复制文件

上面例子中我们使用 COPY --from=0 /go/src/github.com/go/helloworld/app .从上一阶段的镜像中复制文件，我们也可以复制任意镜像中的文件。

```
COPY --from=nginx:latest /etc/nginx/nginx.conf /nginx.conf
```
