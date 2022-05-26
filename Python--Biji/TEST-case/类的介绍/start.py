# d1={'tudou':3,'yangcong':1,'mitao':8}
# d2={'mitao':3,'pantao':5,'wutongshu':2,'bailian':1}
# d = d1.copy()
# d3 = d.update(d2)
# print(d)
# # print(d3)
#
#
str = 'abccccabdergggggd'
def count(n):
  list1 = []
  list2 = []
  list3 = []
  for i in n:
    list4 = []
    count_max = n.count(i)
    list4.append(i)
    list4.append(count_max)
    list2.append(list4)
    list3.append(count_max)
  num=max(list3)
  for i in range(len(list3)):
    if list3[i] == num:
      list1.append(list2[i][0])
  return list(set(list1)),'字符出现最多次数为:%d' % num
print(count(str))

#
#


#反转字符串
s = "hello world"
def str_reverse2(s):
    l = list(s)        #字符串转化为列表
    l.reverse()         #通过reverse函数进行反转成列表格式
    return "".join(l)    #再去除符号

if __name__ == '__main__':
    rs = str_reverse2(s)
    print(rs)
