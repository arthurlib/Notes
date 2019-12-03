
### useradd与adduser

#### centos:
useradd与adduser是没有区别的都是在创建用户，在home下自动创建目录，没有设置密码，需要使用passwd命令修改密码。

#### ubuntu:

- adduser: 会在/home下自动创建与用户名同名的用户目录，系统shell版本，会在创建时会提示输入密码，更加友好。
- useradd: 不会在/home下自动创建与用户名同名的用户目录，而且不会自动选择shell版本，也没有设置密码，那么这个用户是不能登录的，需要使用passwd命令修改密码。
    * -d： 指定用户的主目录
    * -m： 如果存在不再创建，但是此目录并不属于新创建用户；如果主目录不存在，则强制创建； -m和-d一块使用。
    * -s： 指定用户登录时的shell版本
    * -M： 不创建主目录


##### 指定密码

```
passwd username
```

### userdel

- userdel username: 删除用户，只能删除用户
- userdel -r username: 可以删除用户及相关目录。

