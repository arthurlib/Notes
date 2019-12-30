[rust教程](https://kaisery.github.io/trpl-zh-cn/ch01-01-installation.html)



rustup: 一个管理 Rust 版本和相关工具的命令行工具

安装： curl https://sh.rustup.rs -sSf | sh


更新 Rust

rustup update

卸载 Rust 和 rustup

rustup self uninstall


编译运行

rustc file.rs


fn main() {
    println!("Hello, world!");
}

当看到符号 ! 的时候，就意味着调用的是宏而不是普通函数。

rustfmt: 代码文件格式化工具

cargo: 是rust的构建系统和包管理器

cargo build: 编译，debug
cargo run: 编译运行
cargo check: 检查是否能成功编译
cargo build --release: 正式发布
cargo new movie-lib --lib: 创建lib项目，库工程crate
cargo new movie-lib-test --bin

语法

let x = 5; 定义不可变变量
let mut y = 0; 定义可变变量


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










