用于创建临时文件或者临时文件夹

```python
import tempfile


# 创建临时文件
def test_mkstemp():
    # 说明：该方法仅仅创建一个临时文件；返回包含两个元素的元组，
    # 第一个元素指操作该临时文件的安全级别，第二个元素指该临时文件的路径
    file = tempfile.mkstemp(suffix=".txt", prefix="tmp", dir="./tmp", text=True)
    print(file)
    with open(file[0], "w+") as f:
        f.write("aaa\nbbb")
        f.seek(0)
        print(f.readlines())


def test_TemporaryFile():
    # 说明：该方法返回一个文件对象用于临时数据保存，它没有文件名字，你也找不到它所在的位置；
    # 当文件对象被close或者被del的时候，临时文件将从磁盘上删除。
    temp = tempfile.TemporaryFile()  # 参数同上
    try:
        print('temp:', temp)
        print('temp.name:', temp.name)
        # 写入
        temp.write(b"hello world\n")
        temp.seek(0)
        # 读取
        print('temp.read:', temp.read())
    finally:
        # 自动清除文件
        temp.close()


def test_NamedTemporaryFile():
    # 说明：同tempfile.TemporaryFile类似，主要区别就是多了个delete参数，
    # 用于指定文件对象close或者被del之后，是否也一同删除磁盘上的临时文件
    # （当delete = True的时候，即默认的时候行为与TemporaryFile一样）。
    temp = tempfile.NamedTemporaryFile(suffix='.sh', prefix='script_', dir='/tmp')
    try:
        temp.write(b'aaaa\n')
        # 指定从什么位置写入
        temp.seek(0)
        print(temp.read())
    finally:
        # 自动清除文件，因为delete参数默认是True
        temp.close()


# seek有三种写入模式：seek(offset,where): where=0从起始位置移动，1从当前位置移动，2从结束位置移动。

def test_SpooledTemporaryFile():
    # 将 BytesIO或者StringIO转换成临时文件
    file = tempfile.SpooledTemporaryFile()
    file.write(b"asdasdasd")
    file.seek(0)
    print(file.read())


def test_mkdtemp():
    path = tempfile.mkdtemp("tmptmp")
    print(path)  # 要手动处理文件夹删除

```
