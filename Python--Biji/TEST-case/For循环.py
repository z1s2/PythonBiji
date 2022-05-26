####循环的用法之for循环
####条件确定时用for循环

"""
for ...in（）（把in括号里面的每一个值都取出来，如字典，列表，元祖都行）
for  i  in  range()--函数
"""
###用法一：
############      for i in range(n)     ##range函数里的n 代表循环几次
for i in range(5):
    print('今年先赚'+str(i)+'百万')
#打印结果

######用法二：
############      for i in range(a,b,c) #代表一个步长的计算方式（a代表初始值，b代表总长，c代表间隔长度），如下：
for i in range(1,10,2):     #第一位不填写的话默认从0开始，从1取到9，去头不取尾
    print(i)
#打印结果如下：
#$$$$1,3,5,7,9

######用法--之99乘法口句
for i in range(1,10):               #乘数在1到10里进行循环，i分别取1，2，3，4，5，6，7，8，9
    for j in range(1,i+1):            # 被乘数自增加一进行循环，分别取1，2，3，4，5，6，7，8，9 ，乘数加1
        print( '%d X %d = %d' % (j,i,i*j),end = ' ' )          # 字符串拼接
    print('  ')

name = {'日本':'东京','英国':'伦敦','法国':'巴黎'}     #先建立一个字典
for i in name:         #####    name这个字典里取循环取出键值
    print(name[i])     ####     打印时字典的名字以及键

##列表循环

a = {1,2,3}      #定义一个列表
for i in a:      # #定义一个循环，将a里的值循环打印出来,i代表从1开始循环4次
    print("{:.2f}  {:.1f}".format(1,3))       #将列表a里的2和3，保留小数点位置循环打印出来，也就是循环打印列表a里指定的值
    print(i)
# print("{:.1f}  {:.1f}".format(2,3))

#打印结果$$$$：
"""
1.00  3.0
1
1.00  3.0
2
1.00  3.0
3
"""










"""分支结果,多重分支
# """
# a = 1
# if a ==0:
#     print("a=0")
# elif a ==1:
#     print()
# else:
#     print("a=0")

"""
分段函数求值
f(x) = 3x - 5 (x>1)
f(x) = x+2 (-1<= x <=1 )
    5x+3(x<-1)
"""
#分支结构
# x = 1
# if x>=1:
#     y = 3*x - 5
# else:
#     if -1 <= x <= 1:
#         y = x+2
#     else:
#         y = 5*x +3
# print(y)
#1到100里的求和
# result = 0     #定义的结果
# for i in range(101):
#     print(i)
#     result = result+i
# print(i,result)

#1到100的偶数求和
# result = 0
# for i in range(2,101,2):
#     # if i%2==0:
#         # print(i)
#         result = result+i
# print(result)
#

