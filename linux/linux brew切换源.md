
```
第一步，替换brew.git

cd “$(brew --repo)”
git remote -v

可以看到官方镜像是https://github.com/Homebrew/homebrew

git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

第二步：替换homebrew-core.git

cd “$(brew --repo)/Library/Taps/homebrew/homebrew-core”
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

再次使用brew update进行更新，发现速度变的很快。
至此替换镜像完成，我们将官方镜像替换成了中科大的镜像。
```
