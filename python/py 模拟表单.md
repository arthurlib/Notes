
```python
"""
python模拟表单提交Multipart/form-data
"""
import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://arch.s3.netease.com/hzdev-appci/monkeytest/video/local_task/local_device"
# data = {
#     "token": "n7910ljw1234"
# }
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    # 'Referer': url
}
multipart_encoder = MultipartEncoder(
    fields={
        "token": "n7910ljw1234",
        'file': ("video.mp4", open("video.mp4", 'rb'), 'application/octet-stream')
    },
)
headers['Content-Type'] = multipart_encoder.content_type
r = requests.post(url, data=multipart_encoder, headers=headers)
print(r.text)

# r = requests.post(url, data=data, files={"file": open("video.mp4", "rb")}, )
# print(r)
# print(r.json())
```
