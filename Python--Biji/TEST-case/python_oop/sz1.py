# result = 0
# for i in range(2,200,2):
#     if i%3==0:
#         result = result+1
# print(i,result)
# #
"一、乘法口诀题目while循环"
# i= 1
# while i <=9:
#     j = 1
#     while j<=i:
#         print('%d * %d = %d' % (i,j,i*j), end="  ")
#         j +=1
#     print("")
#     i+=1
"二、乘法口诀题目for .. in  range()实现循环，注意缩进的语法格式"
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d = %d' % (i,j,i*j), end= ' ')
#     print("")

"三、实现1到100里的数字乘以5"
# i = 1
# while i<=100:
#     s = 5*i
#     print(s)
#     i =i+1     #(i=i+1等于i +=1)
# print(i)

"四、打印1到7里面的数字，除去4，while循环实现"
# # i =0
# # while i<7:
# #     # print(i)
# #     i +=1
# #     if i!=4:
# #         print(i)
"五、打印1到7里面的数字，除去4，for循环实现"
# for i  in range(1,8):
#     if i !=4:
#         print(i)

"六、if  else循环"

# a = input('请输入')    #input函数输入默认都时str类型，如果单纯没有做转换的化，此时就不会对a 进行比较
# # print(type(a))
# # print('a is' +a)
# a = int(a)
# if a==1:
#     print('apple')
# else:
#     if a==2:
#         print('orging')
#     else:
#         if a==3:
#             print('banana')
#         else:
#             print('shopping')
#     print("a")
# "七、if  elif"
# a = input("请输入")
# if a == 1:
#     print('apple')
# elif a==2:
#     print('orange')
# elif a==3:
#     print('banana')
# else:
#     print('shopping')



'a和b不可能同时为false'




'snippet功能代码片段'


import random
def ball():
    red_num  = range(1,36)
    blue_num = range(1,12)
    red_list = random.sample(red_num,6)
    blue_list = random.sample(blue_num,1)
    print(red_list+blue_list)













