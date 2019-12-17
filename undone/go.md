[go教程](https://github.com/unknwon/the-way-to-go_ZH_CN/blob/master/eBook/directory.md)


go build 编译自身包和依赖包
go install 编译并安装自身包和依赖包
你可以通过如下命令安装：
go install codesite.ext/author/goExample/goex
包安装到本地它会从远端仓库下载包：检出、编译和安装一气呵成

go get github.com/NNNN/uc。 下载包


gofmt 格式化代码
在命令行输入 gofmt –w program.go 会格式化该源文件的代码然后将格式化后的代码覆盖原始内容（如果不加参数 -w 则只会打印格式化后的结果而不重写文件）；gofmt -w *.go 会格式化并重写所有 Go 源文件；gofmt map1 会格式化并重写 map1 目录及其子目录下的所有 Go 源文件。


生成代码文档 godoc使用 go doc args
godoc -http=:6060


go fix 用于将你的 Go 代码从旧的发行版迁移到最新的发行版，它主要负责简单的、重复的、枯燥无味的修改工作，如果像 API 等复杂的函数修改，工具则会给出文件名和代码行数的提示以便让开发人员快速定位并升级代码
go test 是一个轻量级的单元测试框架


反引号
`
原始字符串
`

    

#### 环境变量设置

```
# 安装目录
export GOROOT=go的安装目录
# 工作目录
export GOPATH=/Users/zhu/go_workspace/s4s:/Users/zhu/go_workspace/go:/Users/zhu/go_workspace/test
# 把所有工作目录下的bin目录加入path
export PATH=$PATH:${GOPATH//://bin:}/bin
```

#### 导包

* 相对路径     import   "./model"  
//当前文件同一目录的model目录，但是不建议这种方式import
* 
* 绝对路径    import   "shorturl/model"  
//加载GOPATH/src/shorturl/model模块


1. 点操作: import( . “fmt” ) 可以不通过包名来使用其中的项目
2. 别名操作: import( f “fmt” )
3. _操作 import(_“github.com/ziutek/mymysql/godrv” )
> _操作其实只是引入该包。当导入一个包时，它所有的init()函数就会被执行，  
但有些时候并非真的需要使用这些包，仅仅是希望它的init()函数被执行而已。  
这个时候就可以使用_操作引用该包了。即使用_操作引用包是无法通过包名来调用包中的导出函数，  
而是只是为了简单的调用其init函数()。



#### go get 无反应、访问github.com速度慢、没反应问题的解决方案

修改host，下面是一个示例，可以用[IP查找工具](https://www.ipaddress.com/ip-lookup)来获取IP地址设置hosts，速度杠杠的
```
vim /etc/hosts
192.30.253.112 github.com
151.101.185.194 github.global.ssl.fastly.net

```


#### 交叉编译

- GOOS：目标平台的操作系统（darwin、freebsd、linux、windows） 
- GOARCH：目标平台的体系架构（386、amd64、arm） 
- 交叉编译不支持 CGO 所以要禁用它

> Mac 下编译 Linux 和 Windows 64位可执行程序

```
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```

> Linux 下编译 Mac 和 Windows 64位可执行程序

```
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```

> Windows 下编译 Mac 和 Linux 64位可执行程序

```
SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=amd64
go build main.go

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build main.go
```

**上面的命令编译 64 位可执行程序，你当然应该也会使用 386 编译 32 位可执行程序**


#### 解决 golang org x 下包下载不下来的问题


```
由于众所周知的原因，golang在下载golang.org的包时会出现访问不了的情况。尤其是x包，很多库都依赖于它。由于x包在github上都有镜像，我们可以使用从github.com上把代码clone到创建的golang。org/x目录上就OK了

git clone https://github.com/golang/sys.git
```



```
golang.org/x包放到了https://github.com/golang/text中，下载时需要先在本地建立golang.org/x的目录后，再下载。

mkdir -p golang.org/x
git clone https://github.com/golang/text.git
或
go get github.com/golang/text后将包移到x目录

```


#### init 函数

变量除了可以在全局声明中初始化，也可以在 init 函数中初始化。这是一类非常特殊的函数，它不能够被人为调用，而是在每个包完成初始化后自动执行，并且执行优先级比 main 函数高。


#### 字符串拼接
在循环中使用加号 + 拼接字符串并不是最高效的做法，更好的办法是使用函数 strings.Join()（第 4.7.10 节），有没有更好地办法了？有！使用字节缓冲（bytes.Buffer）拼接更加给力


#### 定时任务
如果你需要在应用程序在经过一定时间或周期执行某项任务（事件处理的特例），则可以使用 time.After 或者 time.Ticker：我们将会在第 14.5 节讨论这些有趣的事情。 另外，time.Sleep（Duration d） 可以实现对某个进程（实质上是 goroutine）时长为 d 的暂停


#### 静态编译

```
GOOS=linux CGO_ENABLED=0 go build -ldflags="-s -w" -o app app.go

你可能有人还使用-a参数，它强制重新编译相关的包,一般你不会使用它。

-s 忽略符号表和调试信息，-w忽略DWARF符号表，通过这两个参数，可以进一步减少编译的程序的尺寸，更多的参数可以参考go link, 或者 go tool link -help(另一个有用的命令是go tool compile -help)。

你也可以使用strip工具对编译的Go程序进行裁剪。

本身Go是静态编译的， 对于CGO, 如果设置CGO_ENABLED=0,则完全静态编译，不会再依赖动态库
```




