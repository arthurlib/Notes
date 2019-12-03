# python3

## win下

1. 先新建文件夹python_ven_demo，
2. 然后进入该文件夹cd python_ven_demo，
3. 然后搭建虚拟环境：python -m venv . （注：venv 之后一个空格加上一点“.”)

或者

1. 在桌面上直接建立虚拟环境文件夹 及 虚拟环境：直接输入 python -m venv python_ven_demo (虚拟环境文件夹名，直接在桌面建立了文件夹，同时生成了虚拟环境）

> 激活方式：dos 界面进入python_ven_demo/Script，然后输入activate.bat (也可直接输入activate）即可激活环境

> 退出方式：输入deactivate.bat 或 deactivate


## linux下

1. 建立虚拟环境方法相同，进入目标文件夹cd desktop
使用python -m venv python_ven_demo
2. 新建文件夹python_ven_demo，进入 cd python_ven_demo，然后python -m venv .


> 激活方法和windos不同，activate文件在bin文件夹下，而是需要使用  
source activate 命令：
> 退出方式： deactivate

> 3. 包安装  
激活后，输入python2，可进入python2.7环境，输入python3，可进入python3.6环境
pip install 可安装2.7对应的包，pip3可安装3.6对应的包


# python2

> virtualenvwrapper在virtualenv的基础上提供了一些更方便的命令。


```
# 安装
sudo pip install virtualenv
sudo pip install virtualenvwrapper
```

```
# 在~/.bashrc里面加上
export WORKON_HOME=/home/dev/virtualenv  #你创建的虚拟环境所放置的目录
source /usr/local/bin/virtualenvwrapper.sh
# source ~/.bashrc
```



```
mkvirtualenv -p python3 py3env
```
- -p 后面的参数指定python解释器，不写使用系统默认
- py3env 指定目录

```
deactivate # 退出当前虚拟环境
workon [虚拟环境名称] # 使用某个虚拟环境
rmvirtualenv [虚拟环境名称] # 删除某个虚拟环境
lsvirtualenv# 列出所有虚拟环境
```


```
pip freeze -l > packages.txt
pip install -r packages.txt
```
