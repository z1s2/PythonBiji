"""分别输入年月日，然后打印出该日是今年第几个月的第几天"""

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 <= month <= 12:
#     sum = months[month - 1]
# else:
#     print ('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
#     print (int('it is the %dth day.') )% sum

#1，2，3，4组合,能组成多少个互不相同且无重复数字的三位数

# for i in range (1,5):
#     for j in range(1,5):
#         for k in range (1,5):
#             if (i != j) and (i != k) and (j != k):
#                 print(i,j,k)

"""企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
 于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
 成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
 40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
 100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？"""

fit1 = 100000 * 0.1
fit2 = fit1 + 100000*0.075
fit3 = fit2 + 200000*0.05
fit4 = fit3 + 400000*0.03
fit5 = fit4 + 600000*0.015
fit6 = fit5 + 1000000*0.001

i = int(input('请输入利润：'))

if i <= 100000:
    fit = 100000 * 0.1
    print(fit)
elif i <= 200000:
    fit = fit1 + (i - 100000) * 0.075
    print(fit)
elif i <= 400000:
    fit = fit2 + (i - 200000) * 0.05
    print(fit)
elif i <= 600000:
    fit = fit3 + (i - 400000) * 0.03
    print(fit)
elif i <= 1000000:
    fit = fit4 + (i - 600000) * 0.015
    print(fit)
else:
    fit = fit5 + (i - 1000000) * 0.001
    print (fit)











