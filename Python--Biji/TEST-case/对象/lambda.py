"""
1、lambda也叫做匿名函数（闭包函数）：定义一个函数时不需要定义他的函数名（怎么将函数名隐藏起来）
2、python中单线程和多线程
3、lambda表达式
4、匿名函数最合适的使用场景
"""

def add(x,y):
    return x+y
print(add(1,2))



f = lambda x,y:x+y        # (lambda表达式关键在于后面的表达式)
print(f(1,2))





 


# parameter_list: expression     #定义为简单的表达式(参数列表)