
```bash

#!/bin/bash
# 在腾讯云ubuntu16 64位，测试通过

#建议使用普通用户账号进行安装
# 准备
sudo apt update
sudo echo y | sudo apt install python-pip
python -m pip install -U pip
sudo echo y | apt install unzip
sudo echo y | apt install ipython


# 安装编译工具
sudo echo y | apt install build-essential
# 安装依赖包
sudo echo y | sudo apt install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# 安装可选包
sudo echo y | sudo apt install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# 下载 opencv 包，这里是当前的 2.4 的包
# wget https://github.com/opencv/opencv/archive/2.4.13.4.zip
# 解压
# unzip 2.4.13.4.zip
# 进入目录
# cd opencv-2.4.13.4/

# 下载 opencv 包，这里是当前的 3.0 的包
wget https://github.com/opencv/opencv/archive/3.3.1.zip
# 解压
unzip 3.3.1.zip
# 进入目录
cd opencv-3.3.1/



# 新建一个文件夹用于存放临时文件
mkdir release
# 切换到该临时文件夹：
cd release

# 腾讯云，这个可以。有些时候需要配置 python 包的搜索路径，自己用的时候可以不用配置，以后有需要了在可修改脚本
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
# 下面是树莓派的时候使用
# cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr ..
# 编译，下面的数字代表编译时候的线程数量
make -j2
# 安装
sudo make install


```
