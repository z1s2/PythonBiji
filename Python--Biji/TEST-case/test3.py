
#：
L =[]  #定一个空的列表用于存储数据
for i in range (2000,2050):
    if (i%7 == 0)and(i%5 != 0):
        L.append(str(i))
print(',' .join(L))
        # for j in L:
print((L))

#：
def demo(*parm):
    print(parm)
    print(type(parm))
240684434818
demo(1,2,3,4,5,6)



n = int(input('Enter a number'))
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print(d)

def numbeer(n):
    d = dict()
    for i in range(1,n+1):
        d[i] = i*i
    return d
# print(numbeer(4))

print(numbeer(5))

#

x = 'abc'
y = 123
isinstance(x,str)
print(x)

d={'k1':111,'k2':2222}
# d.get('k1')

print(d.get('k1'))
print(d['k2'])