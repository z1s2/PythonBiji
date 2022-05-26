# 文件读取

"""
1、打开文件
2、读取文件
3、关闭文件
"""
f = open('data.txt')        #打开某一个文件
print(open('data.txt'))       #将读取的文件打印出来
print(f.readable())         #代表可读的状体
print(f.readlines())        #读取文件里所有的行
print(f.readline())         #读取文件里的任意行，按行读取
# f.close()

"""
1、with语句快，可以将文件打卡后，操作完毕，自动关闭这个文件
2、读取图片要使用rb,读取二进制的格式    
with open('data.txt'，'rb') as f:
3、正常的文本则使用rt,即默认的模式，不用写
"""
with open('data.txt') as f:
    while True:      #循环读取，每次读取一行
        line = f.readlines()        #
        if line:     #如果这一行有数据则继续执行，没有则执行下一步操作
            print(line)
        else:
            break
    print(f.readlines())
