> 检测zsh

```shell
zsh --version
# 没有的话
apt install zsh
```

> on-my-zsh 安装

一、自动安装

```shell
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh
```

二、手动安装

1. 克隆仓库

```shell
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

2. 创建一个新的zsh配置文件

```shell
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

4. 改变默认的Shell

```shell
chsh -s /bin/zsh
```

5. 设置

```shell
# 在 ~/.zshrc 最后添加 .bash_profile

source ~/.bash_profile

# 重载配置文件
source ~/.zshrc
```
