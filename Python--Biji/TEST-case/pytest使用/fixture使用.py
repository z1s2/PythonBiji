#fixture的用法
"""
一、作用
a、定义传入测试中的数据集
b、配置测试前系统的初始状态

1、类似setup,teardown功能，但比setup,teardown更灵活
2、直接通过函数名字调用或使用装饰器@pytest.mark.usefixtures
3、允许使用多个fixture
4、作用域（sessio>module>class>function）
5、使用autouse自动应用，如果要返回值，需要穿fixture函数名

"""

#fix作用域
"""
1、function函数或者方法级别都会被调用
2、class类级别调用一次
3、module模块级别调用一次
4、session是多个文件调用一次
"""