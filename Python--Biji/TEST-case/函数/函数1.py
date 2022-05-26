# """
# Lambda函数，表达式，简单的饿函数实现
# """

sun = lambda x,y:x+y

print(sun(1,3))

s = lambda a,b: a-b if a<b else a+b
print(s(2,4))

"""
三目运算符
"""
a = 1
b = 2
# h = ""
h = a-b if a<b else a+b
print(h)

a = 1
b = 4
if a>b:
    s = a-b
else:s = a+b
print(s)

"""
生成器yield
什么时候使用生成器：
当循环读取特别大文件的时候，特别大的日志文件的时候，一行一行的读出来就可以就可以使用生成器
"""
def provider():
    #循环读取一个数据
    for i in range(10):
        print('开始操作')
        yield i
        print("结束操作")
        return i
#生成器函数的调用,需要在被打印函数前加一个next函数
p = provider()
print(next(p))
"""
迭代器
"""
list = {1,2,3,4,68}
it = iter(list)
print(next(it))
print(next(it))



#普通函数调用
# print(provider())
#<generator object provider at 0x103a32c00>这是一个函数

l = lambda a,b:a-b if a>b else a+b


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        list1 = list.reverse(pHead)
        return list1


pHead ={1,2,3}
s= Solution()
s.ReverseList({1,2,3})