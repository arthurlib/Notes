import os
import shutil
import sys
import time

base_path = os.path.dirname(os.path.realpath(sys.argv[0]))
deploy = ".deploy"


def get_all_file_path(path):
    """获取路径下所有文件的路径"""
    remove_list = ["README.md"]

    all_file_path = []
    for info in os.walk(path):
        for file_name in info[2]:
            if not file_name.startswith(".") and \
                    file_name.endswith(".md") and \
                    file_name not in remove_list:
                all_file_path.append(os.path.join(info[0], file_name))
                # print(os.path.join(info[0], file_name))
    return all_file_path


# 获取文件的修改时间
def get_file_modify_time(file_path):
    """获取文件的修改时间"""
    time_struct = time.localtime(os.path.getmtime(file_path))
    return time.strftime('%Y/%m/%d %H:%M:%S', time_struct)


def gen_file(all_path):
    format_str = """
---
title: {title}
date: {date}
categories: 
{categories}
---
{content}

"""
    for path in all_path:
        content = ""
        # 当前根目录
        current_dir = base_path.split('/')[-1]
        # 文件所在的目录
        file_path = os.path.dirname(path)
        file_path_list = file_path.split('/')

        file_name = os.path.basename(path)
        with open(path, "r") as f:
            content = f.read()
        content = format_str.format(
            title=os.path.basename(path),
            date=get_file_modify_time(path),
            categories="\n".join(["- " + i for i in file_path_list[file_path_list.index(current_dir) + 1:]]),
            content=content
        )
        # print(path)

        dst_path = file_path.replace(current_dir, current_dir + '/' + deploy)
        # print(dst_path)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        with open(os.path.join(dst_path, file_name), "w") as f:
            f.write(content)


def set_index_about():
    pass


def run():
    deploy_path = os.path.join(base_path, deploy)
    if os.path.exists(deploy_path):
        shutil.rmtree(deploy_path)

    all_path = get_all_file_path(base_path)
    gen_file(all_path)


if __name__ == "__main__":
    run()
    print(__file__)
