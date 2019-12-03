## 打开图像

1. 通过路径

```python
# PIL
from PIL import Image
 
# Image path
im_path = "./a.jpg"
 
# 1. path
im1 = Image.open(im_path)
print (' From image path {}'.format(im1))

```

2. 通过打开图像对象
```python
# PIL
from PIL import Image
 
# Image path
im_path = "./a.jpg"
 
# 2. file
with open(im_path, 'rb') as f:
    im2 = Image.open(f)
    print (' From image file {}'.format(im2))

```

3. 打开图像字符串流
```python
# Platform.
import platform
if ('2.' in platform.python_version()):
    from StringIO import StringIO as Bytes2Data
else:
    from io import BytesIO as Bytes2Data
 
# PIL
from PIL import Image
 
# Image path
im_path = "./a.jpg"
 
# 3. Bytes.
with open(im_path, 'rb') as f:
    im_bytes = f.read()
    im3 = Image.open(Bytes2Data(im_bytes))
    print (' From image bytes {}'.format(im3))

```

4. 打开包含图像的压缩包
```python
# Platform
import platform
if ('2.' in platform.python_version()):
    from StringIO import StringIO as Bytes2Data
elif ('3.' in platform.python_version()):
    from io import BytesIO as Bytes2Data
 from PIL import Image
# Zip
import zipfile
 
# Zip path
zip_path = "./z.zip"
 
# 4. Zip.
z_file = zipfile.ZipFile(zip_path, "r")
for filename in z_file.namelist():
    # Bytes.
    bytes_img = z_file.read(filename)
    if (0 != len(bytes_img)):
        im4 = Image.open(Bytes2Data(bytes_img))
        print(' From zip file {}'.format(im4))
    else: # directory.
        pass

```