# a = [1,2,3,4,5,6,7,8,9,10]
#
# def is_odd(n):
#
#     return n % 2 == 0
#
# print(list(filter(is_odd,a)))
#
# n = 1000
# while n >1:
#     n = n/2
# print(n)
#
# print(r"\nwoow")
# def fun(a=(),b=[]):
#
#     a += (1,)
#
#     b.append(1)
#
#     return a,b
#
# fun()
#
# print(fun())
#
#
# #
# # b = []
# # i = 0
# # while i < len(a):
# #     if a[i] not in b:
# #         b.append(a[i])
# #     else:
# #         i += 1
# # print(b)
#
#
# tmp = 'ab' + 'c'*2
# print(tmp)

# 执行以下程序，输出结果为（）
#
# lis = ['apple','lemon','pear','peach']
# def fn(x):
#     return x[::-1]
# lis.sort(key=fn,reverse=True)
# print(lis)
#
# tmp = [1, 2, 3, 4, 5, 6]
# print(tmp[5::-2])

# import copy
# a = [1, 2, 3, 4, ['a', 'b']]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a.append(5)
# a[4].append('c')


"""
1.对象的赋值
都是进行对象引用（内存地址）传递，即‘’ b is a‘’ ，a 变 b 也变
2.浅拷贝
会创建一个新的对象,即 “c is not a” ，但是，对于对象中的元素，浅拷贝就只会使用原始元素的引用（内存地址），也就是说”c[i] is a[i]”
当我们使用下面的操作的时候，会产生浅拷贝的效果：

使用切片[:]操作
使用工厂函数（如list/dir/set）
使用copy模块中的copy()函数
3.深拷贝
会创建一个新的对象，即”d is not a” ，并且 对于对象中的元素，深拷贝都会重新生成一份（有特殊情况，下面会说明），
而不是简单的使用原始元素的引用（内存地址）
"""
import copy
a = [1, 2, 3, 4, ['a', 'b']]
b = a                   #此时b则为 b = [1, 2, 3, 4, ['a', 'b']]
a[4].append('c')
c = copy.copy(a)        #浅拷贝，只会拷贝父对象，，不会拷贝子对象，所以此时c = [1, 2, 3, 4, ['a', 'b']]
d = copy.deepcopy(a)    #深拷贝，完全复制了a的所有值，已经完全与a无关，对a的任何操作都不会影响 d  = [1, 2, 3, 4, ['a', 'b']]
a.append(5)
print(a)      #[1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(d)      #[1, 2, 3, 4, ['a', 'b', 'c']]
print(c)      #[1, 2, 3, 4, ['a', 'b', 'c']]



