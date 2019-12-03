参考： https://blog.csdn.net/nzyalj/article/details/79177291


```
docker pull mysql
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -d mysql
—name 为设置容器的名字
-p 端口映射
-e 为设置执行时的环境变量,其他可参考官网
-d 为设置镜像，镜像名:版本


mysql -h 47.102.125.88 -P 3306 -u root
docker run -it --link mysql:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -p'
-it 使用交互模式
–link 连接运行的容器 mysql.5.7.21 为之前首次运行时创建的容器名，冒号后为镜像名

# 进入容器中的msyql
docker exec -it 9157649a7fdd mysql -h 127.0.0.1 -P 3306 -p
```



2059错误解决

```
原因： 最新的mysql8.0对用户密码的加密方式为caching_sha2_password, django暂时还不支持这种新增的加密方式。只需要将用户加密方式改为老的加密方式即可。


一、

use mysql; #选择数据库
#本地
#更改加密方式
ALTER USER 'root'@'localhost' IDENTIFIED BY 'current_passwd' PASSWORD EXPIRE NEVER;
#更新用户密码
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_passwd';

#远程
#更改加密方式
ALTER USER 'root'@'%' IDENTIFIED BY 'current_passwd' PASSWORD EXPIRE NEVER;
#更新用户密码
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'new_passwd';

FLUSH PRIVILEGES; #刷新权限



二、
use mysql
# 本地
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_passwd';
# 远程
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'new_passwd';
flush privileges;
```


