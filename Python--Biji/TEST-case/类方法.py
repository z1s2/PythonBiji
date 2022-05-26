# coding: utf-8
#@Author : zhangsong
#类基本作用封装变量/方法

class House:    #类名应该是驼峰式命名:首字母大写
    #静态属性，---类变量，在类之中，方法之外定义
    door = 'red'
    floor = 'white'
    #构造方法，
    # #在类实例化的时候自动执行
    def __init__(self):
        # print(House.door)
        #加上self.变成实例变量
        print(self.door)
        #定义实例变量,----在类之中，方法之内，以self.变量名，方式定义
        #实例变量的作用域是整个类中的所有方法（在动态方法里也可以直接加self.变量的方式
        #一般在所有的函数这里添加实例变量，便于后面的调用
        self.kitchen = 'cook'

    #动态的方法
    ##描述房子来干嘛，描述类能干啥以及服务
    def sleep(self):
        #普通变量--在类之中，方法之中，并且前面没有self.开头
        bed = '席梦思'
        print(f'在房子里可以躺在{bed}睡觉')

    def cook(self):
        print('在房子里可以做饭')

# if __name__ == '__main__':可加可不加
north_house = House()   #类的实例化1
china_house = House()   #类的实例化2

north_house.sleep()     #实例north_house在调用sleep这个方法时，相当于把自身作为一个self参数穿进括号里。
# 通过类直接修改属性
House.door = "green"
#通过实例修改属性
north_house.door = 'white'

print(north_house.door)  #通过实例对象调用类属性
print(House.door)       #通过类也可以调用类属性


"""
self的作用
1、单单只在类中定义的方法和变量才用到，代表其本身
2、单一的函数里不需要使用
3、函数和方法的区别
----函数在类的外面（在定义时，括号里不需要self）
----类里面的方法去使用类变量时一定得加self
----方法在类的里面（在定义时，括号里需要self）
"""









