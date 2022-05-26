"""
函数代码块以def 关键字开头，后接函数名称和圆括号（）
冒号起始
圆括号中定义参数
函数说明文档字符串
return（表达式）结束函数
选择性地返回一个值给调用方
不带表达式地return或者不写return函数，相当于None

类方法
实例
"""
def fun1(a,b,c):



# 函数的调用

  
 class Game():
    #初始化方法（构造函数）
    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.enemy_hp  = 1000
        self.enemy_power = 199

    #实例方法（对打方法）
    def fight(self):
        while True:
            #我的血量
            self.my_hp = self.my_hp- self.my_power
        #敌人的血量
            self.enemy_hp = self.my_power

        print(f"我的血量,{self.my_hp}VS敌人血量,{self.enemy_hp}")

        if self.my_hp <= 0:
            print(我赢了)

        elif self.enemy_hp <= 0:
            print(敌人赢了)





