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

















