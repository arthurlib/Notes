
cargo: 是rust的构建系统和包管理器

* cargo build: 编译，debug
* cargo run: 编译运行
* cargo check: 检查是否能成功编译
* cargo build --release: 正式发布
* cargo new movie-lib --lib: 创建lib项目，库工程crate
* cargo new movie-lib-test --bin
* cargo doc 功能，开发者可以通过这个命令将工程中的说明注释转换成 HTML 格式的说明文档。


### 换源

换源：为rust crates.io换上国内中科大的源
中科大说明： [https://lug.ustc.edu.cn/wiki/mirrors/help/rust-crates](https://lug.ustc.edu.cn/wiki/mirrors/help/rust-crates)

1. 进入当前用户的 .cargo 目录 cd ~/.cargo
2. 新建名字叫 config 的文件
3. 编辑 config 文件写入

```bash
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'ustc'
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
```
如果所处的环境中不允许使用 git 协议，可以把上述地址改为：

registry = "https://mirrors.ustc.edu.cn/crates.io-index"


### 更改依赖库存放位置

cargo build会把rust工程的外部依赖的源代码放到~/.cargo目录

CARGO_HOME来设置放置依赖代码的位置，如果要设置固定路径直接设置环境变量即可


目前可以通过设置脚本的方式来把每个工程的依赖代码保存在自己的工程目录里：
把下面的脚本保存成env.cmd(名字随便取），然后在放在rust工程目录下，
以后每次都通过这个脚本启动的命令行来运行cargo build，这样代码就会在当前目录下的.cargo里了

```
set PROMPT=$g$s
set CARGO_HOME=%~dp0\.cargo
%~d0
cls
start cmd.exe
```

可以把这个env.cmd复制到每个rust工程目录下，这样每个工程的依赖代码都保存在自己的目录下

