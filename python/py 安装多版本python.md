#### 推荐： pyenv

github: https://github.com/pyenv/pyenv#installation

use: http://einverne.github.io/post/2017/04/pyenv.html  
https://www.jianshu.com/p/af1f8d7b6b31


#### 2 ubuntu安装py3.7

```bash
# 01、首先更新软件包列表并安装先决条件：
sudo apt update
sudo apt install software-properties-common
# 02、接下来，将deadsnakes PPA添加到您的源列表：
sudo add-apt-repository ppa:deadsnakes/ppa
# 出现提示时按Enter继续：
# Press [ENTER] to continue or Ctrl-c to cancel adding it.
# 03、启用存储库后，使用以下命令安装Python 3.7：
sudo apt install python3.7
```


#### 源码安装

```bash
#01、首先更新包列表并安装构建Python源所需的包：
sudo apt update
sudo apt install build-essential zlib1g-dev libncurswget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xzes5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
#02、使用以下wget命令从Python下载页面下载最新版本的源代码
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
#03、下载完成后，解压压缩包
tar -xf Python-3.7.2.tar.xz
#04、接下来，导航到Python源目录并运行configure脚本，该脚本将执行大量检查以确保系统上存在所有依赖项
cd Python-3.7.2


## 配置安装路径情况
./configure --prefix=/usr/local/python3.7.2 
# 编译
make
# 测试没问题
make test
# 安装
make install



## 不配置安装路径情况
./configure --enable-optimizations
#--enable-optimizations选项将通过运行多个测试来优化Python二进制文件，这将使构建过程变慢。
#05、使用make启动Python构建过程, -j 使用几核心进行编译
make -j 8
#06、构建完成后，键入以下命令安装Python二进制文件：
sudo make altinstall
#不要使用标准的make install，因为它会覆盖默认的系统python3二进制文件

```
