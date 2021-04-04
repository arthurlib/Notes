git tag ?

# 配置

> 删除

```
vim  ~/.gitconfig
# 删除 origin  的 参数
[remote "origin"]
```

git 修改commit 的注释,最新的一次提交,push过了不行
```
git commit --amend
```

> git配置（提交commit时的签名）
> 下面的是全局设置，单独的话就不带 --global 选项

```
git config --global core.editor vim  #设置默认编辑器
git config -l 所有的配置参数
git config --global user.name "name"
git config --global user.email "email"
```

> ssh与https互换

```
1.修改命令
git remote set-url origin [url]
我这里使用 git remote set-url origin [url]命令，直接修改远程仓库为https的地址

2.先删后加
git remote rm origin
git remote add origin [url]

3.直接修改config文件

以上进行git操作的时候，每次都需要密码，所以可以配置免密
添加内容
https://{username}:{passwd}@github.com
```
> 忽略本地文件修改

```
在使用git时，对于本地配置文件，肯定不必提交，但总是在’git status’中看到文件修改

git update-index --assume-unchanged build/conf/a.conf

要恢复的话，方法如下：
git update-index --no-assume-unchanged build/conf/a.conf

如果想知道当前被忽略修改的本地文件列表，使用如下命令：

git ls-files -v | grep -e "^[hsmrck]"
```


> 配置多个远程仓库

```
输入的时候不需要输入 < 和 >

# 添加一个新远程仓库
# 其中，name 表示你要给这个远程库起的名字，url 表示这个库的地址
git remote add <name> <url>
# 提交的时候
git push <name> <branch>
git push <name> <local branch>:<remote branch>
git pull <name> <branch>
git pull <name> <remote branch>:<local branch>
# 其中，name 表示你在上一步给它起的名字，branch 表示某一个分支

# 删除远程分支
# 一种方式是，可以直接在 github 网页上操作
# 另一种方式是：
git push <name> :<branch> #（注意冒号前的空格）

# 配置远程仓库
git remote add origin https://url

# 再添加一个远程仓库，跟origin一样
git remote set-url --add origin https://url

# 注意这里多次添加需要用
git remote set-url --add
# 不然会报错：
fatal: remote origin already exists.
# 或者改名
git remote add otherOrigin https://url

# 一次提交到所有远程仓库
git push --all

# 注意
git pull 是 git pull (from) origin (to) master
git push 是 git push (to) origin (from) master
```

# 基本操作

```
显示图形界面，显示项目历史
gitk/git gui

初始化一个新仓库
git init

url 路径（可以是本地路径,即目录路径）
git clone url

将更新内容添加到索引中
git add file1 file2
添加全部
git add .

获得当前项目的一个状况
git status

编写.ignore文件

提交一个版本
git commit
会自动把所有内容有修改的文件（不包括新创建的文件），都添加到索引中，并且同时把他们提交
git commit -a
直接提交一个版本
git commit -m "info"

推送到远程仓库
git push
```


# git remote

```
查看有哪些远程仓库
git remote

查看远程仓库的详细信息，列出其远程url
git remote -v

修改远程仓库地址
git remote set-url origin "https://..."

添加远程仓库
git remote add test url

添加或者修改远程仓库地址
git config remote.origin.url "https://..."

删除远程仓库配置
git remote rm origin

添加和删除 global 的 remote.origin.url
git remote --global set-url origin "https://..." 
git config --global remote.origin.url "https://..."



同时推送到多个版本库【既push到github上，又push到开源中国的Git@OSC上】
 首先，先增加第一个地址 git remote add origin <url1>
 然后增加第二个地址 git remote set-url --add origin <url2>
增加第三个地址 git remote set-url --add origin <url3>

```

# git fetch
> git fetch 相当于是从远程获取最新到本地，不会自动merge，

