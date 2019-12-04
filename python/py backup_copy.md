```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
拷贝文件目录，不重复拷贝，修改过的会覆盖，源中删除的会目标中也会删除
"""
import shutil
import os


def copy(src, dst):
    next_list = []
    src_list = os.listdir(src)
    dst_list = os.listdir(dst)
    for src_name in src_list:
        src_path = os.path.join(src, src_name).replace('\\', '/')
        dst_path = os.path.join(dst, src_name).replace('\\', '/')
        if src_name not in dst_list:  # dst不存在
            if os.path.isdir(src_path):
                os.mkdir(dst_path)
                next_list.append((src_path, dst_path))
            else:
                shutil.copy2(src_path, dst_path)
        else:
            if os.path.isfile(src_path):
                if os.path.getmtime(src_path) > os.path.getmtime(dst_path):
                    shutil.copy2(src_path, dst_path)
    for dst_name in dst_list:
        if dst_name not in src_list:
            dst_path = os.path.join(dst, dst_name).replace('\\', '/')
            if os.path.isfile(dst_path):
                os.remove(dst_path)
            else:
                shutil.rmtree(dst_path)

    return next_list


def main(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    next_list = [(src, dst)]
    for src, dst in next_list:
        next_list += copy(src, dst)


if __name__ == "__main__":
    main('./tmp', './ss')
```
