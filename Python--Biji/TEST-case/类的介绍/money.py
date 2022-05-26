"""
fun(*args,*kwargs)中的*args，以及*kwargs意思


*args,可以将不定量的参数传递给一个函数，这里的不定的意思是函数的使用者预先不知道会传递多少个参数给你，
是用来发送一个非键值对可变数量的参数列表   给一个函数
"""

def demo(args_f,*args_v):
    print (args_f)
    for x in (args_v):
        print(x)
demo(1,2,4,5)

"""
*kwargs允许将不定长度的键值对，作为参数传递给一个函数，如果想要使用一个函数里处理带名字的参数，应该使用**kwargs
"""

def demo1(**args_v):
    for k,v in args_v.items():
        print(k,v)
demo1(shanghai = "zhangsong" )



