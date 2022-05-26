class Student:
    name = ''
    age = 18

    def __init__(self,name,age):
        name  = name
        age = age
        print('student')

student1 = Student('小明',18)  #实例化方法
student1.__init__('小米',18)     #构造函数后，可以省略这一步（类的方法的调用）
print(student1.age)             #类的属性的调用   print（实例名.属性）