```
将远程仓库的master分支下载到本地当前branch中
git fetch origin master

比较本地的master分支和origin/master分支的差别
git log -p master  ..origin/master

进行合并
git merge origin/master
```
也可以用以下指令：
```
从远程仓库master分支获取最新，在本地建立tmp分支
git fetch origin master:tmp

將當前分支和tmp進行對比
git diff tmp

合并tmp分支到当前分支
git merge tmp

删除temp
git branch -d temp
```


# git pull

> 相当于是从远程获取最新版本并merge到本地

```
下面这句，pull 远程仓库origin的master分支
git pull origin master

从远程仓库origin 拉取tt分支，到本地的分支名为tt2
git pull origin tt:tt2
```

# git diff

```
对比工作区(未 git add)和暂存区(git add 之后)
git diff

对比暂存区(git add 之后)和版本库
git diff --cached
git diff --cached HEAD

对比工作区(未 git add)和版本库
git diff HEAD

显示两个分支间的差异
git diff master..test

显示master,test的共有父分支和test之间的差异
git diff master...test

当前分支与test分支的差别，也可比较某一文件或目录
git diff test

当前工作目录（分支）lib目录与上次提交的差别
git diff HEAD -- ./lib

统计当前哪些文件被改动，有几行改动
git diff --stat


```

# git log

> git log 参数 （有各种参数，功能强大）

```
显示每个提交的被修改文件，以及这些文件分别添加删除了几行
git log --stat

格式化输出
git log --pretty=oneline
git log --pretty=short (medium,full,fuller,email,raw) 自定义 --pretty=format

可视化提交图
git log --graph 

```

# git push

> 不带任何参数的git push，默认只推送当前分支，这叫做simple方式。
> 此外，还有一种matching方式，会推送所有有对应的远程分支的本地分支。
> Git 2.0版本之前，默认采用matching方法，现在改为默认采用simple方式。

```
强制push
git push -f

提交指定仓库，把本地local分支提交到test仓库的master分支
git push test local:master

将当前分支推送到origin主机的对应分支
git push origin

建立本地关联远程分支
git branch --set-upstream-to=origin/<branch> release

建立本地关联远程分支
git push -u origin my_branch
git push --set-upstream origin client_dev


当有多个远程主机仓库时，下面命令将本地的master分支推送到origin主机，
同时指定origin为默认主机，后面就可以不加任何参数使用git push了
git push -u origin master 

使用matching方式，可以在命令行输入：
git config --global push.default matching

使用simple方式，可以在命令行输入：
git config --global push.default simple
可以不加 --global
```

# git branch

```
新建分支
git branch branch_name

获取当前仓库所有分支列表
git branch

获取远程所有分支列表
git branch a

切换分支
git checkout branch_name

创建并切换分支
git checkout -b branchName

合并分支
git merge branch_name

删除分支（只能删除被当前分支合并的分支）
git branch -d branch_name

强制删除分支
git branch -D branch_name 

手动建立追踪关系
git branch --set-upstream master origin/next

删除远程分支
git branch -r -d origin/branch-name
git push origin :branch-name
```

# 撤销回滚操作
```
文件被修改了，但未执行git add操作(working tree内撤销)
git checkout fileName
git checkout .

同时对多个文件执行了git add操作，但本次只想提交其中一部分文件
git reset HEAD <filename>

文件执行了git add操作，但想撤销对其的修改（index内回滚）
# 取消暂存
git reset HEAD fileName
git reset 文件名
# 撤销修改
git checkout fileName

修改的文件已被git commit，但想再次修改不再产生新的Commit
# 修改最后一次提交 
git add sample.txt
git commit --amend -m"说明"

撤销指定文件到指定版本
# 查看指定文件的历史版本
git log <filename>
# 回滚到指定commitID
git checkout <commitID> <filename>

删除最后一次远程提交
git revert HEAD
git push origin master

删除最后一次远程提交，使用reset
git reset --hard HEAD^
git push origin master -f

回滚某次提交
# 找到要回滚的commitID
git log
git revert commitID
```

# git reset

