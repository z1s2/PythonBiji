#排序：
def bubble_sort(data):
    for i in range(0,len(data)-1):
        for j in range(0,len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data

s = bubble_sort([8,2,5,3,6,9,4])
print(s)












