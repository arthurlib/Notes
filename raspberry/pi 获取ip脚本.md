
```bash
#!/bin/bash

sleep 10s
IP=`ifconfig | grep inet | sed -n '4p'| awk -F ' ' '{print $2}' | awk -F ':' '{print $2}'`
echo $IP
`/home/pi/init/pcd8544_rpi ${IP}`

```
