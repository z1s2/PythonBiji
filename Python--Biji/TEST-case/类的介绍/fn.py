#coding=utf-8

import  sys
#
# class Book:
# #定义一个初始化方法：
#     def __init__(self,name,author,comment,state =0):  #"""在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
#         self.name = name            #创建实例变量
#         self.author = author        #创建实例变量
#         self.comment = comment      #创建实例变量
#         self.state = state          #创建实例变量
#         book1 = Book('看不见的城市', '卡尔薇娅', '献给城市的最后一道爱情', '未借出')
#
# # book = Book('看不见的城市','卡尔薇娅','献给城市的最后一道爱情','未借出')   #类的实例化
# # print(book.name)                                            #调用类中的实例变量
#
#     # def show_inf  o(self):
#     def __str__(self):          #类中定义了  __str__(self)方法时，使用print打印实例对象时，就直接打印出这个方法中的return数据
#         if self.state ==0:      #如果state = 0,则表示未借出
#             status = '未借出'
#         else:
#             status = '已借出'
#         return '名称:《%s》 作者：%s 推荐语：%s\n 状态：%s' % (self.name,self.author,self.comment,status)   #返回书籍信息

# book = Book('像自由一样美丽', '林达', '你要用光明来定义黑暗，用黑暗来定义光明')
# print(book.show_info())       #打印类中show_info这个方法
# # print(book)                #如果采用了__str__(self)这个函数时，则直接采用print(book)这个方式就可打印出return的返回数据

# class BookManager:
#     books = []
#     def __init__(self):     #定义创建一个book类的实例对象，
#         book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
#         book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
#         book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
#         self.books.append(book1)
#         self.books.append(book2)
#         self.books.append(book3)
#
# manager = BookManager()
# print(len(manager.books))
# # 打印列表长度
# for book in manager.books:
#     print(book)








    #
    # def menu(self):

    #     print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地.\n')
    #
    # def show_all_book(self):
    #     pass
    #
    # def add_book(self):
    #
    #     pass
    #
    # def lend_book(self):
    #     pass
    #
    # def return_book(self):
    #     pass
    #
    #     while True:
    #         print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
    #         choice =int(input('请输入数字选择对应的功能'))
    #         if choice == 1:
    #             self.show_all_book()       #调用对象方法
    #
    #         elif choice ==2:
    #             self.add_book()
    #
    #         elif choice == 3:
    #             self.lend_book()
    #
    #         elif choice ==4:
    #             self.turn_book()
    #         elif choice ==5:
    #             print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
    #             break

def number(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


print(number([3,5,6,7]))


a ='hello world'
#a.replace('hello',' python')
print(a.replace('hello','python'))




