"""
元组的常用方法touple
1、不可变，不可删除，不可新增，但是可以通过索引ID来访问元祖内容，列表则以上条件均满足
2、

"""
tuple1 = (1,2,3,5)
print(tuple1[2])

list1 = [1,2,3,45]
print(list1[2])

# list =[2,3,5,9,6]
# list1= []
# def get_min(l):
#     a = min(list)  #获取列表最小值
#     list.remove(a)   #移除列表最小值
#     list1.append(a)    #将列表最小值添加到新列表里
#     if len(list)>0:   #如果list函数的值大于0了，继续执行get_min函数
#         get_min(l)
#     return list1    #直至返回list1

# list1 = get_min(list)     #构造方法
# # print(list1)
#
# list1 =[2,3,5,9,6]
# set1 = set(list1)
# print(set1)
#
# list2 = list(set1)
# print(list2)


