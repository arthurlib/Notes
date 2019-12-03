## 使用requests和requests_toolbelt上传文件

https://blog.csdn.net/summerpowerz/article/details/80293235

模拟浏览器上传表单

例子1
```python
import time
import datetime
import hashlib
import os
import random
import sys
import requests
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder

url = 'http://XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Referer': url
}

multipart_encoder = MultipartEncoder(
    fields = {
        'save_name': 'test.txt',
        'save_data': ('test.txt', open('test.txt', 'rb'), 'application/octet-stream')
    },
    boundary = '-----------------------------' + str(random.randint(1e28, 1e29 - 1))
)

headers['Content-Type'] = multipart_encoder.content_type
#请求头必须包含一个特殊的头信息，类似于Content-Type: multipart/form-data; boundary=${bound}

responseStr = requests.post(url, data=multipart_encoder, headers=headers)
print(responseStr.text)

```


例子2

```python
import os, random, sys, requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = 'http://127.0.0.1/sendmsg'
argvstr = sys.argv[1:]
argv_dict = {}
for argv in argvstr :
    argv = str(argv).replace("\r\n" , "")
    DICT = eval(argv)
    argv_dict.update(DICT)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Referer': url
    }

multipart_encoder = MultipartEncoder(
    fields={
        'username': argv_dict['username'],
        'pwd': argv_dict['pwd'],
        'type': 'txt',
        'friendfield': argv_dict['friendfield'],
        'friend': argv_dict['friend'],
        'content': argv_dict['content'],
        'file': (os.path.basename(argv_dict['file']) , open(argv_dict['file'], 'rb'), 'application/octet-stream')
        #file为路径
        },
        boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))
    )

headers['Content-Type'] = multipart_encoder.content_type
#请求头必须包含一个特殊的头信息，类似于Content-Type: multipart/form-data; boundary=${bound}

r = requests.post(url, data=multipart_encoder, headers=headers)
print(r.text)
#注意，不要设置cookies等其他参数，否则会报错

# 例子/usr/local/python36/bin/python3 /opt/lykchat/test_upload.py "{'username':'lykchat','pwd':'123456','type':'img','friendfield':'1','friend':'xxxx','content':'恭喜发财','file':'/root/b.jpg'}"
#等同于curl -F "file=@/root/a" 'http://127.0.0.1/sendmsg?username=lykchat&pwd=123456&type=img&friendfield=1&friend=xxxx&content=恭喜发财'

```