参考: [link](https://dotblogs.com.tw/wasichris/2016/04/29/225157)

> HEAD: 这是当前分支版本顶端的别名，也就是在当前分支你最近的一个提交

> Working Copy/Working Tree: 代表你正在工作的那个(区域)

> Index: index也被称为staging area，是指一整套即将被下一个提交的文件集合。他也是将成为HEAD的父亲的那个commit. Stage 或 Cache,即缓冲器，git add的区域

```
--soft: 保留 Working Tree、Index，HEAD变化（repository 中的档案內容变成与 reset 目标结点一致）
使用情景
1. 当我们想合并「当前结点」与「reset目标结点」间不具太大意义的 commit 纪录(可能是阶段性地频繁提交)时，可以考虑使用 Soft Reset 来让 commit 演进线图较为清晰。

--mixed: 默认，保留Working Tree，Index 和HEAd(Repository文件内容)会变更与目标节点一致。 
使用情景
1. 一样可以达到合并commit节点的效果
2. 移除所有Index中准备要提交的档案（staged files）可执行 git reset HEAD 来unstage所有已列入Index的待提交档案

--keep: 使用命令时，需在新提交之后，可以返回以前的版本并去除后面的提交，三个Working Tree、Index 和HEAd(Repository文件内容)会变更与目标节点一致。（pycharm中smart reset后会把本地变动存在stash中）


--hard: 不保留，重置HEAD、Working Tree、Index，(Repository档案内容)会恢复到目标节点一致
使用情景
1. 放弃目前本地的所有变更，执行 git reset --hard HEAD 来强制恢复资料内容及状态；
2. 或者真的想放弃目标节点之后的所有变更



列出所有记录，复原操作依靠此命令（当想回到原来的状态时）
git reflog

回退到上一个版本（上一个操作），会把最后一次commit后又更改的代码丢弃
回滚pull
git reset --hard ORIG_HEAD 

在没有commit的情况下回滚pull，可以保留之前没有commit的那些更改
git reset --merge ORIG_HEAD

回到之前的某个版本，目标版本之后的提交全部消失,
git reset --hard HEAD
git reset --hard HEAD~2
git reset --hard 版本号
git reset --hard HEAD@{7}
```

# git revote

```
指定要反做的提交版本号，解决冲突，commit即可
git revert -n 版本号

丢弃最近的三个commit，把状态恢复到最近的第四个commit，并且提交一个新的commit来记录这次改变。
git revert HEAD~3

丢弃从最近的第五个commit（包含）到第二个（不包含）,但是不自动生成commit，这个revert仅仅修改working tree和index。
git revert -n master~5..master~2：
```

# git stash

> 暂存未跟踪或忽略的文件
默认情况下，git stash会缓存下列文件：

- 添加到暂存区的修改（staged changes）
- Git跟踪的但并未添加到暂存区的修改（unstaged changes）  
> 但不会缓存一下文件：

- 在工作目录中新的文件（untracked files）
- 被忽略的文件（ignored files

```
保存当前的修改，恢复到当前版本修改前的状态
git stash

给每个stash加一个message，用于记录版本，使用git stash save取代git stash命令。
git stash save "test-cmd-stash"

查看现有stash
git stash list

将缓存堆栈中的stash多次应用到工作目录中，但并不删除stash拷贝
git stash apply命令时可以通过名字指定使用哪个stash，默认使用最近的stash（即stash@{0}）
git stash apply

将缓存堆栈中的第一个stash删除，并将对应修改应用到当前的工作目录下
git stash pop

移除stash,后面可以跟着stash名字
git stash drop stash@{0}

删除所有缓存的stash
git stash clear


查看指定stash的diff，只有修改的文件统计，后面可以跟着stash名字
git stash show

查看特定stash的全部diff
git stash show -p


从stash创建分支， 检出你储藏工作时的所处的提交，重新应用你的工作，如果成功，将会丢弃储藏。
git stash branch testchanges
```


# .ignore

```
忽略某些文件
* \# 以'#' 开始的行，被视为注释.
* \# 忽略掉所有文件名是 foo.txt 的文件.
* foo.txt
* \# 忽略所有生成的 html 文件,
* *.html
* \# foo.html是手工维护的，所以例外.
* !foo.html
* \# 忽略所有.o 和 .a文件.
* *.[oa]
```

# git rebase

> git rebase过程相比较git merge合并整合得到的结果没有任何区别，但是通过git rebase衍合能产生一个更为整洁的提交历史。
如果观察一个衍合过的分支的历史提交记录，看起来会更清楚：仿佛所有修改都是在一根线上先后完成的，尽管实际上它们原来是同时并行发生的。

> 一般我们使用衍合的目的，是想要得到一个能在远程分支上干净应用的补丁，比如某个项目你不是维护者，但是想帮点忙，最好使用衍合处理。
先在自己的一个分支进行开发，当准备向主项目提交补丁的时候，根据最新的orgin/master进行一次衍合操作然后再提交，这样维护者就不需要任何整合工作。

> **实际为：把解决分支补丁同最新主干代码之间的冲突的责任，划转给由提交补丁的人来解决。作为维护项目的人只需要根据你提供的仓库地址做一次快进合并，或者直接采纳你提交的补丁。**

>衍合的风险，请务必遵循如下准则：
一旦分支中的提交对象发布到公共仓库，就千万不要对该分支进行衍合操作。

```
#先切换到其他分支
git checkout dev
git rebase master # 将dev上的c2、c5在master分支上做一次衍合处理
# git提示出现了代码冲突，此处为之前埋下的冲突点，处理完毕后
git add readme # 添加冲突处理后的文件
git rebase --continue # 加上--continue参数让rebase继续处理
切回主分支进行merge
```

# 移除文件以及取消对文件的跟踪

```
* git rm tmp.txt  删除文件并取消文件跟踪，如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 -f（译注：即 force 的首字母），以防误删除文件后丢失修改的内容。
* git rm --cached readme.txt  仅取消文件跟踪
* git rm log/\*.log 可不要反斜杠，删除所有 log/ 目录下扩展名为 .log 的文件
* git rm \*~ 递归删除当前目录及其子目录中所有 ~ 结尾的文件


取消对文件的跟踪还有一个命令：git update-index --assume-unchanged <取消跟踪的文件>
注：该命令只能取消提交到暂存区之前的文件，可以先用git reset <文件名>将暂存区的文件回退到暂存区之前，然后再取消跟踪

认为未改变
git update-index --assume-unchanged config.ini

取消认为未改变
git update-index --no-assume-unchanged config.ini
```

-----------------------------------------------


```
先查看某行代码由谁写的，在哪个commit中提交的：
git blame file_name
其显示格式为： 
commit ID | 代码提交作者 | 提交时间 | 代码位于文件中的行数 | 实际代码
从而获得commit ID，我们就可以知道commit ID了，然后使用命令：git show commitID来看
```




# Git 命令参考手册
参考：  
[git - 移除文件以及取消对文件的跟踪(git rm --cached readme.txt)](https://blog.csdn.net/leedaning/article/details/44976319)

[如何将本地仓库和github仓库关联起来](http://blog.csdn.net/nunchakushuang/article/details/45193109)

[git 官网](https://git-scm.com/)

[Git 中文参考手册 http://gitref.org/zh/index.html](http://gitref.org/zh/index.html)

[Git命令参考手册(文本版)](https://www.oschina.net/question/156344_148084)

[Git命令参考手册(图片版)](http://www.oschina.net/question/156344_147449)

[Git-Book https://git-scm.com/book/zh/v2/](https://git-scm.com/book/zh/v2/)

[Git-Documentation https://git-scm.com/doc](https://git-scm.com/doc)


## github提交commit,contributions不统计显示绿色

需要满足一些条件  
[解决github提交commit,contributions不统计显示绿色的问题](http://www.cnblogs.com/dongliu/p/5782329.html)

