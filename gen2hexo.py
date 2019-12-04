import os
import shutil
import sys
import time

base_path = os.path.dirname(os.path.realpath(sys.argv[0]))
build_dir = "_build"
build_path = os.path.join(base_path, build_dir)
dst_dir = "_build/source"
source_path = os.path.join(base_path, dst_dir)
bolg_dir = "_build/source/_posts"
bolg_path = os.path.join(base_path, bolg_dir)


def get_all_file_path(path):
    """获取路径下所有文件的路径"""
    remove_list = ["README.md"]

    all_file_path = []
    for info in os.walk(path):
        if "static" not in info[0]:
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

        dst_path = file_path.replace(current_dir, current_dir + '/' + bolg_dir)
        # print(dst_path)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        with open(os.path.join(dst_path, file_name), "w") as f:
            f.write(content)


def gen_static():
    shutil.copytree(os.path.join(base_path, "static/source/about"), os.path.join(source_path, "about"))
    shutil.copy2(os.path.join(base_path, "static/source/CNAME"), os.path.join(source_path, "CNAME"))

    shutil.copytree(os.path.join(base_path, "static/themes"), os.path.join(build_path, "themes"))
    shutil.copy2(os.path.join(base_path, "static/_config.yml"), os.path.join(build_path, "_config.yml"))


def init_dir():
    """
    打扫目录
    """
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
    os.makedirs(build_path)


def move_file():
    mv_dst_path = os.path.join(base_path, "../source")
    if os.path.exists(mv_dst_path):
        shutil.rmtree(mv_dst_path)

    shutil.move(source_path, mv_dst_path)

    mv_theme_indexs_path = os.path.join(base_path, "../themes/3-hexo/layout/indexs.md")
    if os.path.exists(mv_theme_indexs_path):
        os.remove(mv_theme_indexs_path)
    shutil.copy2(os.path.join(build_path, "themes/3-hexo/layout/indexs.md"), mv_theme_indexs_path)

    mv_theme_config_path = os.path.join(base_path, "../themes/3-hexo/_config.yml")
    if os.path.exists(mv_theme_config_path):
        os.remove(mv_theme_config_path)
    shutil.copy2(os.path.join(build_path, "themes/3-hexo/_config.yml"), mv_theme_config_path)

    mv_hexo_config_path = os.path.join(base_path, "../_config.yml")
    if os.path.exists(mv_hexo_config_path):
        os.remove(mv_hexo_config_path)
    shutil.copy2(os.path.join(build_path, "_config.yml"), mv_hexo_config_path)

    shutil.rmtree(build_path)


def main():
    init_dir()
    all_path = get_all_file_path(base_path)
    gen_file(all_path)
    gen_static()
    move_file()
    pass


if __name__ == "__main__":
    # run()
    main()
    print(__file__)
