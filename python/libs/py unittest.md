[附另一个测试框架 pytest 官网](https://docs.pytest.org/en/latest/getting-started.html#install-pytest)

Pyhon工作原理—— 核心概念：test case, testsuite, TestLoder,TextTestRunner,TextTestResult, test fixture


* TestCase（测试用例）: 所有测试用例的基类，它是软件 测试中最基本的组成单元。  
	(一个test case就是一个测试用例，是一个完整的测试流程，包括测试前环境的搭建setUp，执行测试代码(run)，以及测试后环境的还原(tearDown)。测试用例是一个完整的测试单元，可以对某一问题进行验证。)
* TestSuite（测试套件）:多个测试用例test case集合就是TestSuite，TestSuite可以嵌套TestSuite
* TestLoder：是用来加载 TestCase到TestSuite中，其中有几个loadTestsFrom_()方法，就是从各个地方寻找TestCase，创建他们的实例，然后add到TestSuite中，再返回一个TestSuite实例
* TextTestRunner：是来执行测试用例的，其中的run（test）会执行TestSuite/TestCase中的run(result)方法。
* TextTestResult：测试结果会保存到TextTestResult实例中，包括运行了多少用例，成功与失败多少等信息
* TestFixture:又叫测试脚手，测试代码的运行环境，指测试准备前和执行后要做的工作，包括setUp和tearDown方法


```python
# file: handler
def get_add(a, b):
    return a + b


def get_max(a, b):
    return a if a > b else b


def get_min(a, b):
    return a if a < b else b

```


```python
# coding: utf8
# file: test_handler
import unittest
from handler import get_add, get_max, get_min


# 在第一行给出了每一个用例执行的结果的标识，
# 成功是 .，失败是 F，出错是 E，跳过是 S
# 测试的执行跟方法的顺序没有关系
class TestHandler(unittest.TestCase):
    # setUpClass()与tearDownClass() 
    # 在所有case执行之前准备一次环境，并在所有case执行结束后再清理环境
    # 注意：@classmethod必须加，否则报错
    @classmethod
    def setUpClass(cls):
        print('This setUpClass() method only called once\n')

    @classmethod
    def tearDownClass(cls):
        print('This tearDownClass() method only called once too\n')

    # setUp， tearDown 两个方法在每个测试方法执行前以及执行后执行一次
    # setUp用来为测试准备环境，tearDown用来清理环境，已备之后的测试
    def setUp(self):
        print('do something before test')

    def tearDown(self):
        print('do something after test')

    # 每个测试方法均以 test 开头，否则是不被unittest识别的
    def test_add(self):
        print("test_add")
        self.assertEqual(5, get_add(2, 3))
        self.assertNotEqual(3, get_add(2, 3))

    # 跳过某个case
    # @unittest.skip("no reason")
    # @unittest.skipIf(1, u"为True时跳过")
    # @unittest.skipUnless(0, u"为False时跳过")
    def test_max(self):
        print("test_max")
        self.assertEqual(3, get_max(2, 3))

    def test_min(self):
        print("test_min")
        self.assertEqual(2, get_min(2, 3))


def fun1():
    # 直接用 addTests 方法添加 TestCase 列表，确定 case 执行顺序
    suite = unittest.TestSuite()
    tests = [TestHandler("test_min"), TestHandler("test_add"), TestHandler("test_max")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def fun2():
    # 直接用 addTest 方法添加单个 TestCase, 确定 case 执行顺序
    suite = unittest.TestSuite()
    suite.addTest(TestHandler("test_min"))
    suite.addTest(TestHandler("test_max"))

    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)


def fun3():
    # 用 addTests + TestLoader， 加载多个模块（文件），确定文件执行顺序
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromName("test_handler.TestHandler"))
    # 添加多个
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(["test_handler.TestHandler"]))

    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)


def fun4():
    # 用 loadTestsFromTestCase 方法传入 TestCase 名称即可, 确定类执行顺序
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHandler))

    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)


def fun5():
    # 结果输出到文件
    suite = unittest.TestSuite()
    tests = [TestHandler("test_min"), TestHandler("test_add"), TestHandler("test_max")]
    suite.addTests(tests)

    with open("result.txt", "a") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)


if __name__ == "__main__":
    # 在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，是
    # 1，默认值
    # 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行
    # 2，则输出详细的执行结果
    # unittest.main(verbosity=1)
    fun5()
```
