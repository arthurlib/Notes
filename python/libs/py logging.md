[logging官网](https://docs.python.org/2/library/logging.html)  

基本用法

```python
# -*- coding: utf-8 -*-

import logging
import sys

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")
# 这是最基本的入口，该方法参数可以为空，默认的logger名称是root，
# 如果在同一个程序中一直都使用同名的logger，其实会拿到同一个实例，使用这个技巧就可以跨模块调用同样的logger来记录日志。
# logger = logging.getLogger("App.UI")
# logger = logging.getLogger("App.Service")

# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')

# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message

# 移除一些日志处理器
logger.removeHandler(file_handler)

```

格式化输出
```python
# 格式化输出
 
service_name = "Booking"
logger.error('%s service is down!' % service_name)  # 使用python自带的字符串格式化，不推荐
logger.error('%s service is down!', service_name)  # 使用logger的格式化，推荐
logger.error('%s service is %s!', service_name, 'down')  # 多参数格式化
logger.error('{} service is {}'.format(service_name, 'down')) # 使用format函数，推荐
 
# 2016-10-08 21:59:19,493 ERROR   : Booking service is down!
```

记录异常信息

```python
try:
    a = 1 / 0
except:
    logger.error("this is an exception message")
    
    # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息
    logger.exception('this is an exception message')
```

-----------
Formatter日志格式

Formatter对象定义了log信息的结构和内容，构造时需要带两个参数：

1. 一个是格式化的模板fmt，默认会包含最基本的level和 message信息
2. 一个是格式化的时间样式datefmt，默认为 2003-07-08 16:49:45,896 (%Y-%m-%d %H:%M:%S)

fmt中允许使用的变量可以参考下表。

格式 | 含义
---|---
%(name)s | Logger的名字
%(levelno)s | 数字形式的日志级别
%(levelname)s | 文本形式的日志级别
%(pathname)s | 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s | 调用日志输出函数的模块的文件名
%(module)s | 调用日志输出函数的模块名|
%(funcName)s | 调用日志输出函数的函数名|
%(lineno)d | 调用日志输出函数的语句所在的代码行
%(created)f | 当前时间，用UNIX标准的表示时间的浮点数表示|
%(relativeCreated)d | 输出日志信息时的，自Logger创建以来的毫秒数|
%(asctime)s | 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d | 线程ID。可能没有
%(threadName)s | 线程名。可能没有
%(process)d | 进程ID。可能没有
%(message)s | 用户输出的消息


-------
SetLevel 日志级别

Logging有如下级别: DEBUG，INFO，WARNING，ERROR，CRITICAL
默认级别是WARNING，logging模块只会输出指定level以上的log。

--------

Handler 日志处理器

最常用的是StreamHandler和FileHandler, Handler用于向不同的输出端打log。
Logging包含很多handler, 可能用到的有下面几种


Handler | function
---|---
StreamHandler | instances send error messages to streams (file-like objects).
FileHandler | instances send error messages to disk files.
RotatingFileHandler | instances send error messages to disk files, with support for maximum log file sizes and log file rotation.
TimedRotatingFileHandler | instances send error messages to disk files, rotating the log file at certain timed intervals.
SocketHandler | instances send error messages to TCP/IP sockets.
DatagramHandler | instances send error messages to UDP sockets.
SMTPHandler | instances send error messages to a designated email address.

----------


Configuration 配置方法

logging的配置大致有下面几种方式。

1. 通过代码进行完整配置，参考开头的例子，主要是通过getLogger方法实现。
2. 通过代码进行简单配置，下面有例子，主要是通过basicConfig方法实现。
3. 通过配置文件，下面有例子，主要是通过 logging.config.fileConfig(filepath)
-------



logging.basicConfig

basicConfig()提供了非常便捷的方式让你配置logging模块并马上开始使用，可以参考下面的例子。
具体可以配置的项目请查阅[官方文档](https://docs.python.org/2/library/logging.html#logging.basicConfig)
。
> 下面的方式获取的是root logger。只要你在程序中使用过root logger，那么默认你打印的所有日志都算它一份。（会导致日志的重复输出）
如果你真的想禁用root logger，有两个不是办法的办法：  
logging.getLogger().handlers = []  # 删除所有的handler
logging.getLogger().setLevel(logging.CRITICAL)  # 将它的级别设置到最高

```python
import logging
# 获取的是 root logging，项目中不建议
# 输出到文件
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')

# 输出到控制台
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')

# 输出到控制台，进行设置，也可以不设置（默认）
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

logging.basicConfig()
logging.warning('is when this event was logged.')
```
------------


通过文件配置logging

[官方文档](https://docs.python.org/2/library/logging.config.html)

```
# logging.conf
[loggers]
keys=root
 
[logger_root]
level=DEBUG
handlers=consoleHandler
#,timedRotateFileHandler,errorTimedRotateFileHandler
 
#################################################
[handlers]
keys=consoleHandler,timedRotateFileHandler,errorTimedRotateFileHandler
 
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)
 
[handler_timedRotateFileHandler]
class=handlers.TimedRotatingFileHandler
level=DEBUG
formatter=simpleFormatter
args=('debug.log', 'H')
 
[handler_errorTimedRotateFileHandler]
class=handlers.TimedRotatingFileHandler
level=WARN
formatter=simpleFormatter
args=('error.log', 'H')
 
#################################################
[formatters]
keys=simpleFormatter, multiLineFormatter
 
[formatter_simpleFormatter]
format= %(levelname)s %(threadName)s %(asctime)s:   %(message)s
datefmt=%H:%M:%S
 
[formatter_multiLineFormatter]
format= ------------------------- %(levelname)s -------------------------
 Time:      %(asctime)s
 Thread:    %(threadName)s
 File:      %(filename)s(line %(lineno)d)
 Message:
 %(message)s
 
datefmt=%Y-%m-%d %H:%M:%S
```

```python
import os
import logging
def get_logger():
    filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')
    logging.config.fileConfig(filepath)
    return logging.getLogger()
```


