视频拼接参考： https://www.jianshu.com/p/98a0c091c4bf  
ffmpeg下载： http://ffmpeg.org/  
拼接参考： https://blog.csdn.net/east196/article/details/79821361

```python
import os
import tempfile

def get_temp_file(self, data, suffix=None):  # 传入缓存路径，数据，文件后缀例如 ".txt"
    """临时文件，需要close, tmp_file_obj.close()"""
    if not os.path.exists(self.tempfile_tmp_path):
        os.makedirs(self.tempfile_tmp_path)
    tmp_file_obj = tempfile.NamedTemporaryFile(suffix=suffix, dir=self.tempfile_tmp_path)
    tmp_file_obj.write(data)
    tmp_file_obj.seek(0)
    return tmp_file_obj
```


```
import os
import shutil
import threading
import uuid


class DataUtils(object):

    def __init__(self, storage_path="/data/report"):
        # 文件存储路径
        self.storage_path = storage_path
        # 缓存路径
        self.tmp_path = os.path.join(storage_path, "tmp/").replace("\\", "/")

    def save_data(self, task_id, device_id, file_obj, path=None):
        """保存文件，同名覆盖.
        path传入绝对路径的话只有path生效，相对路径的话，path会添加到file_path后面
        """

        file_path = os.path.join(self.storage_path, task_id, device_id).replace("\\", "/")
        file_name = file_obj.name.replace("\\", "/").split("/")[-1]

        if path:
            dir_name = os.path.dirname(path)
            base_name = os.path.basename(path)
            if dir_name:
                file_path = os.path.join(file_path, dir_name).replace("\\", "/")
            if base_name:
                file_name = base_name

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        dst_path = os.path.join(file_path, file_name).replace("\\", "/")

        # 保存
        if 'b' in file_obj.mode:
            with open(dst_path, "wb") as f:
                f.write(file_obj.read())
                return

        with open(dst_path, "w") as f:
            f.write(file_obj.read())

    def async_save_data(self, task_id, device_id, file_obj, path=None):
        threading.Thread(target=self.save_data, args=(task_id, device_id, file_obj, path)).start()

    def stitching_video_mp4(self, task_id, device_id, video_path=None, dst_path="video.mp4"):
        """将目录下多个mp4视频拼接成一个,系统需要安装ffmpeg，并加入环境变量
        video_path 要合并的视频所在目录，
        dst_path传入绝对路径的话只有dst_path生效，相对路径的话，dst_path会添加到file_path后面
        """
        if not dst_path.endswith('.mp4'):
            raise RuntimeError("dst_path，目标路径必须以 '.mp4' 结尾")

        if not video_path:
            video_path = os.path.join(self.storage_path, task_id, device_id, 'video').replace("\\", "/")  # 视频源默认目录
        else:
            video_path = video_path.replace('\\', '/')

        # 目录不存在就返回
        if not os.path.exists(video_path) or not os.path.isdir(video_path):
            raise RuntimeError("video_path 参数路径不存在或者不是目录: " + str(video_path))

        video_list = []
        for name in os.listdir(video_path):
            if name.endswith(".mp4"):
                video_list.append(name.split('.')[0])

        # 没有 mp4 就返回
        if not video_list:
            return

        if not os.path.exists(self.tmp_path):  # 检查 tmp 目录是否存在
            os.makedirs(self.tmp_path)
        tmp_output_path = os.path.join(self.tmp_path, str(uuid.uuid1()) + '.mp4').replace("\\", "/")  # 临时video文件路径

        cmd_ts = "echo y | ffmpeg -i %s -vcodec copy -acodec copy -vbsf h264_mp4toannexb %s"
        cmd_out = 'echo y | ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s'
        video_list.sort()  # 视频拼接顺序
        src_list = []
        out_ts_list = []
        for video_name in video_list:
            src_path = os.path.join(video_path, video_name + ".mp4").replace("\\", "/")
            ts_path = os.path.join(video_path, video_name + ".ts").replace("\\", "/")
            get_ts = cmd_ts % (src_path, ts_path)

            os.system(get_ts)
            src_list.append(src_path)
            out_ts_list.append(ts_path)
        get_out = cmd_out % ("|".join(out_ts_list), tmp_output_path)  # 生成临时video文件
        os.system(get_out)

        for ts in out_ts_list:  # 删除中间文件
            os.remove(ts)

        if os.path.exists(tmp_output_path):  # 临时文件存在
            # 拼接后的文件生成了才可以删除源文件，但是相同目录存在同名文件的情况不能处理，应对cmd异常。
            for ts in src_list:
                os.remove(ts)  # 删除源目录文件
            output_path = os.path.join(video_path, os.path.dirname(dst_path)).replace("\\", "/")  # 存储目录路径
            if not os.path.exists(output_path):  # 创建目标路径
                os.makedirs(output_path)
            output_path = os.path.join(output_path, os.path.basename(dst_path)).replace("\\", "/")  # 存储文件路径
            # 移动到目标路径
            shutil.move(tmp_output_path, output_path)
            # return output_path
        # return None

    def async_stitching_video_mp4(self, task_id, device_id, video_path=None, dst_path="video.mp4"):
        threading.Thread(target=self.stitching_video_mp4, args=(task_id, device_id, video_path, dst_path)).start()

```
