
```python
# coding: utf8
"""
构造模式: 控制复杂对象的构造
当对象需要多个部分组合起来一步步创建，并且创建和表示分离的时候。
可以这么理解，你要买电脑，工厂模式直接返回一个你需要型号的电脑，
但是构造模式允许你自定义电脑各种配置类型，组装完成后给你。
这个过程你可以传入builder从而自定义创建的方式。
"""


class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


# 使用buidler，可以创建多个builder类实现不同的组装方式
engineer = HardwareEngineer()
engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
computer = engineer.computer
print(computer)

```
