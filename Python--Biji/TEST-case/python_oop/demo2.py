
# coding: utf-8
#@Author : zhangsong

from demo import Game
#继承父类的方式

class HouYi(Game):
    def __init__(self):
        self.defense = 100      #增加一个护甲
        """
         #如果重写的方法或者变量的化
        # 继承父类的构造方法，直接用super"""
        super().__init__(2000,20000)
    def fight(self):
        #我的剩余血量
        while True:
            self.my_hp = self.my_hp +self.defense -self.enemy_power         #我的剩余血量
            self.enemy_hp -= self.my_power     # 敌人的剩余血量
            print(f"我的血量{self.my_hp} VS 敌人的血量：{self.enemy_hp}")    # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break
    #定义休息方法
    def rest(self,time_num):
        print(f"太累了，休息{time_num}分钟")

# if __name__ == "_main":
houyi = HouYi()   #实例化类
    #子类对象可以直接调用父类的属性和方法
print(houyi.my_power)
houyi.fight()
houyi.rest(5)