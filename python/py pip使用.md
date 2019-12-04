[pip指南](http://chenjiee815.github.io/pipzhi-nan.html)

# pip使用

> pip 安装特定版本的 Python 包

```python
pip install -v pycrypto==2.3
```


> python 使用豆瓣的pypi源  
http://pypi.douban.com/simple/   
注意后面要有/simple目录。 使用镜像源很简单，用-i指定就行了：   

```
sudo easy_install -i http://pypi.douban.com/simple/ saltTesting   
sudo pip install -i http://pypi.douban.com/simple/ saltTesting
```


>  使用requirements.txt

生成
```
pip freeze > requirements.txt
```

安装，在另一个环境下使用
```
pip install -r requirements.txt
```
