#!/usr/bin/env python3

def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input('Enter a string:')
    if palindrome(s):
        print("Yay a palindrome")
    else:
        print('Oh no, not a palindrome')


import random
"""random生成随机函数"""

def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#
#     :param code_len: 验证码的长度(默认4个字符)
#
#     :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    s = input('Enter a number')
    if generate_code(code_len=6):
        print(generate_code())


# def test(a,b = -43):
#     if a > b:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#
#     res= test(12,13)
#     print(res)

# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
# def lcm(x, y):
#     return x * y // gcd(x, y)
# if __name__ == '__main__':
#     x = int(input('Enter a number'))
    y = int(input('Enter anumber'))
    s = gcd(x,y)
    print(s)
import sys
def hours(Mintue):
    h = int(Mintue/60)
    m = int(Mintue%60)
    if Mintue < 0:
        raise ValueError('Enter number not be negative')
    else:
        print('{}h,{}m'.format(h,m))

if __name__ == '__main__':
    s = int(input('Enter a number'))
    s1= hours(s)
    print(s1)





def Hours(minute):
    # 如果为负数则 raise 异常
    if minute < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H, {} M".format(int(minute / 60), minute % 60))
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")

print(Hours(80))


"""随机生成双色球"""
from random import randrange, randint, sample


def display(balls):
    """
    # 输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()

#
# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls



"""可变参数"""

def cals(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
        return sum
a = cals((1,2,3,4))
print(a)

