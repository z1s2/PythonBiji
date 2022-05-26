"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""

class Animal:
    name = "八月"           #类变量（和类相关的变量，）
    colour = ""
    #类变量（和类相关的变量，）
    age = "45"               #类变量（和类相关的变量，）
    sex = "green"            #类变量（和类相关的变量，）

    def __init__(self,name,age,colour,sex):   #构造方法参数里必须添加self参数（构造函数）-----相当于一个模版
        self.name = name            #实例变量（实例对象和对象相关）
        self.age = age              #2、实例对象必须要有个地方存储变量
        self.colour = colour        #1、实例变量只和实例对象相关，实例对象的变量保存在这里
        self.sex = sex              #3、self不是关键字
#如果访问实例变量时，py会先查找实例变量的列表，如果找不到，就会去类里去查找，如果还找不到，则会去父类里去找
#         print(self.age)                #实例范围内访问实例变量，print加上self
#         print(self.__class__.age)      #实例范围访问类变量，print加self._class__
#         print(sex)
#         print(Animal.name)
#         print("init function")
#         print(f"毛毛的年龄是：{self.name},maomao的年龄是:{self.age}")
    def dog(self,age,name):
        age  = ''
        name  = ''
        if age <= "0":
            return "哈士奇"
        print("这个狗是个神经病")

# #
cat =Animal('毛毛',19,'man','blue')      #实例方法，将构造的方法实例化方可打印出来
# print(f"毛毛的名字是：{cat.name},maomao的年龄是:{cat.age}")
# print(Animal.name)       #打印类里的变量----八月
# print(cat.name)          #打印构造函数（方法）里的变量----毛毛
print(cat.dog(16,67))
print(cat.dog(18,56))

print(f"毛毛的年龄是：{cat.age}")
dog = Animal('小花',20,'women','red')
print(Animal.age)
print(cat.sex)
print(cat.name)
#实例方法内部访问实例变量：         print(self.变量名)，
#实例方法内部访问类变量            print(类名.变量)//// print(self.__class__.age)
#实例方法外部访问类变量：           print(类名.变量)














