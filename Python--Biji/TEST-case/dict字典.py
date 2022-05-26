"""字典是是无序3.6版本以前的键值对{key:value}集合"""
"""删除字典中的键值对del"""
data= {'小明':'81','小红':'95','小白':'72','小李':'84',}
del data['小白']            #删除字典data里的某一个键值
data['小张'] = [100]        #在data字典里添加一个新的键值对
print(data)

"""字典的遍历"""
dict1 ={'年龄':'30','姓名':'赵姬','体重':'120'}
for i in dict1.items():   #将字典的键和值均打印出来
    for i in dict1.keys():    #将字典里的键打印出来
        print(i)

"""字典中的键是不可变类型，不能使用list作为键，但是可以使用touble"""
# dict((('小白','小红'),('78','89')))
# print(dict)


"""一个判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，如果总成绩小于 120"""

Number =int(input("请输入学生的数量"))
data= {}                        #用来存储数据的字典变量(保存已有的数据）
data= {}                        #用来存储数据的字典变量(保存已有的数据）
Subjects = ('lishi','shuxue','yingyu')
for i in range(0,Number):
    name =input('请输入学生的名字{}:'.format(i + 1))       #或得学生的名字
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of{}:'.format(x))))     #或得每一颗的分数
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x,"failed")
    else:
        print(x,"passed")


