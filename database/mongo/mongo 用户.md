查看数据库

```
show dbs
```

新mongo没有admin,创建

```
use admin
db.createUser(
  {
    user: "admin",
    pwd: "admin",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```


启用 auth

```
vi /etc/mongod.conf
修改
auth=true
重启 mongod 服务：
service mongod restart

or
./mongod --auth  # 启用认证
```

创建新库带用户密码的

在那个库下create，就是那个db的用户，不过首先需要 auth admin

```
认证登录
use admin
db.auth("admin", "password")

为自己的库创建用户
use mydb
db.createUser(
  {
    user: "myuser",
    pwd: "myuser",
    roles: [ { role: "readWrite", db: "mydb" } ]
  }
)
# or,权限不一样
db.createUser(
  {
    user: "myuser",
    pwd: "myuser",
    roles: [ { role: "dbOwner", db: "mydb" } ]
  }
)


# auth mydb

use mydb
db.auth("myuser","myuser")
```

其他：

```
# 查看系统用户
use admin
db.system.users.find()  # 显示当前系统用户

# 授予角色：db.grantRolesToUser( "userName" , [ { role: "<role>", db: "<database>" } ])
db.grantRolesToUser( "myuser" , [ { role: "dbOwner", db: "mydb" } ])

# 取消角色：db.grantRolesToUser( "userName" , [ { role: "<role>", db: "<database>" } ])
db.revokeRolesFromUser( "myuser" , [ { role: "readWrite", db: "mydb" } ])


# 删除用户
use mydb
db.dropUser("myuser")
# 删除用户的时候需要切换到用户管理的数据库才可以删除；
```
