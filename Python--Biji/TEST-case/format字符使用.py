
"""字符串的用法format"""
a = {1,2,3}      #定义一个列表
for i in a:      # #定义一个循环，将a里的值循环打印出来,i代表从1开始循环4次
    print("{:.2f}  {:.1f}".format(1,3))       #将列表a里的2和3，保留小数点位置循环打印出来，也就是循环打印列表a里指定的值
    # print(b)     #将列表a里面的值一次打印出来
# print("{:.1f}  {:.1f}".format(2,3))
#
"""
1、格式化字符串的用法1
2、format将字符输入到制定位置
"""
f = 456.789
print("{:.2f}".format(f))  #1、保留小数点后2为的写法{}花括号表示位置省略几位小数，format输入要打印的字符
#结果：456.79
print ("%.2f" % f)        #2、保留小数点后两位的写法2 ，格式（'%.2f' % f)，  f代表要打印的字符，常用于要输出的字符
#结果：456.79


a = 72
b = 85
r =(b-a)/a
print("%.1f" % r)
###结果：0.2

"""
格式化字符串的用法2
求n个数的平均值
"""
#
# n = 3
# sum = 0
# count = 0
# print("please input 3 numbers:")    #输入10个数字
# while count < n:
#     number = float(input())    #输入1，2，3
#     sum = sum + number
#     count  = count +1
# average = sum / n
# print('n={},sum = {}'.format(n,sum))   #format输出值的指定位置
# ###结果：n=3,sum = 6.0
#
# print("Average = {:.3f}".format(average))   #打印出的数字保留小数点后两位，打印的字符串
###结果：Average = 2.000

name = "lili"
age = 20
list1 = [1,3,4]
dic1 = {'name':'tome','gender':'male'}
print('我的列表{},字典是{}'.format(list1,dic1))
###结果：我的列表[1,3,4],我的字典['name':'tome','gender':'male']
print('my name is {1},age is {0},{0}{1}{1}'.format(name,age))  #####打印函数顺序的字符0，1分别代表每一行的字符
###结果：my name is "lili",age is

namelist = ['lili','tom','jerry']
print('we name:{}、{}and{}'.format(*namelist))  #列表解包
###结果：we name:lili、tomandjerry

print('my name is.{name},gender is.{gender}'.format(**dic1))    #字典解包,并且在前面加上键值的名字，字符串里跟上字典的键，format(**字典的名字)
###结果：my name is.tome,gender is.male

print(f'my name is {name},age is {age}, my list is {list1},my dict is {dic1}')    #解包3.6以上版本
####结果：my name is lili,age is 20, my list is [1, 3, 4],my dict is {'name': 'tome', 'gender': 'male'}



#
"""
step：
1、%.d的用法
"""
print('我们需要%.8d个人' %(10))
#%.8d整数位的个数   ： 我们需要00000010个人
"""
2、%d的用法
"""
print('我们需要%8d个人' %(10))
#%8d整数位的位数 ，从左往右省略8个 ：  我们需要      10个人
"""
3、%f的用法
step：2f浮点数float,没有点，减去从右往左减去2位 
"""
print('我们需要%2f年'%(3.14158234))
####结果： 我们需要3.141582年

"""
4、%.f的用法
step：%.2f浮点数，保留小数点后两位
"""
print('我们需要%.2f年'%(3.14158234))
####结果：    我们需要3.14年


"""format使用详解"""

"""format基本用法1"""
print('hello {} {}'.format('xiao','zhao'))
#打印结果：hello xiao zhao

print("{} is good".format("小 赵"))  # 引用第一个参数
#打印结果：小 赵 is good\

print("My name is {name}".format(name="xiao zhao"))    # 引用名字为name的参)引用名字为name的参
#打印结果：My name is xiao zhao

'''
1、类型的转换
'''
print('"Chen xin is a cute {!s}".format("baby") # !s 相当于对于参数调用str()')

"""
2、字符串的填充
"""
print('{0},{1},{2}'.format('小明','小花','小刘'))    #按照字符的ID顺序正序
#打印结果：小明,小花,小刘

print('{2},{1},{0}'.format('小明','小花','小刘'))     #按照字符的ID倒叙打印
#打印结果：小刘,小花,小明

print('{2},{1},{0}'.format(*("小明","小花","小刘")))  #按照字符的ID

#打印结果：小刘,小花,小明
print('{2}, {1}, {0}'.format(*'abc'))
#打印结果：c, b, a

print('{},{},{}'.format('a','b','c'))
#打印结果：a,b,c

print('{0} {1} {0} {0}'.format('aa', 'bb','c','bb'))
#打印结果： aa bb aa

"""
3、按照名称显示
"""
print('name: {last_name}{first_name}'.format(last_name='chen', first_name='xin'))
#打印结果：name:chen,xin

name= {'last_name': 'chen', 'first_name': 'xin'}
print('name:{last_name},{first_name}'.format(**(name)))
#打印结果：name:chen,xin


"""
4、通过参数属性访问
"""
class Mylist:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Mylist({self.x},{self.y})".format(self=self)

print(str(Mylist('陈新明','www.baidu.com')))
#打印结果：MyList(陈新明, www.chenxm.cc)

"""
5、通过参数的items访问
"""
my_list = ['陈新明', 'www.chenxm.cc']

print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的，0代表字典的第一个值的位置
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的，0代表字典的第一个值的位置
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的，0代表字典的第一个值的位置

#打印结果：网站名：陈新明, 地址 www.chenxm.cc

"""
6、访问字典中的元素
"""
people = {"name": "Chen", "age": 18}
"My name is {p[name]} and my age is {p[age]}".format(p=people)

#打印结果： 'My name is Chen and my age is 18'
# 注意：用%格式化字符串不支持此功能

"""
7、访问元祖中的元素
"""
a = (1,2)
print('X: {0[0]};  Y: {0[1]}'.format(a))
# 打印结果 'X: 1;  Y: 2'
# 注意：用%格式化字符串不支持此功能

"""
8、时间格式化
"""
import datetime

d = datetime.datetime(2018, 7, 31, 15, 58, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
#打印结果 2018-07-31 15:58:58

"""
9、表示一个百分比
"""
print('number: {:.2%}'.format(0.61898))

#打印结果：number: 61.90%

"""
10、数字格式化
"""
a = 3.1415926
print("%.2f" % a)
#打印结果：3.14
print("{:.2f}".format(a))
#打印结果：3.14

'''
11\\
'''
a = {1,2,3,4}      #定义一个列表
for i in a:      #定义一个循环，将a里的值循环打印出来,i代表从1开始循环4次
    print("{:.2f}  {:.1f}".format(1,4))       #将列表a里的2和3，保留小数点位置循环打印出来，也就是循环打印列表a里指定的值
    print(type(i))
