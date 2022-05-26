"""
1、集合是无序的
2、集合可支持自动去重

"""
list1= [1,9,3,4,5,6]
list2= [3,4,7,8]
list5 = list1 + list2

list3 = set(list5)    #将列表转化为集合set
list4 = list(list3)     #将集合再转化为列表

list1= [1,9,3,4]
list2= [3,4,7,8]
dict1 = dict(zip(list1,list2))
print(dict1)

print(list)
print(type(list))
print(list3)
print(type(list3))

print(list4)
print(type(list4))



set1 = {1,3,4,5,7}
set2 = {4,5,8,9}
set = set1 - set2
set = set1 | set2    #集合里求并集去重
print(set)
print(type(set))