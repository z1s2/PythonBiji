#基础数据类型 ：列表、元祖、字典、字符串
'一、列表转化为字典'
'##1、使用for循环'
list1 = ['fs','ef','zhnag']
list2= [1,2,3]
dict1= {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)

'##2、/使用内置函数zip'
l1= [1,2,3,5]
l2 = ['w','rt','gt','ht']
d = dict(zip(l1,l2))
print(d)

"""二、列表转化为字符串"""
'##1、使用str函数'
l1 = [1,'r',5,'fdg']
str1 = str(l1)
print(str1)

'##2、使用列表推到式'
#列表推到式格式==[表达式 for 变量 in 列表]或者[表达式 for 变量 in 列表 if 条件]
l1 = [1,'f','g','h']
str = [str(i) for i in l1]
print(str)

#列表转化为字典1（两个列表）
list1 = ['g','gge','df']
list2 =[1,2,3,]
dict1= dict(zip(list1,list2))
print(dict1)

#列表转化为字典2（数组列表）
list3 = [['1','de'],['2','ed'],['3','hg']]
new_dict = {}
for i in list3:
    new_dict[i[0]] = i[1]
print(new_dict)

"""三、字典"""

"""四、元祖tuple"""

"""五、集合set"""


