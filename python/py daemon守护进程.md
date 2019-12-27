```python
import atexit
import os
import sys
import time
from _signal import SIGTERM

base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))


class Daemon(object):
    def __init__(self):
        self.application_name = "TestDaemon"
        self.work_dir = "./tmp"
        # pid file 保存pid
        self.pid_file = os.path.join(base_dir, "%s.pid" % self.application_name)
        # 用户掩码，默认为0
        # https://www.runoob.com/linux/linux-comm-umask.html
        self.umask = 0

    def start(self, *args, **kwargs):
        try:
            pid = self._get_pid()
        except IOError:
            pid = None
        # 如果PID存在，则说明进程没有关闭。
        if pid:
            message = self.application_name + ': pid_file %s already exist. Process already running!\n'
            sys.stderr.write(message % self.pid_file)
            # 程序退出
            sys.exit(1)

        # 构造进程环境
        self._daemonize()
        message = self.application_name + ': Process is start.\n'
        sys.stderr.write(message)
        # 执行具体任务
        self.run(*args, **kwargs)

    def stop(self):
        # 从pid文件中获取pid
        try:
            pid = self._get_pid()
        except IOError:
            pid = None

        # 如果程序没有启动就直接返回不在执行
        if not pid:
            message = self.application_name + ': pid_file %s does not exist. Process not running!\n'
            sys.stderr.write(message % self.pid_file)
            return

        # 杀进程
        try:
            while 1:
                # 发送信号，杀死进程
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
                message = self.application_name + ': Process is stopped.\n'
                sys.stderr.write(message)
        except OSError as err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pid_file):
                    os.remove(self.pid_file)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self, *args, **kwargs):
        self.stop()
        self.start(*args, **kwargs)

    def status(self):
        try:
            pid = self._get_pid()
        except IOError:
            pid = None

        if not pid:
            message = self.application_name + ": No such a process running.\n"
            sys.stderr.write(message)
        else:
            message = self.application_name + ": The process is running, PID is %s\n"
            sys.stderr.write(message % str(pid))

    # 这个方法的主要目的就是脱离主体，为进程创造环境
    def _daemonize(self):
        # 第一步
        try:
            # 第一次fork，生成子进程，脱离父进程，它会返回两次，PID如果等于0说明是在子进程里面，如果大于0说明当前是在父进程里
            pid = os.fork()
            # 如果PID大于0，说明当前在父进程里，然后sys.exit(0)，则是退出父进程，此时子进程还在运行。
            if pid > 0:
                # 退出父进程，此时linux系统的init将会接管子进程
                sys.exit(0)
        except OSError as e:
            sys.stderr.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)

        # 初始化工作环境
        self.init()

        # 第二、三、四步
        self.set_env()

        # 第五步
        try:
            # 第二次fork，禁止进程打开终端，相当于是子进程有派生一个子进程
            pid = os.fork()
            if pid > 0:
                # 子进程退出，孙子进程运行，此时孙子进程由init进程接管，在CentOS 7中是Systemed。
                sys.exit(0)
        except OSError as e:
            sys.stderr.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)

        # 把之前的刷到硬盘上
        sys.stdout.flush()
        sys.stderr.flush()

        # 注册程序结束时的调用
        self.end_callback()

        # 写入pid
        with open(self.pid_file, 'w') as f:
            f.write('%s\n' % str(os.getpid()))

    def init(self):
        # 重定向标准文件描述符
        # sys.stdin = open(os.devnull, 'r')
        # sys.stdout = open(os.devnull, 'a+')
        # sys.stderr = open(os.devnull, 'a+')

        # 初始化 work_dir 目录
        if not os.path.exists(self.work_dir):
            os.makedirs(self.work_dir)

    def set_env(self):
        # 设置子进程环境
        # 第二、三、四步
        os.chdir(self.work_dir)  # 修改进程工作目录
        os.setsid()  # 设置新的会话，子进程会成为新会话的首进程，同时也产生一个新的进程组，该进程组ID与会话ID相同
        os.umask(self.umask)  # 重新设置文件创建权限，也就是工作目录的umask

    def end_callback(self):
        # 注册退出函数，根据文件pid判断是否存在进程
        atexit.register(self._del_pid)

    def _get_pid(self):
        try:
            # 读取保存PID的文件
            pf = open(self.pid_file, 'r')
            # 转换成整数
            pid = int(pf.read().strip())
            # 关闭文件
            pf.close()
        except IOError:
            pid = None
        except SystemExit:
            pid = None
        return pid

    def _del_pid(self):
        """
        删除 pid 文件
        """
        if os.path.exists(self.pid_file):
            os.remove(self.pid_file)

    def run(self, *args, **kwargs):
        """
        这里是孙子进程需要做的事情，你可以继承这个类，然后重写这里的代码，上面其他的都可以不做修改
        """
        while True:
            """
            print 等于调用 sys.stdout.write(), sys.stdout.flush()是立即刷新输出。正常情况下如果是输出到控制台那么会立即输出
            但是重定向到一个文件就不会了，因为等于写文件，所以需要进行刷新进行立即输出。 下面使用print 还是 write都是一样的。
            """
            with open("a.txt", 'a') as f:
                f.write('%s:hello world\n' % (time.ctime(),))
            time.sleep(2)


if __name__ == '__main__':
    daemon = Daemon()
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'status' == sys.argv[1]:
            daemon.status()
        else:
            print('unknown command')
            sys.exit(2)
        sys.exit(0)
    else:
        print('usage: %s start|stop|restart|status' % sys.argv[0])
        sys.exit(2)

```
