"""99乘法表，for  i  in  range循环"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s' % (i, j, i * j), end=' ')
#     print()


"""99乘法口诀（嵌套循环案例）"""
i = 1
while i < 10:           #程序开始执行此时行数i=1，i<=9成立进入循环，此时列数j=1
    j = 1
    while j <=i:       #程序判断j小于i时（此时j=1小于i= 1），打印print('%d * %d = %d\t' % (j, i, j*i), end='')，然后j自增为2大于i时，跳出内部循环，继续执行内部循环。
        print('%d * %d = %d\t' % (i, j, j*i), end='')
        j += 1
    print()
    i += 1
"""（斐波那契（Fibonacci）数列）这个数列前两项为 1，之后的每一个项都是前两项之和。所以这个数列看起来就像这样：1,1,2,3,5,8,13 """
# a, b = 0,1
# while b < 100:
#     print(b, end = '\t')
#     a, b = b, a+b
# print('\n')
"""打印出纵横列表的乘法表"""
# i = 1
# while i <=10:
#     j = 1
#     while j <=9:
#         print(end='')
#         j += 1
#         print('%5d * %d = %d\t' % (i, j, i * j),end=' ')
#     i +=1
#     print()
'''100以内的乘法结果'''
# i = 1
# print("_" * 50)  #控制打印下划线分割符长度
# while i<=11:
#     n = 1
#     while n <= 10:
#         print("{:3d}".format(i * n), end=' ')    #format用于打印出指定位置，{:3d}表示位右对齐，位置宽度为3
#         n += 1
#     print()
#     i += 1
#     print()
# print("_" * 50)
"""while循环的第二种写法99乘法口诀"""
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         # print("%d * %d = %d\t" % (i,j,i * j),end=' ')
#         print('%d * %d = %d\t' % (i, j, j * i), end='')
#         j += 1
#     print()


"""打印100以内的所有素数方法一"""

i = 2
while (i <100):
    j = 2
    while (j <= (i/j)):
#if not 判断（i%j)余数是否为空
        if not(i%j):
            break
        j = j+1
    if (j > i/j):
        print(i,"是素数")
#递归，否则会无限执行下去。
    i = i+1

"""打印100以内的素数方式二"""
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

i = 2
while i < 100: #限制i的范围
    j = 2
    while j <= i/j: #限制j的范围
        if not(i % j): #如果能整除则进行下面的代码
            break #能整除则跳出,直接进行i=i+1，不是素数不打印
        j = j + 1 #不能整除则j+1继续

    if(j > (i/j)): #加到j大于根号i还没有找到可被i整除的数，则应该满足素数的要求，打印
        print(i, " 是素数")
    i = i + 1

print ("Good bye!")


"""获取100以内的质数"""
num = [];
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)    #否则将i插入到列表num的末尾
print(num)



num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,100):
        if  (i % j ==0):
            break
    else:
        num.append(i)
    print(num)





# for i in range(1,10)
#         for j in range(i,i+1)
#             print('s% * s% = s%',(i,j,i * j),end=)
#         print()
my_list = list（range(2,10))
print(my_list)
