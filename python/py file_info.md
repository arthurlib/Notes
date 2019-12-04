```python
# coding:utf8
"""
文件、路径方面的操作
"""
import os
import time


def get_all_file_path(path):
    """获取路径下所有文件的路径"""
    all_file_path = []
    for info in os.walk(path):
        for file_name in info[2]:
            all_file_path.append(os.path.join(info[0], file_name))
    return all_file_path


# 把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
def timestamp2time(timestamp):
    """把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12"""
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


# 获取文件的大小,结果保留两位小数，默认单位单位为 KB
def get_file_size(file_path, unit=1, reserved=2):
    """获取文件的大小,结果保留两位小数，默认单位单位为 KB"""
    file_size = os.path.getsize(file_path)
    file_size = file_size / float(1024 ** unit)
    return round(file_size, reserved)


# 获取文件的访问时间
def get_file_access_time(file_path):
    """获取文件的访问时间"""
    t = os.path.getatime(file_path)  # 得到时间戳
    return timestamp2time(t)


# 获取文件的创建时间v
def get_file_create_time(file_path):
    """获取文件的创建时间"""
    t = os.path.getctime(file_path)
    return timestamp2time(t)


# 获取文件的修改时间
def get_file_modify_time(file_path):
    """获取文件的修改时间"""
    t = os.path.getmtime(file_path)
    return timestamp2time(t)
```
