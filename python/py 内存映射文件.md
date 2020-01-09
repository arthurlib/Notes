server.py
```python
import mmap
import contextlib
import time

with open("test.dat", "w") as f:
    f.write('\x00' * 1024)

with open('test.dat', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_WRITE)) as m:
        for i in range(1, 10001):
            m.seek(0)
            s = bytes("msg this is a test " + str(i), encoding="utf8")
            s.rjust(1024, b'\x00')
            m.write(s)
            m.flush()
            time.sleep(1)

```

client.py
```python
import mmap
import contextlib
import time

while True:
    with open('test.dat', 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)) as m:
            s = m.read(1024).replace(b'\x00', b'')
            print(s)
    time.sleep(1)

```
