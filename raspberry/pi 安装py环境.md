
示例，根据实际安装py版本，完了之后环境搞搞
```
# 安装编译所需依赖包
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

# 安装SSL依赖
sudo apt-get install libssl-dev


# 到官网下载Python3.6.6： https://www.python.org/downloads/source/
wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz

# 解压
tar xf Python-3.6.6.tar.xz 

# 进入目录
cd Python-3.6.6

# 开始编译（时间漫长，需要等待，建议用&&把三句连在一起执行）
sudo  ./configure
sudo make
sudo make install

# 升级pip
sudo python3.6 -m pip install --upgrade pip
```

