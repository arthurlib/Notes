
1. 先将home目录下系统默认的文件夹名称改为英文，手动操作，也可以参考以下脚本
```bash
name=`whoami`;
#echo $name
#可以将第二步骤的内容保存到文件中，命名user-dirs.dirs，打开下面一句的注释，执行该脚本。
#我忘记这个命令能不能生效了，暂时没有时间重新测试
#cp /home/$name/linux/config/user-dirs.dirs /home/$name/.config/user-dirs.dirs;echo user-dirs.dirs 复制完成;
mv /home/$name/图片 /home/$name/Pictures;
mv /home/$name/桌面 /home/$name/Desktop;
mv /home/$name/下载 /home/$name/Downloads;
mv /home/$name/模板 /home/$name/Templates;
mv /home/$name/公共的 /home/$name/Public;
mv /home/$name/文档 /home/$name/Documents;
mv /home/$name/音乐 /home/$name/Music;
mv /home/$name/视频 /home/$name/Videos;
echo home文件夹重命名完成;


```
2. 进入~/.config/user-dirs.dirs，将里面的内容改为如下,其中的英文要与你文件夹的名称对应
```
# This file is written by xdg-user-dirs-update
# If you want to change or add directories, just edit the line you're
# interested in. All local changes will be retained on the next run
# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped
# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an
# absolute path. No other format is supported.
#
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="$HOME/Documents"
XDG_MUSIC_DIR="$HOME/Music"
XDG_PICTURES_DIR="$HOME/Pictures"
XDG_VIDEOS_DIR="$HOME/Videos"

```

3. 重启或者注销，应该就能生效了