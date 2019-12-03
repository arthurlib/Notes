参考： https://www.jianshu.com/p/e9ce1a7e1ed1

error: CRON[8380]: (CRON) info (No MTA installed, discarding output)

```
如果crontab任务有想控制台打印信息，那么会发送邮件。
这时候如果没有安装邮件服务器会日志报错

解决： 
在crontab中首行添加：

MAILTO=""   # 可以阻止发送邮件

* * * * * task >/dev/null 2>&1   # 任务输出重定向

```



crontab日志

```
sudo vim /etc/rsyslog.conf

1. 找到 cron.*    /var/log/cron.log 这一行，取消注释，保存退出

sudo /etc/init.d/rsyslog restart

然后可以在  /var/log/cron.log  查看日志信息


2. 在 /var/log/syslog 里也能看到 crontab 的日志，即使不开启这个。

```



### 开启crontab日志

> crontab默认情况下是不执行开启日志的

步骤

1. 修改rsyslog服务，将 /etc/rsyslog.d/50-default.conf  文件中的 #cron.* 前的 # 删掉
2. 重启rsyslog服务： service rsyslog restart
3. 然后再重启crontab服务： service cron restart

之后，在这个位置 /var/log/cron.log 就可以查看定时任务的文件日志文件了

> 查看crontab的状态 

```
service cron status
```

> 查看运行时的日志文件，如果在日志文件中执行一条语句后出现：  
No MTA installed, discarding output  
则crontab执行脚本时是不会直接错误的信息输出，而是会以邮件的形式发送到邮箱里，需要邮件服务器了，如果没有安装邮件服务器，它就会报这个错。  
可以在每条定时脚本后面加入：  
> /dev/null 2 > &1  
即将所有信息输入到linux系统中的空设备/dev/null中。  
即可解决No MTA installed, discarding output的问题。


如果两个文件同时存在，那么/etc/cron.allow 优先。  
如果两个文件都不存在，那么只有超级用户可以安排作业。



> ubuntu
```
$sudo /etc/init.d/cron start
$sudo /etc/init.d/cron stop
$sudo /etc/init.d/cron restart
```

> 参数

- /etc/cron.deny: 表示不能使用crontab 命令的用户  
- /etc/cron.allow:  表示能使用crontab 的用户。  

```
-u user：用来设定某个用户的crontab服务；

file：file是命令文件的名字,表示将file做为crontab的任务列表文件并载入crontab。如果在命令行中没有指定这个文件，crontab命令将接受标准输入（键盘）上键入的命令，并将它们载入crontab。

-e：编辑某个用户的crontab文件内容。如果不指定用户，则表示编辑当前用户的crontab文件。文件存放在 /var/spool/cron/crontabs 文件夹下并且以用的的名字命名的文件

-l：显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容。

-r：从/var/spool/cron目录中删除某个用户的crontab文件，如果不指定用户，则默认删除当前用户的crontab文件。

-i：在删除用户的crontab文件时给确认提示。

```

> crontab的文件格式

* 第1列分钟0～59
* 第2列小时0～23（0表示子夜）
* 第3列日1～31
* 第4列月1～12
* 第5列星期0～7（0和7表示星期天）
* 第6列要运行的命令,绝对路径

```
*/1 * * * * cmd 表示每隔一分钟
*/60  * * * * #每60分钟即每小时执行一次
*/105 * * * * #每105分钟执行一次
@reboot cmd # 开机执行
```
