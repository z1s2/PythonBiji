"""列表的用法1   insert（）插入元素"""
b = [1,2,3,4]
b.append(9)             #调用列表方法只能将要插入的数字插入到列表的末尾，不能指定位置
# b.insert(2,9)           #可以使用insert的方法插入到任意位置
print(b)
#$1,2,3,4,9    打印结果
#$1,2,9,3,4
#
# [1, 2, 9, 3, 4, 9]
# random(): 0.10023738048882891

"""列表的用法2 extend()列表中插入列表"""
a = [34,56,89,90]
b = [1,2,4,5]
a.extend(b)    #将列表b里的所有元素插入到元素a列表的末尾
print(a)

"""列表的用法3  remove()将列表中的元素移除"""
a = [34,4,5,6]
a.remove(5)
print(a)

"""列表的用法4  将列表用作栈和队列（即先进先出pop()）比如排队买票"""
a = [2,3,498]     #根据元素的索引进行删除，列表名.pop(索引编号)
a.pop(0)
print(a)


"""输入三个整数x,y,z，请把这三个数由小到大输出"""

l = []  #先定义一个空的l列表
for i in range(3):               #再进行输入三个数进行循环
    x = int(input('integer:\n'))      #然后输入一个整形数字integer转换(input在python3中表示输入不用加raw)
    l.append(x)  #对列表l进行添加输入的数字
l.sort(reverse=True)     #对列表l从小到大排序（从大到小排序l.sort(reverse=True)
print (l)

"""在屏幕上显示跑马灯文字"""
import os
import time

import random

def main():
    test = '北京欢迎你为你开天劈地'
    while True:
        os.system('cls')
        print(test)
        time.sleep(0.2)
        test = test[1:] + test[0]

if __name__ == '__main__':
    main()


list_square = []    #定义一个空列表
for i in range(1,5):     #使用for循环，在1到4进行循环，
    # 结果：1，2，3，4
    list_square.append(i**2)    #(i的平方i**2，)，，(list.append用法，不返回原结果，把新结果打印出来在列表的末尾)
    #结果：1。4。9。16
print(list_square)


#列表推导试实现上面的方式
list_square2 =[i**2 for i in range(1,4)]    #
print(list_square2)


#判断一个列表是否为空
a = []
if a:
    print('list是非空')
else:
    print('list是空')

#python:
'''
1、数字0：默认为false，其他的均为true
2、数据为空的列表[]\字典{}\ 元祖(),非空的为True,其他类型（字典/元祖）
'''



def fun(x,y):
     return x*y

fun(2,3)

#
# a_touble  = ('A','B','C')
# # i = 0
# print(a_touble)

#字符串分隔符
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
#>>> s
s = 'server=mpilgrim;uid=sa;database=master;pwd=secret'
s.split(";")

s1= ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
# s1.split(" ")
# ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']


"判断列表里是否为空"
# 1、数字0：默认为false，其他的均为true
# 2、数据为空的列表[]\字典{}\ 元祖(),非空的为True,其他类型（字典/元祖）
#方法一
a=[]
if a:      #如果a是空，则为false
    print('list是非空')
else:      #否则a不为空时，则为true
    print('list是空')

#方法二，通过len函数判断--长度判断：
a = [1]
if len(a) ==0:    #如果a的长度等于0，
    print('list是空')
else:
    print('list是非空')

